from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, f1_score


def optimize_svm(X_train, y_train, X_test, y_test, baseline_svm):
    baseline_acc = accuracy_score(y_test, baseline_svm.predict(X_test))
    baseline_f1 = f1_score(y_test, baseline_svm.predict(X_test), average="macro")

    param_grid = {
        "C": [0.1, 1, 10, 100],
        "kernel": ["linear", "rbf"],
    }
    grid = GridSearchCV(SVC(random_state=42), param_grid, cv=5, scoring="accuracy", n_jobs=-1)
    grid.fit(X_train, y_train)

    best_model = grid.best_estimator_
    opt_acc = accuracy_score(y_test, best_model.predict(X_test))
    opt_f1 = f1_score(y_test, best_model.predict(X_test), average="macro")

    return {
        "best_params": grid.best_params_,
        "best_cv_score": grid.best_score_,
        "baseline_accuracy": baseline_acc,
        "baseline_f1_macro": baseline_f1,
        "optimized_accuracy": opt_acc,
        "optimized_f1_macro": opt_f1,
        "best_model": best_model,
    }
