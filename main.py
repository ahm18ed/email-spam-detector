from src.model.predictor import predict_email

print("Enter the email text.")
print("Press Ctrl+D when finished.\n")

email = input()

prediction, probability = predict_email(email)

if prediction == 1:
    print("Spam")
else:
    print("Ham")

print(f"Spam probability: {probability:.2f}")

