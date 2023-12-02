from agents.assistant_agent import AssistantAgent
from agents.user_proxy_agent import UserProxyAgent


def main():
    assistant_agent = AssistantAgent()
    user_proxy_agent = UserProxyAgent()

    # Read the generate numbers prompt
    with open('prompts/generate_random_numbers.txt', 'r') as file:
        generate_numbers_prompt = file.read()

    # Read the general instructions
    with open('prompts/general_instructions.txt', 'r') as file:
        general_instructions = file.read()

    # Combine both prompts
    combined_prompt = generate_numbers_prompt + "\n" + general_instructions

    # Initiate chat with Autogen
    user_proxy_agent.user_proxy.initiate_chat(
        assistant_agent.assistant, message=combined_prompt)

    # Handle the chat response
    # Note: This is a simplified example. You'll need to implement a loop or some logic
    # to handle ongoing interaction depending on how your Autogen system is set up.
    # print("Autogen Response: ", response)


if __name__ == "__main__":
    main()
