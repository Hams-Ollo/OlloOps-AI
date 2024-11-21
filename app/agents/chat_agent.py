#-------------------------------------------------------------------------------------#
# File: chat_agent.py
# Description: Lead conversational agent implementation using CrewAI and Groq's Llama 3
# Author: @hams_ollo
# 
# This agent serves as the primary interface for user interactions, managing:
# - Conversation flow and context management
# - Task delegation to specialized agents
# - Response generation and formatting
# - Memory management and conversation history
#-------------------------------------------------------------------------------------#
import os
from typing import Dict, Any, List
from crewai import Agent, Task, Crew
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

class ChatAgent:
    def __init__(self):
        """Initialize the chat agent with Groq LLM"""
        self.model = os.getenv("GROQ_MODEL", "llama3-groq-70b-8192-tool-use-preview")
        self.conversation_history = []
        
        # Initialize CrewAI agents
        self.chat_agent = Agent(
            role='Lead Conversational Assistant',
            goal='Engage in natural, helpful conversation and coordinate with other agents',
            backstory="""You are an expert conversational AI assistant with deep knowledge 
            across various domains. You excel at understanding context, providing helpful 
            responses, and maintaining engaging conversations.""",
            allow_delegation=True,
            verbose=True,
            llm=self.create_groq_llm()
        )
        
        self.scheduling_agent = Agent(
            role='Scheduling Assistant',
            goal='Handle scheduling and time management tasks',
            backstory="""You are an expert in scheduling and time management. You help users
            organize their time effectively and manage their calendar.""",
            allow_delegation=True,
            verbose=True,
            llm=self.create_groq_llm()
        )
        
        self.content_agent = Agent(
            role='Content Creation Assistant',
            goal='Create and optimize various types of content',
            backstory="""You are an expert in content creation and optimization. You help users
            create engaging and effective content across different formats.""",
            allow_delegation=True,
            verbose=True,
            llm=self.create_groq_llm()
        )
        
        # Initialize the crew
        self.crew = Crew(
            agents=[self.chat_agent, self.scheduling_agent, self.content_agent],
            tasks=[],
            verbose=True
        )

    def create_groq_llm(self):
        """Create a Groq LLM configuration for the agent"""
        from langchain_groq import ChatGroq
        
        return ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name=self.model,
            temperature=0.7,
            max_tokens=4096
        )

    def process_message(self, message: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Process a user message and return a response"""
        try:
            # Add message to conversation history
            self.conversation_history.append({"role": "user", "content": message})
            
            # Create LLM instance
            llm = self.create_groq_llm()
            
            # Prepare messages for chat
            messages = [
                {"role": "system", "content": self.chat_agent.backstory},
                *self.conversation_history[-10:]  # Include last 10 messages for context
            ]
            
            # Generate response
            response = llm.invoke(messages)
            
            # Add response to conversation history
            self.conversation_history.append({"role": "assistant", "content": response})
            
            # Create and process any necessary tasks based on the message
            if self._requires_scheduling(message):
                task = Task(
                    description=f"Schedule task: {message}",
                    agent=self.scheduling_agent
                )
                self.crew.tasks.append(task)
            
            if self._requires_content_creation(message):
                task = Task(
                    description=f"Create content: {message}",
                    agent=self.content_agent
                )
                self.crew.tasks.append(task)
            
            # Process any pending tasks
            if self.crew.tasks:
                crew_result = self.crew.kickoff()
                response += f"\n\nAdditional insights from the crew:\n{crew_result}"
            
            return {
                "response": response,
                "success": True
            }
            
        except Exception as e:
            return {
                "response": f"I apologize, but I encountered an error: {str(e)}",
                "success": False,
                "error": str(e)
            }
    
    def _requires_scheduling(self, message: str) -> bool:
        """Check if the message requires scheduling assistance"""
        scheduling_keywords = ['schedule', 'appointment', 'meeting', 'calendar', 'remind']
        return any(keyword in message.lower() for keyword in scheduling_keywords)
    
    def _requires_content_creation(self, message: str) -> bool:
        """Check if the message requires content creation assistance"""
        content_keywords = ['write', 'create', 'draft', 'content', 'article', 'blog']
        return any(keyword in message.lower() for keyword in content_keywords)
