# Keypuncher Autogen Project Starter

This repository serves as a starter template for Autogen projects. It is designed to be a base from which you can quickly bootstrap new Autogen projects to run on local systems. It is structured to ensure ease of use and scalability without containing any keys or secrets.

## Getting Started

1. **Setup Python Environment**  
   Ensure you have Python installed on your system. It's recommended to use a virtual environment:

   ```bash
   $ python -m venv venv
   $ source venv/bin/activate  # For Windows use `venv\Scripts\activate`

2. **Environment Variables**

  Create a .env file in the root of your project to store sensitive keys and secrets, which should never be committed to your repository.

3. **Running the Application**

  To run the application, execute the main.py script:

  ```bash
  $ python main.py
  ```

# Adding Prompts

**To add a new prompt:**

  Create a new .txt file in the /prompts directory with your prompt content.
  Ensure the main.py or respective agent scripts reference the new prompt file.

## Running on Local Systems
This project is designed to run locally. Follow the setup steps in the 'Getting Started' section above to ensure the application is configured correctly on your system.

## Contributing
Feel free to fork this repository and customize it to fit your needs. If you wish to contribute to this template, create a pull request with your proposed changes.

## License
This project is open source and available under the MIT License.

## Support
If you encounter any problems or have suggestions, please open an issue in the repository.

