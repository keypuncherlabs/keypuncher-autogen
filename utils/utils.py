class Utils:
    @staticmethod
    def create_prompt(file_name):
        """
        Creates a prompt by combining the content from the specified file with general instructions.

        :param file_name: Name of the file to read from (assumed to be in the 'prompts' directory)
        :return: Combined content of the specified file and general_instructions.txt
        """
        try:
            # Read the specified file
            with open(f'prompts/{file_name}', 'r') as file:
                primary_content = file.read()

            # Read the general instructions
            with open('prompts/general_instructions.txt', 'r') as file:
                general_instructions = file.read()

            # Combine both contents
            combined_content = primary_content + "\n" + general_instructions
            return combined_content
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return None
