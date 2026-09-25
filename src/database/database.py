import sqlite3
from pathlib import Path


db_path = Path(__file__).resolve().parent.parent.parent / "data" / "iran_export.db"
db_path.parent.mkdir(parents=True, exist_ok=True)

connection = sqlite3.connect(db_path)

print("Database created successfully.")

connection.close()