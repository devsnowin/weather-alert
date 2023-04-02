import os
from dotenv import load_dotenv

# Loads the environment variables from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')
END_POINT = 'https://api.openweathermap.org/data/2.5'
NAME = 'Jeno'