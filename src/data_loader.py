import pandas as pd

COLUMNS = [
    "area", "perimetro", "compacidade", "comprimento_nucleo",
    "largura_nucleo", "coef_assimetria", "comprimento_sulco", "classe"
]


def load_data(path):
    df = pd.read_csv(path, sep=r'\s+', header=None, names=COLUMNS)
    df["classe"] = df["classe"].astype(int)
    assert df.shape == (210, 8), f"Shape inesperado: {df.shape}"
    assert set(df["classe"].unique()).issubset({1, 2, 3}), "Classes inválidas"
    return df
