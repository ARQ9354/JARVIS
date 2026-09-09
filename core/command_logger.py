import csv
from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent.parent

LOG_FILE = BASE_DIR / "data" / "real_world_commands.csv"


def log_command(text, predicted_intent, confidence=None):
    """
    User command ko real-world dataset mein save karta hai.
    """

    file_exists = LOG_FILE.exists()

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        # Agar file pehli baar ban rahi hai
        if not file_exists:
            writer.writerow([
                "timestamp",
                "text",
                "predicted_intent",
                "confidence",
                "correct_intent"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            text,
            predicted_intent,
            confidence,
            ""
        ])