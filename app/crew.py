from crewai import Crew, Process
from typing import Dict, List, Any
import yaml
import os

from agents.chat_agent import ChatAgent
from agents.scheduling_agent import SchedulingAgent
from agents.content_agent import ContentAgent
from agents.podcast_agent import PodcastAgent
from utils.voice_utils import VoiceUtils
from utils.db_utils import DatabaseUtils

class AssistantCrew:
    def __init__(self, config_path: str = "config"):
        """Initialize the Assistant Crew with configuration"""
        self.config_path = config_path
        self.agents_config = self._load_config("agents.yaml")
        self.tasks_config = self._load_config("tasks.yaml")
        
        # Initialize utilities
        self.voice_utils = VoiceUtils()
        self.db_utils = DatabaseUtils("assistant.db")
        
        # Initialize agents
        self.agents = self._initialize_agents()
        
        # Create the crew
        self.crew = Crew(
            agents=list(self.agents.values()),
            process=Process.sequential  # Can be changed to hierarchical if needed
        )

    def _load_config(self, filename: str) -> Dict:
        """Load configuration from YAML file"""
        config_file = os.path.join(self.config_path, filename)
        with open(config_file, 'r') as f:
            return yaml.safe_load(f)

    def _initialize_agents(self) -> Dict:
        """Initialize all agents from configuration"""
        agents = {}
        
        # Initialize each agent type
        if 'chat_agent' in self.agents_config:
            agents['chat'] = ChatAgent()
        
        if 'scheduling_agent' in self.agents_config:
            agents['scheduling'] = SchedulingAgent()
            
        if 'content_agent' in self.agents_config:
            agents['content'] = ContentAgent()
            
        if 'podcast_agent' in self.agents_config:
            agents['podcast'] = PodcastAgent()
            
        return agents

    def process_user_input(self, user_input: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Process user input and coordinate agent responses"""
        try:
            # Determine which agents should handle the input
            # This could be enhanced with task classification
            results = {}
            
            # Chat agent always processes the input
            if 'chat' in self.agents:
                chat_response = self.agents['chat'].process_message(user_input)
                results['chat'] = chat_response
            
            # Check if input requires scheduling
            if 'scheduling' in self.agents and any(keyword in user_input.lower() 
                for keyword in ['schedule', 'meeting', 'appointment', 'calendar']):
                schedule_response = self.agents['scheduling'].process_message(user_input)
                results['scheduling'] = schedule_response
            
            # Check if input requires content creation
            if 'content' in self.agents and any(keyword in user_input.lower() 
                for keyword in ['content', 'post', 'blog', 'social media']):
                content_response = self.agents['content'].process_message(user_input)
                results['content'] = content_response
            
            # Check if input requires podcast handling
            if 'podcast' in self.agents and any(keyword in user_input.lower() 
                for keyword in ['podcast', 'episode', 'show notes']):
                podcast_response = self.agents['podcast'].process_message(user_input)
                results['podcast'] = podcast_response
            
            # Save the interaction
            self.db_utils.save_conversation(
                user_message=user_input,
                ai_response=str(results),
                metadata=context
            )
            
            return results
            
        except Exception as e:
            logging.error(f"Error processing user input: {str(e)}")
            return {"error": str(e)}

    def get_agent(self, agent_type: str):
        """Get a specific agent by type"""
        return self.agents.get(agent_type)

    def run_task(self, task_name: str, **kwargs) -> Any:
        """Run a specific task from the tasks configuration"""
        if task_name not in self.tasks_config:
            raise ValueError(f"Task {task_name} not found in configuration")
        
        task_config = self.tasks_config[task_name]
        agent = self.agents.get(task_config['agent'])
        
        if not agent:
            raise ValueError(f"Agent {task_config['agent']} not found")
        
        return agent.run_task(task_config, **kwargs)
