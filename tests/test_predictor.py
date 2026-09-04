from src.model.predictor import predict_email


def test_prediction_returns_valid_class():
    prediction, probability = predict_email(
        "Congratulations! You have won a free prize!"
    )

    assert prediction in (1, 0)

def test_prediction_returns_valid_probability():
    prediction, probability = predict_email(
        "Congratulations! You have won a free prize!"
    )

    assert 0.0 <= probability <= 1.0

def test_prediction_returns_valid_type():
    prediction, probability = predict_email(
        "Congratulations! You have won a free prize!"
    )

    assert isinstance(prediction, int)
    assert isinstance(probability, float)