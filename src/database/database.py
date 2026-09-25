import sqlite3
from pathlib import Path

db_path = Path(__file__).resolve().parent.parent / "data" / "iran_export.db"

connection = sqlite3.connect(db_path)

print("Database created successfully.")

connection.close()