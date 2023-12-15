import os
from datetime import datetime
from todoist_api_python.api import TodoistAPI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve the Todoist API token from an environment variable
TODOIST_API_TOKEN = os.getenv('TODOIST_API_TOKEN')


def main():
    print('hello world! Your environment variable is: ' + TODOIST_API_TOKEN)


if __name__ == "__main__":
    main()
