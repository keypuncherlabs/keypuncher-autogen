import autogen
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent as AutogenRetrieveAssistantAgent
from config.llm_config import llm_config


class RetrieveAssistantAgent:
    def __init__(self):
        self.assistant = AutogenRetrieveAssistantAgent(
            name="assistant",
            system_message="You are a helpful assistant.",
            llm_config=llm_config,
        )

    # Add more methods as needed
