from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from dotenv import load_dotenv
from pathlib import Path
import os

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from a .env file located in the base directory
load_dotenv(BASE_DIR / ".env")

# Get the user model from Django's auth system
User = get_user_model()

class Command(BaseCommand):
    """
    A custom Django management command to create a superuser if one does not already exist.
    """

    def handle(self, *args, **options):
        """
        Execute the command to check for an existing superuser and create one if necessary.

        :param args: Positional arguments (not used in this command).
        :param options: Keyword arguments (not used in this command).
        """
        # Retrieve superuser credentials from environment variables
        username = os.getenv('ADMIN_USERNAME')
        email = os.getenv('ADMIN_EMAIL')
        password = os.getenv("ADMIN_PASSWORD")

        try:
            # Check if a superuser with the specified username or any superuser exists
            if not User.objects.filter(username=username).exists() and not User.objects.filter(is_superuser=True).exists():
                print("Admin user not found, creating one")

                # Create a new superuser with the specified credentials
                User.objects.create_superuser(username, email, password)
                print(f"===================================")
                print(f"A superuser '{username}' was created with email '{email}' and password '{password}'")
                print(f"===================================")
            else:
                print("Admin user found. Skipping superuser creation")
        except Exception as e:
            # Print any errors that occur during superuser creation
            print(f"There was an error: {e}")
