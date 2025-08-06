import os
from dotenv import load_dotenv
from pathlib import Path

# .env laden
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR}/data/sommerlager.db")
