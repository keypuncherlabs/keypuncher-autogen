import argparse
from agents.assistant_agent import AssistantAgent
from agents.user_proxy_agent import UserProxyAgent
from agents.retrieve_assistant_agent import RetrieveAssistantAgent
from agents.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from utils.utils import Utils


def main():
    parser = argparse.ArgumentParser(
        description='Run Autogen with a specified prompt file.')
    parser.add_argument('prompt_file', nargs='?', default='generate_random_numbers.txt',
                        help='Prompt file name (default: generate_random_numbers.txt)')
    args = parser.parse_args()

    assistant_agent = AssistantAgent()
    user_proxy_agent = UserProxyAgent()
    retrieve_assistant_agent = RetrieveAssistantAgent()
    retrieve_user_proxy_agent = RetrieveUserProxyAgent()

    # Query a local document
    # retrieve_assistant_agent.assistant.reset()
    # retrieve_user_proxy_agent.ragproxyagent.initiate_chat(retrieve_assistant_agent.assistant, problem="What is Keypuncher Autogen?")

    # # Create the prompt using the utility function
    prompt = Utils.create_prompt(args.prompt_file)

    if prompt:
        # Initiate chat with Autogen
        user_proxy_agent.user_proxy.initiate_chat(
            assistant_agent.assistant, message=prompt)

        # Handle the chat response
        # Note: Implement a loop or logic to handle ongoing interaction depending on how your Autogen system is set up.
        # print("Autogen Response: ", response)


if __name__ == "__main__":
    main()
