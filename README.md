# Keypuncher Autogen

This repository serves as a starter template for Autogen projects. It is designed to be a base from which you can quickly bootstrap new Autogen projects to run on local systems. It is structured to ensure ease of use and scalability without containing any keys or secrets.

## Getting Started

1. **Setup Python Environment with Conda**  
   Ensure you have [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed on your system. Set up a Conda environment using:

   ```bash
   conda create --name keypuncher-autogen python=3.11.5
   conda activate keypuncher-autogen
   ```

2. **Install Dependencies**  
   Install the required packages including Autogen using pip:

   ```bash
    pip install -r requirements.txt
    # Ensure autogen is included in the requirements.txt file
    # If not, you can install it directly using:
    pip install pyautogen
   ```

3. **Environment Variables**  
   Create a .env file in the root of your project to store sensitive keys and secrets, which should never be committed to your repository.

4. **Running the Application**  
   To run the application, execute the main.py script:

   ```bash
   python main.py
   ```

   Or specify the prompt: (replace your_prompt_file.txt with the name of your prompt file located in the /prompts directory)

   ```bash
   python main.py your_prompt_file.txt
   ```

## Adding Prompts

**To add a new prompt:**

  Create a new .txt file in the /prompts directory with your prompt content.
  Ensure the main.py or respective agent scripts reference the new prompt file.

## Caching

Caching in Autogen is used to speed up the generation process by storing some of the results and intermediate data. This allows Autogen to retrieve data quickly without regenerating it, which is especially beneficial when working with large datasets or complex generation tasks.

#### How Caching Works

Autogen typically uses a combination of in-memory and on-disk caching strategies. In-memory caching is ephemeral and lasts only for the duration of the program execution. On-disk caching saves data between sessions, which is where the generated files are often stored.

#### Clearing the Cache

To clear the cache in Autogen, you have two primary methods:

1. **Update the Seed Variable**  
   If your Autogen configuration includes a seed variable (like the `seed` key in the `llm_config`), changing this variable can effectively invalidate the cache. For example, changing the seed from `41` to another number will cause Autogen to regenerate data since it alters the generation process.

2. **Delete the Cache Directory Manually**
   Autogen may store cache files in a specific directory. To clear the cache, you can delete this directory. Ensure you close any running Autogen processes before doing so to prevent errors. The location of this directory depends on your specific Autogen setup, but you can typically find it in the generated directory or a .cache directory.

   ```bash
   rm -rf .cache/*     # If cache is stored in a '.cache' directory, use this command

   rm -rf generated/*  # This command deletes all cached files in the 'generated' directory
   ```

## Running on Local Systems
This project is designed to run locally. Follow the setup steps in the 'Getting Started' section above to ensure the application is configured correctly on your system.

## Contributing
Feel free to fork this repository and customize it to fit your needs. If you wish to contribute to this template, create a pull request with your proposed changes.

## License
This project is open source and available under the MIT License.

## Support
If you encounter any problems or have suggestions, please open an issue in the repository.

