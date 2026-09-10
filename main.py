from speech.Listen import speech_stream
from core.decision_model import predict_intent
from core.command_logger import log_command
from core.speech_correction import save_correction
from core.text_normalizer import normalize_text
from agents.automation_agent import execute_automation


for raw_text, audio_file in speech_stream():

    print("\nRaw STT:", raw_text)

    # --------------------------------
    # STEP 1: Save speech correction data
    # --------------------------------

    answer = input("Was the transcription correct? (y/n): ")

    if answer.lower() == "y":
        corrected_text = raw_text

    else:
        corrected_text = input("What did you actually say? : ")

    save_correction(
        audio_file,
        raw_text,
        corrected_text
    )

    # --------------------------------
    # STEP 2: Normalize / translate
    # --------------------------------

    normalized_text = normalize_text(corrected_text)

    print("Normalized:", normalized_text)

    # --------------------------------
    # STEP 3: Intent prediction
    # --------------------------------

    intent, confidence = predict_intent(normalized_text)

    print("Intent:", intent)
    print("Confidence:", round(confidence, 2))

    # --------------------------------
    # STEP 4: Log command
    # --------------------------------

    log_command(
        corrected_text,
        intent,
        confidence
    )

    # --------------------------------
    # STEP 5: Execute
    # --------------------------------

    if intent == "AUTOMATION":

        result = execute_automation(normalized_text)

        print("Jarvis:", result)

    elif intent == "GENERAL":

        print("General agent coming soon...")

    elif intent == "REAL_TIME":

        print("Real-time agent coming soon...")