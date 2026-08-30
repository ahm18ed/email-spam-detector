from flask import Flask, jsonify, render_template, request

from src.model.predictor import predict_email

def register_routes(app: Flask) -> None:


    @app.get("/")
    def home():
        return render_template("index.html")
    
    @app.post("/predict")
    def predict():
        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                "error": "Request body must be JSON."
            }), 400

        email = data.get("email")

        if not isinstance(email, str) or not email.strip():
            return jsonify({
                "error" : "The 'email' field is required."
            }), 400

        try:
            prediction, spam_probability = predict_email(email)

            return jsonify({
                "prediction": int(prediction),
                "spam_probability": float(spam_probability)
            })
        except Exception:
            return jsonify({
                "error": "Unable to analyze the email"
            }), 500