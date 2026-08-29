from sklearn.metrics import(
    accuracy_score,
    recall_score,
    f1_score,
    precision_score,
    confusion_matrix,
    classification_report
)

def evaluate_model(y_true, y_pred):
    matrix =  {
        "Accuracy": accuracy_score(y_true, y_pred),
        "Recall": recall_score(y_true,y_pred),
        "F1": f1_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred),
    }
    return matrix

def get_classification_report(y_true, y_pred):
    return classification_report(
        y_true,
        y_pred,
        target_names= ["Ham", "Spam"]
    )


def get_confusion_matrix(y_true, y_pred):
    return confusion_matrix(y_true, y_pred)
