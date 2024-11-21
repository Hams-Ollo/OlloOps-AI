
#-------------------------------------------------------------------------------------#
# File: chat_agent.py
# Description: Custom chat agent implementation using Groq's Mixtral model for conversational AI
# Author: @hams_ollo
#
# INITIAL SETUP:
# 1. Create virtual environment:    python -m venv venv
# 2. Activate virtual environment:
#    - Windows:                    .\venv\Scripts\activate
#    - Unix/MacOS:                 source venv/bin/activate
# 3. Install requirements:         pip install -r requirements.txt
# 4. Create .env file:            cp .env.example .env
# 5. Update dependencies:          pip freeze > requirements.txt
#
#-------------------------------------------------------------------------------------#
#----------# IMPORTS  #----------#
from typing import List, Dict, Any, Optional
import logging
import groq