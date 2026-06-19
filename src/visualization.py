import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import os

FEATURE_COLS = [
    "area", "perimetro", "compacidade", "comprimento_nucleo",
    "largura_nucleo", "coef_assimetria", "comprimento_sulco"
]
CLASS_NAMES = {1: "Kama", 2: "Rosa", 3: "Canadian"}


def save_histograms(df, output_dir):
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    axes = axes.flatten()
    for i, col in enumerate(FEATURE_COLS):
        axes[i].hist(df[col], bins=20, edgecolor="black")
        axes[i].set_title(col)
    axes[-1].axis("off")
    plt.tight_layout()
    path = os.path.join(output_dir, "histograms.png")
    plt.savefig(path, dpi=100)
    plt.close()
    return path


def save_boxplots(df, output_dir):
    df2 = df.copy()
    df2["classe_nome"] = df2["classe"].map(CLASS_NAMES)
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    axes = axes.flatten()
    for i, col in enumerate(FEATURE_COLS):
        sns.boxplot(data=df2, x="classe_nome", y=col, ax=axes[i])
        axes[i].set_title(col)
        axes[i].set_xlabel("")
    axes[-1].axis("off")
    plt.tight_layout()
    path = os.path.join(output_dir, "boxplots.png")
    plt.savefig(path, dpi=100)
    plt.close()
    return path


def save_correlation(df, output_dir):
    corr = df[FEATURE_COLS].corr()
    fig, ax = plt.subplots(figsize=(9, 7))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    ax.set_title("Matriz de Correlação")
    plt.tight_layout()
    path = os.path.join(output_dir, "correlation.png")
    plt.savefig(path, dpi=100)
    plt.close()
    return path


def save_pairplot(df, output_dir):
    df2 = df.copy()
    df2["classe_nome"] = df2["classe"].map(CLASS_NAMES)
    g = sns.pairplot(df2, vars=FEATURE_COLS, hue="classe_nome", diag_kind="kde", plot_kws={"alpha": 0.6})
    g.fig.suptitle("Pairplot por Classe", y=1.02)
    path = os.path.join(output_dir, "pairplot.png")
    g.savefig(path, dpi=80)
    plt.close()
    return path
