# Provide a way of using operating system dependent functionality
import os
# Read, add to env variable key-value pair from .env
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "<YourOpenAIKey>")

# MongoDB Connection String
MONGODB_CONNECTION_STRING = os.getenv("MONGODB_CONNECTION_STRING", "<YourMongoDBConnectionString>")

# Database Name
DATABASE_NAME = os.getenv("DATABASE_NAME", "<YourDatabaseName>")
