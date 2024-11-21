# 🪶 **hams_ollo & AI 🤖**  

A Multi-Agent, Voice-Powered AI Assistant for Productivity, Podcasting, and Beyond

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Latest-green)](https://github.com/joaomdmoura/crewAI)
[![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)](https://streamlit.io/)
[![Version](https://img.shields.io/badge/version-0.0.3-blue)](CHANGELOG.txt)
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

2. **Advanced Knowledge Management**:
   - RAG (Retrieval Augmented Generation) system
   - ChromaDB vector store for efficient document storage
   - Support for multiple document formats (PDF, DOCX, TXT, MD)
   - Intelligent text chunking with semantic boundaries
   - Context-aware document retrieval

3. **Advanced Language Model**:  
   - Powered by Groq's Llama 3 70B model
   - High-performance inference
   - Context-aware responses
   - Enhanced with RAG capabilities

4. **Modern User Interface**:  
   - Clean, intuitive Streamlit frontend
   - Real-time chat interface
   - Settings customization
   - User feedback system

5. **Smart Features**:  
   - Conversation memory
   - Document-aware responses
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

1. **Multi-Agent System**
   - CrewAI framework for agent orchestration
   - Specialized agents for different tasks
   - Task delegation system

2. **Knowledge Management**
   - RAG system with ChromaDB
   - Document processing pipeline
   - Semantic text chunking
   - Vector-based retrieval

3. **Language Model Integration**
   - Groq's Llama 3 70B
   - Context management
   - Temperature control
   - Token optimization

4. **User Interface**
   - Streamlit frontend
   - Real-time updates
   - Settings management
   - Error handling

---

## **🤝 Contributing**

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on:

- Development workflow
- Branch structure
- Code standards
- Pull request process

For future plans and roadmap, check our [Roadmap](ROADMAP.md).

---

## **📄 License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **🙏 Acknowledgments**

- CrewAI team for the multi-agent framework
- Groq for the powerful language models
- Open source community for various tools and libraries

---

**Version**: 0.0.3 - See [CHANGELOG.txt](CHANGELOG.txt) for details

Last Updated: [2024-11-21]
