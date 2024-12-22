# 🪶 **OlloOps AI: Multi-Agent Assistant for Intelligent Operations**  

A voice-powered, multi-agent AI productivity suite designed for collaboration, creativity, and advanced task orchestration.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Latest-green)](https://github.com/joaomdmoura/crewAI)
[![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## **📖 Project Overview**

**Welcome to OlloOps AI**  
OlloOps AI is an open-source, voice-powered platform built to demonstrate the transformative power of **multi-agent systems**. Leveraging **CrewAI's multi-agent orchestration framework**, **Groq's cutting-edge language models**, and an intuitive **Streamlit interface**, OlloOps AI empowers users to automate complex workflows, collaborate seamlessly, and maximize productivity.  

---

## **✨ Key Features**

1. **Dynamic Multi-Agent System**:  
   - Specialized agents working collaboratively:
     - **Lead Conversational Assistant**: Manages user interaction and delegates tasks.
     - **Scheduling Assistant**: Handles calendar management, reminders, and time-based tasks.
     - **Content Creation Assistant**: Supports content ideation, generation, and optimization.
     - **Podcast Production Assistant**: Automates workflows for audio content production.
   - Agents dynamically delegate and communicate based on task complexity.

2. **State-of-the-Art AI Capabilities**:  
   - Powered by **Groq’s Llama 3 70B model** for high-performance language understanding.
   - Supports **context-aware responses** and natural conversations.

3. **Modern User Experience**:  
   - Interactive **Streamlit frontend** with a real-time chat interface.
   - Customizable settings and a robust user feedback system.

4. **Smart Features for Scalability**:  
   - Conversation memory and context persistence.
   - Dynamic temperature control for response fine-tuning.
   - Comprehensive error handling for robust operations.

---

## **🚀 Getting Started**

### Prerequisites

- Python 3.8 or higher
- Git
- Groq API key

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Hams-Ollo/hams_ollo_ai.git
   cd hams_ollo_ai
   ```

2. **Set Up Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Unix/MacOS
   .\venv\Scripts\activate   # For Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**
   - Copy `.env.example` to `.env`
   - Add your Groq API key

   ```bash
   cp .env.example .env
   ```

5. **Run the Application**

   ```bash
   python main.py
   ```

The application will start and be available at `http://localhost:8501`

---

## **🛠️ Technical Architecture**

### Core Components

1. **AI Framework**:
   - CrewAI for multi-agent orchestration
   - Groq's Llama 3 70B model for language processing

2. **Frontend**:
   - Streamlit for user interface
   - Real-time chat updates
   - Interactive settings controls

3. **Backend**:
   - Python-based application server
   - Environment management
   - Logging system

### Agent System

1. **Lead Conversational Assistant**:
   - Main interface for user interactions
   - Task delegation management
   - Context maintenance

2. **Scheduling Assistant**:
   - Calendar management
   - Time-based task handling
   - Reminder systems

3. **Content Creation Assistant**:
   - Content ideation and generation
   - Writing assistance
   - Format optimization

---

## **📝 Development**

### Project Structure

```bash
hams_ollo_ai/
├── app/
│   ├── agents/
│   │   ├── chat_agent.py
│   │   ├── scheduling_agent.py
│   │   └── content_agent.py
├── frontend/
│   └── streamlit.py
├── docs/
│   └── DEVELOPMENT.md
├── main.py
├── requirements.txt
└── .env
```

### Development Commands

See [DEVELOPMENT.md](docs/DEVELOPMENT.md) for detailed development guidelines and commands.

---

## **🤝 Contributing**

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to:

- Report bugs
- Suggest features
- Submit pull requests
- Follow our coding standards

---

## **📄 License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **🙏 Acknowledgments**

- [CrewAI](https://github.com/joaomdmoura/crewAI) for the multi-agent framework
- [Groq](https://groq.com) for the powerful language model
- [Streamlit](https://streamlit.io) for the amazing UI framework

---

## **📬 Contact**

- GitHub: [@Hams-Ollo](https://github.com/Hams-Ollo)
- Twitter: [@hams_ollo](https://twitter.com/hams_ollo)

---

**Note**: This project is under active development. Features and documentation are regularly updated.
