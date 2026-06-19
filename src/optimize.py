import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

from evaluate import evaluate_model

# Grade de hiperparâmetros por modelo
PARAM_GRIDS = {
    "KNN": (
        KNeighborsClassifier(),
        {
            "n_neighbors": [3, 5, 7, 9, 11],
            "weights": ["uniform", "distance"],
            "metric": ["euclidean", "manhattan", "minkowski"],
        },
    ),
    "SVM": (
        SVC(random_state=42),
        {
            "C": [0.1, 1, 10, 100],
            "kernel": ["linear", "rbf"],
            "gamma": ["scale", "auto"],
        },
    ),
    "Random Forest": (
        RandomForestClassifier(random_state=42),
        {
            "n_estimators": [100, 200, 300],
            "max_depth": [None, 5, 10, 20],
            "min_samples_split": [2, 5, 10],
            "max_features": ["sqrt", "log2"],
        },
    ),
}


def optimize_model(name, X_train, y_train, X_test, y_test, baseline_model):
    """Otimiza um único modelo via GridSearchCV e devolve avaliação completa
    (accuracy, precisão, recall, F1 e matriz de confusão) para baseline e otimizado."""
    estimator, param_grid = PARAM_GRIDS[name]

    grid = GridSearchCV(estimator, param_grid, cv=5, scoring="accuracy", n_jobs=-1)
    grid.fit(X_train, y_train)
    best_model = grid.best_estimator_

    baseline_metrics = evaluate_model(baseline_model, X_test, y_test)
    optimized_metrics = evaluate_model(best_model, X_test, y_test)

    return {
        "name": name,
        "best_params": grid.best_params_,
        "best_cv_score": grid.best_score_,
        "best_model": best_model,
        "baseline_metrics": baseline_metrics,
        "optimized_metrics": optimized_metrics,
    }


def optimize_all(models, X_train, y_train, X_test, y_test):
    """Otimiza todos os modelos do dicionário `models`."""
    return {name: optimize_model(name, X_train, y_train, X_test, y_test, model)
            for name, model in models.items()}


def optimization_summary(results):
    """Tabela comparativa baseline x otimizado para todos os modelos."""
    rows = []
    for name, r in results.items():
        b, o = r["baseline_metrics"], r["optimized_metrics"]
        rows.append({
            "Modelo": name,
            "Acc (baseline)": round(b["accuracy"], 4),
            "Acc (otimizado)": round(o["accuracy"], 4),
            "F1 macro (baseline)": round(b["f1_macro"], 4),
            "F1 macro (otimizado)": round(o["f1_macro"], 4),
            "Ganho Acc": round(o["accuracy"] - b["accuracy"], 4),
        })
    return pd.DataFrame(rows).set_index("Modelo")
