import pandas as pd
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    return {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision_macro": precision_score(y_test, y_pred, average="macro", zero_division=0),
        "recall_macro": recall_score(y_test, y_pred, average="macro", zero_division=0),
        "f1_macro": f1_score(y_test, y_pred, average="macro", zero_division=0),
        "f1_weighted": f1_score(y_test, y_pred, average="weighted", zero_division=0),
        "confusion_matrix": confusion_matrix(y_test, y_pred),
        "classification_report": classification_report(y_test, y_pred, target_names=["Kama", "Rosa", "Canadian"]),
        "y_pred": y_pred,
    }


def compare_models(models, X_test, y_test):
    rows = []
    for name, model in models.items():
        metrics = evaluate_model(model, X_test, y_test)
        rows.append({
            "Modelo": name,
            "Accuracy": round(metrics["accuracy"], 4),
            "Precision (macro)": round(metrics["precision_macro"], 4),
            "Recall (macro)": round(metrics["recall_macro"], 4),
            "F1 (macro)": round(metrics["f1_macro"], 4),
            "F1 (weighted)": round(metrics["f1_weighted"], 4),
        })
    return pd.DataFrame(rows).set_index("Modelo")
