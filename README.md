# 🪶 **hams_ollo & AI 🤖**  

A Multi-Agent, Voice-Powered AI Assistant for Productivity, Podcasting, and Beyond

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Latest-green)](https://github.com/joaomdmoura/crewAI)
[![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## **📖 Project Overview**

**Welcome to the future of AI-powered collaboration.**  
🪶 **hams_ollo & AI 🤖** is an innovative open-source project that leverages CrewAI's multi-agent framework to create an intelligent assistant capable of handling complex tasks through specialized agents. Built with Groq's state-of-the-art language models and a modern Streamlit interface, this system demonstrates the power of collaborative AI in automating tasks, generating content, and facilitating meaningful interactions.

---

## **✨ Key Features**

1. **CrewAI Multi-Agent System**:  
   - Specialized agents working together:
     - Lead Conversational Assistant
     - Scheduling Assistant
     - Content Creation Assistant
     - Podcast Production Assistant
   - Dynamic task delegation based on agent expertise
   - Seamless inter-agent communication

2. **Advanced Language Model**:  
   - Powered by Groq's Llama 3 70B model
   - High-performance inference
   - Context-aware responses

3. **Modern User Interface**:  
   - Clean, intuitive Streamlit frontend
   - Real-time chat interface
   - Settings customization
   - User feedback system

4. **Smart Features**:  
   - Conversation memory
   - Context persistence
   - Dynamic temperature control
   - Comprehensive error handling

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
