# Development Guide moved to docs/DEVELOPMENT.md

import os
import sys
import logging
import subprocess
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('logs/app.log')
    ]
)
logger = logging.getLogger(__name__)

def setup_environment():
    """Setup the application environment"""
    try:
        # Load environment variables
        load_dotenv()
        
        # Ensure required environment variables are set
        required_vars = ['GROQ_API_KEY', 'GROQ_MODEL']
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        if missing_vars:
            raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
        # Create logs directory if it doesn't exist
        os.makedirs('logs', exist_ok=True)
        
        logger.info("Environment setup completed successfully")
        return True
    except Exception as e:
        logger.error(f"Environment setup failed: {str(e)}")
        return False

def start_streamlit():
    """Start the Streamlit application"""
    try:
        logger.info("Starting Streamlit application...")
        streamlit_path = os.path.join('frontend', 'streamlit.py')
        process = subprocess.Popen(
            ['streamlit', 'run', streamlit_path, '--server.port', '8501'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return process
    except Exception as e:
        logger.error(f"Failed to start Streamlit: {str(e)}")
        return None

def main():
    """Main application entry point"""
    logger.info("Starting AI Assistant application...")
    
    # Setup environment
    if not setup_environment():
        logger.error("Failed to setup environment. Exiting...")
        sys.exit(1)
    
    # Start Streamlit
    streamlit_process = start_streamlit()
    if not streamlit_process:
        logger.error("Failed to start Streamlit. Exiting...")
        sys.exit(1)
    
    try:
        # Keep the main process running
        while True:
            output = streamlit_process.stdout.readline()
            if output:
                logger.info(output.strip())
            
            error = streamlit_process.stderr.readline()
            if error:
                logger.error(error.strip())
            
            # Check if Streamlit process has ended
            if streamlit_process.poll() is not None:
                break
    except KeyboardInterrupt:
        logger.info("Shutting down application...")
    finally:
        if streamlit_process:
            streamlit_process.terminate()
            streamlit_process.wait()
    
    logger.info("Application shutdown complete")

if __name__ == "__main__":
    main()
