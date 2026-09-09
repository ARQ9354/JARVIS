import csv
from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent.parent

METADATA_FILE = (
    BASE_DIR
    / "data"
    / "speech_dataset"
    / "metadata.csv"
)


def save_correction(audio_file, stt_text, corrected_text):

    file_exists = METADATA_FILE.exists()

    with open(
        METADATA_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "audio_file",
                "stt_text",
                "corrected_text"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            audio_file,
            stt_text,
            corrected_text
        ])