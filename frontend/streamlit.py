#-------------------------------------------------------------------------------------#
# File: streamlit.py
# Description: Streamlit-based frontend interface for the Podcast and AI Assistant application
# Author: @hams_ollo
# Version: 0.0.3
# Last Updated: [2024-11-21]
# Run: streamlit run frontend/streamlit.py
#-------------------------------------------------------------------------------------#
import os
import sys
import logging
from datetime import datetime
import streamlit as st
from dotenv import load_dotenv

# Add the app directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.agents.chat_agent import ChatAgent

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('logs/streamlit.log')
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'chat_agent' not in st.session_state:
    try:
        logger.info("Initializing ChatAgent...")
        st.session_state.chat_agent = ChatAgent()
        logger.info("ChatAgent initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize ChatAgent: {str(e)}", exc_info=True)
        st.error(f"Failed to initialize AI Assistant: {str(e)}")
        st.stop()
if 'show_settings' not in st.session_state:
    st.session_state.show_settings = False

# Streamlit UI
st.title("🪶 hams_ollo & AI 🤖")

# Sidebar
with st.sidebar:
    st.subheader("Settings")
    if st.button("Toggle Settings"):
        st.session_state.show_settings = not st.session_state.show_settings
    
    if st.session_state.show_settings:
        st.write("Chat Settings")
        temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
        max_tokens = st.slider("Max Tokens", 1000, 8192, 4096, 100)
        
        if st.button("Clear Chat History"):
            st.session_state.messages = []
            st.session_state.chat_agent.conversation_history = []
            st.rerun()

# Main chat interface
st.subheader("Your AI Assistant")

# Display chat messages
for idx, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant":
            message_container = st.container()
            with message_container:
                col1, col2 = st.columns([0.1, 0.9])
                with col1:
                    if st.button("👍", key=f"like_msg_{idx}"):
                        st.toast("Thanks for the feedback!")
                with col2:
                    if st.button("👎", key=f"dislike_msg_{idx}"):
                        feedback = st.text_input("What could be improved?", key=f"feedback_msg_{idx}")
                        if feedback:
                            st.toast("Thanks for your feedback!")

# Chat input
if prompt := st.chat_input("What's on your mind?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.chat_agent.process_message(prompt)
                if response["success"]:
                    st.markdown(response["response"])
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response["response"]
                    })
                    
                    # Add feedback buttons
                    message_container = st.container()
                    with message_container:
                        col1, col2 = st.columns([0.1, 0.9])
                        with col1:
                            if st.button("👍", key=f"like_new_msg_{len(st.session_state.messages)}"):
                                st.toast("Thanks for the feedback!")
                        with col2:
                            if st.button("👎", key=f"dislike_new_msg_{len(st.session_state.messages)}"):
                                feedback = st.text_input("What could be improved?", key=f"feedback_new_msg_{len(st.session_state.messages)}")
                                if feedback:
                                    st.toast("Thanks for your feedback!")
                else:
                    st.error(f"Error: {response.get('error', 'Unknown error occurred')}")
            except Exception as e:
                logger.error(f"Error processing message: {str(e)}", exc_info=True)
                st.error("I apologize, but I encountered an error processing your message. Please try again.")
