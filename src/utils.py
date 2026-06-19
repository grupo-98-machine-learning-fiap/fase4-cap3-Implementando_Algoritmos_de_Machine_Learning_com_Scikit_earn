import pandas as pd


def feature_importance(rf_model, feature_names):
    importances = rf_model.feature_importances_
    df = pd.DataFrame({"feature": feature_names, "importance": importances})
    return df.sort_values("importance", ascending=False).reset_index(drop=True)
