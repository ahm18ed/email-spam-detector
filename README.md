````markdown
# MailGuard

A machine-learning-powered email spam detector built with Python, scikit-learn, and Flask.

MailGuard analyzes the text of an email and predicts whether it is likely to be **spam** or **legitimate**, while also providing a spam probability through a clean web interface.

---

## Overview

MailGuard combines a traditional machine-learning text classification pipeline with a lightweight Flask web application.

The application takes an email as input, cleans and transforms the text, passes it through a trained machine-learning model, and returns the predicted class along with the estimated probability of spam.

### Prediction Pipeline

```text
Email Text
    │
    ▼
Text Preprocessing
    │
    ▼
TF-IDF Feature Extraction
    │
    ▼
Multinomial Naive Bayes
    │
    ▼
Prediction + Spam Probability
    │
    ▼
Flask Web Interface
````

---

## Features

* Email spam classification using machine learning
* Text preprocessing and normalization
* TF-IDF feature extraction
* Multinomial Naive Bayes classifier
* Spam probability estimation
* Flask-based web application
* Responsive and minimal user interface
* Client-side and server-side input validation
* Saved model and vectorizer for inference
* Automated prediction tests
* API endpoint for email classification

---

## Machine Learning

### Dataset

The dataset used by MailGuard contains:

* **5,695 emails**
* **4,327 legitimate emails**
* **1,368 spam emails**

Class distribution:

| Class      |     Count | Approx. Percentage |
| ---------- | --------: | -----------------: |
| Legitimate |     4,327 |                76% |
| Spam       |     1,368 |                24% |
| **Total**  | **5,695** |           **100%** |

The dataset is therefore imbalanced, with legitimate emails representing the majority class.

Because of this imbalance, MailGuard evaluates the model using **precision, recall, and F1-score** in addition to accuracy.

---

## Text Preprocessing

Before classification, email text is cleaned using a preprocessing function.

The preprocessing pipeline:

1. Converts text to lowercase
2. Removes HTML tags
3. Removes URLs
4. Removes email addresses
5. Removes unnecessary special characters
6. Normalizes whitespace

Example:

```text
Original:
"Congratulations!!! Visit https://example.com NOW!!!"

After preprocessing:
"congratulations visit now"
```

The project intentionally keeps preprocessing relatively conservative rather than aggressively removing stopwords or applying stemming or lemmatization.

---

## Feature Extraction

MailGuard uses **TF-IDF (Term Frequency-Inverse Document Frequency)** to convert email text into numerical features.

TF-IDF gives greater importance to terms that are useful for distinguishing documents while reducing the importance of terms that appear frequently across the dataset.

The vectorizer is fitted on the training data and reused during prediction.

The trained vectorizer is stored as:

```text
models/tfidf_vectorizer.pkl
```

---

## Classification Model

MailGuard uses the **Multinomial Naive Bayes** algorithm.

Naive Bayes is well suited to text classification problems because it works efficiently with high-dimensional text features such as TF-IDF.

The trained classifier is stored as:

```text
models/spam_classifier.pkl
```

### Hyperparameter Selection

Several values of the Naive Bayes smoothing parameter `alpha` were evaluated.

A 5-fold cross-validation experiment was performed using F1-score for model selection.

The best observed cross-validation result was:

```text
alpha = 0.02
mean F1-score = 0.9821
```

The model-selection process was based on the training data rather than repeatedly tuning against the final test set.

---

## Model Evaluation

MailGuard evaluates classification performance using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion matrix
* Classification report

### Why F1-score matters

Because the dataset contains considerably more legitimate emails than spam emails, accuracy alone can be misleading.

For example, a model could achieve high accuracy by predicting most emails as legitimate while still missing a large number of spam messages.

F1-score provides a balance between:

* **Precision** — how many emails predicted as spam are actually spam
* **Recall** — how many actual spam emails are successfully detected

For a spam detector, recall is especially important because false negatives represent spam messages that the system failed to detect.

---

## Web Application

MailGuard provides a browser-based interface built with:

* HTML
* CSS
* JavaScript
* Flask

The interface allows a user to:

1. Paste or type an email
2. Submit it for analysis
3. View the prediction
4. View the estimated spam probability
5. Analyze another email

The interface is intentionally designed around a calm, minimal visual style rather than using excessive gradients, animations, or decorative AI-themed elements.

---

## API

MailGuard exposes a prediction endpoint:

```text
POST /predict
```

### Request

Send a JSON object containing the email text:

```json
{
    "email": "Congratulations! You have won a free prize!"
}
```

### Response

Example:

```json
{
    "prediction": 1,
    "spam_probability": 0.69
}
```

Where:

```text
0 = Legitimate
1 = Spam
```

The `spam_probability` value is returned as a number between `0` and `1`.

For example:

```text
0.69 = 69%
```

---

## Example API Request

Using `curl`:

```bash
curl -X POST http://127.0.0.1:5000/predict \
    -H "Content-Type: application/json" \
    -d '{"email":"Congratulations! You won a free prize!"}'
