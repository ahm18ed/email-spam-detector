from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

MODEL_PATH = PROJECT_ROOT / "models" / "spam_classifier.pkl"
VECTORIZER_PATH = PROJECT_ROOT / "models" / "tfidf_vectorizer.pkl"

def test_model_file_exists():
    assert MODEL_PATH.exists()

def test_vectorizer_file_exists():
    assert VECTORIZER_PATH.exists()