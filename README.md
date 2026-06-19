# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Classificação de Grãos de Trigo — Seeds Dataset

## Grupo

## 👨‍🎓 Integrantes:
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 1</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 2</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 3</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 4</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 5</a>

## 👩‍🏫 Professores:
### Tutor(a)
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Tutor</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Coordenador</a>


## 📜 Descrição

Projeto de Machine Learning para classificação automática de 3 variedades de grãos de trigo (**Kama**, **Rosa** e **Canadian**) a partir de 7 medidas físicas obtidas por análise de imagem, seguindo a metodologia **CRISP-DM**.

O dataset utilizado é o [Seeds Dataset](https://archive.ics.uci.edu/dataset/236/seeds) do UCI Machine Learning Repository, com 210 amostras balanceadas (70 por classe) e 7 features contínuas: área, perímetro, compacidade, comprimento do núcleo, largura do núcleo, coeficiente de assimetria e comprimento do sulco.

Três algoritmos foram treinados e comparados — **KNN**, **SVM** e **Random Forest** — com otimização de hiperparâmetros via GridSearchCV para o SVM. O **Random Forest** obteve melhor desempenho (accuracy 92,1%, F1 macro 91,9%), demonstrando viabilidade para uso em cooperativas agrícolas de pequeno porte.


## 📁 Estrutura de pastas

```
fase4-cap3-/
├── assets/                         # Imagens, relatórios e recursos visuais
│   ├── logo-fiap.png
│   ├── histograms.png
│   ├── boxplots.png
│   ├── correlation.png
│   ├── pairplot.png
│   ├── feature_importance.png
│   ├── results.md                  # Relatório de resultados
│   └── audit_report.md             # Relatório de auditoria
├── config/                         # Arquivos de configuração
├── document/
│   └── ai_project_document_fiap.md # Documento do projeto FIAP
├── notebooks/
│   └── seeds_classification.ipynb  # Notebook principal (executa todo o pipeline)
├── scripts/                        # Scripts auxiliares
├── src/
│   ├── data/
│   │   └── seeds_dataset.txt       # Dataset bruto (210 amostras)
│   ├── data_loader.py              # Carregamento e validação do dataset
│   ├── preprocessing.py            # Extração de X, y
│   ├── visualization.py            # Geração de gráficos exploratórios
│   ├── train_models.py             # Treinamento de KNN, SVM, Random Forest
│   ├── evaluate.py                 # Métricas e tabela comparativa
│   ├── optimize.py                 # Otimização do SVM com GridSearchCV
│   └── utils.py                    # Feature importance
├── requirements.txt
└── README.md
```


## 🔧 Como executar o código

### Pré-requisitos

- Python 3.10 ou superior

### Instalação

```bash
pip install -r requirements.txt
```

### Abrir o Notebook

```bash
jupyter notebook notebooks/seeds_classification.ipynb
```

O notebook executa todas as etapas do pipeline CRISP-DM de forma sequencial. Basta rodar **Kernel → Restart & Run All**.

Os gráficos gerados são salvos automaticamente em `assets/`.

### Resultados

| Modelo | Accuracy | F1 (macro) |
|---|---|---|
| KNN | 87,3% | 87,1% |
| SVM (padrão) | 87,3% | 87,1% |
| **Random Forest** | **92,1%** | **91,9%** |
| SVM (otimizado) | 88,9% | 88,8% |

Relatório completo: [`assets/results.md`](assets/results.md)


## 🗃 Histórico de lançamentos

* 1.0.0 - 19/06/2026
    * Pipeline completo: carregamento, EDA, pré-processamento, treinamento, avaliação e otimização
    * Correção de data leakage no StandardScaler (fit apenas em X_train)
    * Notebook executado e validado


## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
