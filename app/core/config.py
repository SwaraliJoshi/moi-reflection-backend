import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MONGO_DB_URL: str = os.getenv("MONGO_DB_URL", "mongodb://localhost:27017")
    DB_NAME: str = os.getenv("DB_NAME", "todo_app")

settings = Settings()
