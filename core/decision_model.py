import joblib
from pathlib import Path


# JARVIS project ka root folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Model paths
MODEL_PATH = BASE_DIR / "models" / "intent_model.pkl"
VECTORIZER_PATH = BASE_DIR / "models" / "tfidf_vectorizer.pkl"


# Trained ML model aur TF-IDF vectorizer load karo
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)



def predict_intent(text):

    text_vector = vectorizer.transform([text])

    intent = model.predict(text_vector)[0]

    probabilities = model.predict_proba(text_vector)[0]

    confidence = max(probabilities)

    return intent, confidence




if __name__ == "__main__":

    test_commands = [
        "chrome kholo",
        "machine learning kya hai",
        "aaj Delhi ka weather kaisa hai",
        "volume badha do",
        "explain neural networks",
        "what is the latest cricket score"
    ]

    for command in test_commands:
        result = predict_intent(command)
        print(f"{command}  -->  {result}")