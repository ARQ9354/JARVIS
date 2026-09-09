from speech.Listen import speech_stream
from core.decision_model import predict_intent
from core.command_logger import log_command
from core.speech_correction import save_correction
from agents.automation_agent import execute_automation


for user_input, audio_file in speech_stream():

    print("User:", user_input)

    intent, confidence = predict_intent(user_input)

    print("Intent:", intent)
    print("Confidence:", round(confidence, 2))

    log_command(
        user_input,
        intent,
        confidence
    )

    # Temporary confirmation
    answer = input(
        "Was this transcription correct? (y/n): "
    )

    if answer.lower() == "y":
        save_correction(
        audio_file,
        user_input,
        user_input
    )


    else:
        corrected_text = input("What did you actually say? : ")
        save_correction(
        audio_file,
        user_input,
        corrected_text
        )

        
        # Use corrected command
        user_input = corrected_text
        intent, confidence = predict_intent(user_input)

    # Automation
    if intent == "AUTOMATION":

        result = execute_automation(user_input)

        print("Jarvis:", result)