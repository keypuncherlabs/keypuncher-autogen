import autogen
from config.llm_config import llm_config

class AssistantAgent:
    def __init__(self):
        self.assistant = autogen.AssistantAgent(
            name='assistant',
            system_message='You are a coder specializing in Python',
            llm_config=llm_config
        )
    
    # Add more methods as needed
