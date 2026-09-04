from pathlib import Path

import joblib

from src.preprocessing.cleaning import clean_text

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = PROJECT_ROOT / "models" / "spam_classifier.pkl"
VECTORIZER_PATH = PROJECT_ROOT / "models" / "tfidf_vectorizer.pkl"

# Load the trained model and vectorizer
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def predict_email(text):

    # Clean the email
    cleaned_text = clean_text(text)

    # Convert the email into TF-IDF features
    text_vector = vectorizer.transform([cleaned_text])

    # Make prediction
    prediction = model.predict(text_vector)[0]

    # Get probability of Spam
    spam_probability = model.predict_proba(text_vector)[0][1]

    return int(prediction), float(spam_probability)