# Development Guide

## Initial Setup

1. Create virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate virtual environment:
   - Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - Unix/MacOS:

     ```bash
     source venv/bin/activate
     ```

3. Install requirements:

   ```bash
   pip install -r requirements.txt
   ```

4. Create .env file:

   ```bash
   cp .env.example .env
   ```

5. Update dependencies:

   ```bash
   pip freeze > requirements.txt
   ```

## Python Development Commands

### Package Management

1. List outdated packages:

   ```bash
   pip list --outdated
   ```

2. Show package info:

   ```bash
   pip show package_name
   ```

3. Uninstall package:

   ```bash
   pip uninstall package_name
   ```

4. Install dev dependencies:

   ```bash
   pip install -r requirements-dev.txt
   ```

5. Upgrade pip:

   ```bash
   python -m pip install --upgrade pip
   ```

6. Install package:

   ```bash
   pip install package_name==version
   ```

### Virtual Environment

1. List installed packages:

   ```bash
   pip list
   ```

2. Export dependencies:

   ```bash
   pip freeze > requirements.txt
   ```

3. Deactivate venv:

   ```bash
   deactivate
   ```

4. Remove venv:

   ```bash
   rm -rf venv
   ```

## Streamlit Commands

### Development

1. Run app:

   ```bash
   python main.py
   ```

2. Run with custom port:

   ```bash
   streamlit run frontend/streamlit.py --server.port 8502
   ```

3. Enable debug mode:

   ```bash
   streamlit run frontend/streamlit.py --logger.level=debug
   ```

4. Clear cache:

   ```bash
   streamlit cache clear
   ```

5. Show all config options:

   ```bash
   streamlit config show
   ```

6. Create new component:

   ```bash
   streamlit create my_component
   ```

## Agent System Architecture

The application uses CrewAI to implement a multi-agent system with the following specialized agents:

1. **Lead Conversational Agent** (`chat_agent.py`)
   - Primary interface for user interactions
   - Manages conversation flow and context
   - Delegates tasks to specialized agents

2. **Scheduling Agent** (`scheduling_agent.py`)
   - Handles calendar and scheduling tasks
   - Manages appointments and reminders
   - Optimizes time management

3. **Content Creation Agent** (`content_agent.py`)
   - Generates and formats content
   - Provides writing assistance
   - Optimizes content for different platforms

4. **Podcast Production Agent** (`podcast_agent.py`)
   - Creates podcast scripts and outlines
   - Manages episode planning
   - Generates show notes and summaries
   - Provides audio content recommendations

Each agent is implemented as a separate module in the `app/agents/` directory and inherits from the CrewAI Agent class.

## Git Commands

### Basic Operations

1. Initialize repository:

   ```bash
   git init
   ```

2. Add files to staging:

   ```bash
   git add .
   ```

3. Commit changes:

   ```bash
   git commit -m "your message"
   ```

4. Push to remote:

   ```bash
   git push -u origin branch-name
   ```

5. Pull latest changes:

   ```bash
   git pull origin branch-name
   ```

### Branching

1. Create & switch branch:

   ```bash
   git checkout -b branch-name
   ```

2. Switch branches:

   ```bash
   git checkout branch-name
   ```

3. List branches:

   ```bash
   git branch
   ```

4. Delete branch:

   ```bash
   git branch -d branch-name
   ```

5. Merge branch:

   ```bash
   git merge branch-name
   ```

### Advanced Operations

1. Fetch updates:

   ```bash
   git fetch origin
   ```

2. Rebase branch:

   ```bash
   git rebase main
   ```

3. Cherry-pick commit:

   ```bash
   git cherry-pick commit-hash
   ```

4. Reset to commit:

   ```bash
   git reset --hard commit-hash
   ```

5. Clean untracked files:

   ```bash
   git clean -fd
   ```
