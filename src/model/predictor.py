import joblib

from src.preprocessing.cleaning import clean_text

MODEL_PATH = "/home/ahmed/Projects/email-spam-detector/src/models/spam_classifier.pkl"
VECTORIZER_PATH = "/home/ahmed/Projects/email-spam-detector/src/models/tfidf_vectorizer.pkl"

def load_model():
    return joblib.load(MODEL_PATH)

def load_vectorizer():
    return joblib.load(VECTORIZER_PATH)

def predict_email(text):

    # Load the trained model and vectorizer
    model = load_model()
    vectorizer = load_vectorizer()

    # Clean the email
    cleaned_text = clean_text(text)

    # Convert the email into TF-IDF features
    text_vector = vectorizer.transform([cleaned_text])

    # Make prediction
    prediction = model.predict(text_vector)[0]

    # Get probability of Spam
    spam_probability = model.predict_proba(text_vector)[0][1]

    return prediction, spam_probability