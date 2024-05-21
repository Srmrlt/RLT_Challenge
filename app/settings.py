import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME")
DB_PASS = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
DATABASE = "sampleDB"
COLLECTION = "sample_collection"
