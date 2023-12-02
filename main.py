from agents.assistant_agent import AssistantAgent
from agents.user_proxy_agent import UserProxyAgent
from utils.utils import Utils


def main():
    assistant_agent = AssistantAgent()
    user_proxy_agent = UserProxyAgent()

    # Create the prompt using the utility function
    prompt = Utils.create_prompt('fetch_weather.txt')

    if prompt:
        # Initiate chat with Autogen
        user_proxy_agent.user_proxy.initiate_chat(
            assistant_agent.assistant, message=prompt)

        # Handle the chat response
        # Note: You'll need to implement a loop or some logic to handle ongoing interaction
        # depending on how your Autogen system is set up.
        # print("Autogen Response: ", response)


if __name__ == "__main__":
    main()
