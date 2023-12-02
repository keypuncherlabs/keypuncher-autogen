import autogen
from config.llm_config import llm_config

class UserProxyAgent:
    def __init__(self):
        self.user_proxy = autogen.UserProxyAgent(
            name='user_proxy',
            human_input_mode='TERMINATE',
            max_consecutive_auto_reply=10,
            is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
            code_execution_config={
                'work_dir': 'generated',
                'use_docker': False
            },
            llm_config=llm_config,
            system_message='Reply TERMINATE if the task has been resolved at full satisfaction. Otherwise, reply CONTINUE, or the reason why the task is not resolved yet.'
        )
    
    # Add more methods as needed
