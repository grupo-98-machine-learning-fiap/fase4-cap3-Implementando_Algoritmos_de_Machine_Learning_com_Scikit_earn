def preprocess(df):
    feature_cols = [c for c in df.columns if c != "classe"]
    X = df[feature_cols].values
    y = df["classe"].values
    return X, y
