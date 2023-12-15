import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve the Todoist API token from an environment variable
TODOIST_API_TOKEN = os.getenv('TODOIST_API_TOKEN')


def main():
    print('hello world! Your environment variable is: ' + TODOIST_API_TOKEN +
          ' at date: ' + datetime.today().strftime('%Y-%m-%d'))


if __name__ == "__main__":
    main()
