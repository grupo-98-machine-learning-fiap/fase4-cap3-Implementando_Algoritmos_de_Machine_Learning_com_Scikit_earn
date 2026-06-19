from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier


def train_all(X_train, y_train):
    models = {
        "KNN": KNeighborsClassifier(),
        "SVM": SVC(),
        "Random Forest": RandomForestClassifier(random_state=42),
    }
    for name, model in models.items():
        model.fit(X_train, y_train)
    return models
