import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"MailGuard" in response.data


def test_predict_endpoint(client):
    response = client.post(
        "/predict",
        json={
            "email": "Congratulations! You have won a free prize!"
        },
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "prediction" in data
    assert "spam_probability" in data

    assert data["prediction"] in (0, 1)
    assert 0.0 <= data["spam_probability"] <= 1.0


def test_predict_rejects_missing_email(client):
    response = client.post(
        "/predict",
        json={},
    )

    assert response.status_code == 400

    data = response.get_json()

    assert "error" in data


def test_predict_rejects_empty_email(client):
    response = client.post(
        "/predict",
        json={
            "email": "   ",
        },
    )

    assert response.status_code == 400

    data = response.get_json()

    assert "error" in data


def test_predict_rejects_invalid_json(client):
    response = client.post(
        "/predict",
        data="not json",
        content_type="application/json",
    )

    assert response.status_code == 400

    data = response.get_json()

    assert "error" in data


def test_predict_rejects_email_that_is_too_long(client):
    long_email = "a" * 10_001

    response = client.post(
        "/predict",
        json={
            "email": long_email,
        },
    )

    assert response.status_code == 400

    data = response.get_json()

    assert "error" in data