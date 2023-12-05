import autogen
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent as AutogenRetrieveUserProxyAgent


class RetrieveUserProxyAgent:
    def __init__(self):
        self.ragproxyagent = AutogenRetrieveUserProxyAgent(
            name="ragproxyagent",
            retrieve_config={
                "task": "qa",
                "docs_path": "https://raw.githubusercontent.com/keypuncherlabs/keypuncher-autogen/main/README.md",
            },
        )

    # Add more methods as needed
