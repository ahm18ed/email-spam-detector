from src.model.predictor import predict_email

email = input("Enter an email to classify: \n\n")

prediction, probability = predict_email(email)

if prediction == 1:
    print("Spam")
else:
    print("Ham")

print(f"Spam probability: {probability:.2f}")

