from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

def test_connection():
    try:
        with engine.connect() as conn:
            print("Database connection successful.")
    except Exception as e:
        print(f"Database connection failed: {e}")

test_connection()