```

Example response:

```json
{
    "prediction": 1,
    "spam_probability": 0.69
}
```

The exact probability depends on the trained model and input text.

---

## Project Structure

```text
email-spam-detector/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── app.js
│   │
│   └── templates/
│       └── index.html
│
├── data/
│   └── dataset.csv
│
├── models/
│   ├── README.md
│   ├── spam_classifier.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebooks/
│   └── exploration.ipynb
│
├── src/
│   ├── evaluation/
│   │   └── metrics.py
│   │
│   ├── features/
│   │   ├── extraction.py
│   │   └── __init__.py
│   │
│   ├── model/
│   │   ├── classifier.py
│   │   ├── predictor.py
│   │   └── __init__.py
│   │
│   └── preprocessing/
│       ├── cleaning.py
│       └── __init__.py
│
├── tests/
│   └── test_predictor.py
│
├── .gitignore
├── LICENSE
├── main.py
├── pyproject.toml
├── README.md
├── requirements.txt
└── uv.lock
```

---

## Technologies

### Programming Language

* Python

### Machine Learning

* scikit-learn
* pandas
* NumPy

### Web Application

* Flask
* HTML
* CSS
* JavaScript

### Model Serialization

* joblib

### Environment and Dependency Management

* uv

### Development and Testing

* pytest
* Jupyter Notebook

---

## Installation

### Prerequisites

Make sure Python and `uv` are installed on your system.

Verify the installations:

```bash
python --version
uv --version
```

---

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd email-spam-detector
```

Replace `<YOUR_REPOSITORY_URL>` with the URL of your GitHub repository.

---

### 2. Install Dependencies

This project uses `uv` for dependency management.

Run:

```bash
uv sync
```

This creates the project environment and installs the required dependencies.

---

## Running the Application

Start the Flask application:

```bash
uv run python main.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

Open that address in your browser.

---

## Running in Development Mode

For Flask debug mode on Linux or macOS:

```bash
FLASK_DEBUG=1 uv run python main.py
```

Debug mode should only be used during development.

---

## Running Tests

Run the test suite with:

```bash
uv run pytest
```

The tests verify that the prediction pipeline returns:

* A valid prediction class
* A valid probability between `0` and `1`

---

## Notebook

The machine-learning experimentation and exploratory analysis are documented in:

```text
notebooks/exploration.ipynb
```

The notebook contains the development process used to explore:

* Dataset structure
* Missing values
* Duplicate records
* Class distribution
* Email length
* Text preprocessing
* TF-IDF features
* Model training
* Model evaluation
* N-gram experimentation
* Hyperparameter tuning
* Cross-validation

---

## Model Artifacts

The trained model files are stored in the `models/` directory.

### `spam_classifier.pkl`

Serialized Multinomial Naive Bayes classifier.

### `tfidf_vectorizer.pkl`

Serialized TF-IDF vectorizer fitted on the training data.

Both files are required for the Flask application to perform predictions.

---

## Security and Privacy Considerations

MailGuard is an educational machine-learning project and should not be treated as a complete email security solution.

The current application analyzes email text supplied directly by the user and does not connect to external email services.

The model may produce incorrect predictions, including:

* False positives — legitimate emails classified as spam
* False negatives — spam emails classified as legitimate

A machine-learning prediction should therefore not be considered a definitive security verdict.

For production use, additional security controls and detection techniques would be required.

---

## Limitations

MailGuard currently has several limitations:

* The model only considers the text supplied to it
* Email headers are not analyzed
* Attachments are not analyzed
* Sender reputation is not considered
* URLs are removed during preprocessing rather than analyzed for malicious characteristics
* Adversarial or heavily obfuscated spam may reduce model performance
* The model is trained on a fixed dataset and is not automatically retrained
* Predictions depend on patterns learned from the training dataset

These limitations provide opportunities for future development.

---

## Future Improvements

Potential improvements include:

* Experimenting with additional classifiers
* Automated hyperparameter optimization
* Larger and more diverse datasets
* Header and sender analysis
* URL reputation analysis
* Attachment analysis
* Character-level features
* Better detection of obfuscated spam
* Configurable classification thresholds
* Automated model retraining
* Model versioning
* Production deployment
* Authentication and rate limiting for the API
* More comprehensive test coverage

---

## Development Workflow

The project was developed in stages:

```text
1. Dataset exploration
2. Data cleaning
3. Exploratory data analysis
4. Text preprocessing
5. TF-IDF feature extraction
6. Model training
7. Model evaluation
8. Hyperparameter tuning
9. Model serialization
10. Flask API
11. Web interface
12. UI polishing
13. Testing and documentation
```

---

## Example

An email such as:

```text
Congratulations!

You have been selected to receive a FREE prize.

Click now to claim your reward!
```

may produce:

```text
Prediction: Spam
Spam probability: High
```

While an ordinary message such as:

```text
Hi,

Just checking in about our meeting tomorrow.
Please let me know what time works for you.

Thanks.
```

may produce:

```text
Prediction: Legitimate
Spam probability: Low
```

The output is a machine-learning prediction and is not guaranteed to be correct.

---

## License

This project is licensed under the MIT License.

Copyright (c) 2026 Ahmed Hussein

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

````



