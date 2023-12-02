from agents.assistant_agent import AssistantAgent
from agents.user_proxy_agent import UserProxyAgent


def main():
    assistant_agent = AssistantAgent()
    user_proxy_agent = UserProxyAgent()

    # Read the prompt
    with open('prompts/generate_random_numbers.txt', 'r') as file:
        generate_numbers_prompt = file.read()

    # Initiate chat with Autogen
    user_proxy_agent.user_proxy.initiate_chat(
        assistant_agent.assistant, message=generate_numbers_prompt)

    # Handle the chat response
    # Note: This is a simplified example. You'll need to implement a loop or some logic
    # to handle ongoing interaction depending on how your Autogen system is set up.
    # print("Autogen Response: ", response)


if __name__ == "__main__":
    main()
