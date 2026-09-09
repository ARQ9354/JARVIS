import speech_recognition as sr
from mtranslate import translate
from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent.parent

AUDIO_DIR = BASE_DIR / "data" / "speech_dataset" / "audio"
AUDIO_DIR.mkdir(parents=True, exist_ok=True)


def speech_stream():

    recognizer = sr.Recognizer()

    recognizer.dynamic_energy_threshold = True
    recognizer.dynamic_energy_adjustment_damping = 0.15
    recognizer.dynamic_energy_ratio = 1.5
    recognizer.pause_threshold = 0.7
    recognizer.non_speaking_duration = 0.5


    with sr.Microphone() as source:
        print("Microphone opened!")
        print("Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Jarvis Ready!")

        while True:

            try:
                print("Listening...")

                audio = recognizer.listen(
                    source,
                    timeout=None,
                    phrase_time_limit=8
                )


                # Unique ID for this recording
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                audio_filename = f"{timestamp}.wav"

                audio_path = AUDIO_DIR / audio_filename

                # Save raw audio
                with open(audio_path, "wb") as file:
                    file.write(audio.get_wav_data())

                print("Audio saved:", audio_filename)

                # Speech → Text
                text = recognizer.recognize_google(
                    audio,
                    language="en-IN"
                )

                print("Piyush :", text)

                # Hindi/Hinglish → English
                try:
                    translated_text = translate(text, "en", "hi")
                except:
                    translated_text = text

                # Return BOTH text and audio path
                yield translated_text, audio_filename



            except sr.UnknownValueError:
                print("Could not understand...")

            except sr.RequestError as e:
                print("Speech recognition error:", e)

            except Exception as e:
                print("Error:", e)