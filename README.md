# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto

## 98

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/eduardo-venancio/">Eduardo Venancio Leite</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Francisco José Bittencourt Corrêa</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Jullyana de Azevedo Rodrigues</a> 
- <a href="https://www.linkedin.com/in/kaiquecadimiel/">Kaique Cadimiel Amasio de Souza</a> 
- <a href="https://www.linkedin.com/in/lucas-paiva-02ab522a9/">Lucas Paiva de Oliveira</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Nicolly Candida Rodrigues de Souza</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">ANDRÉ GODOI CHIOVATO</a>


## 📜 Descrição

*Descreva seu projeto com base no texto do PBL (até 600 palavras)*


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

*Acrescentar as informações necessárias sobre pré-requisitos (IDEs, serviços, bibliotecas etc.) e instalação básica do projeto, descrevendo eventuais versões utilizadas. Colocar um passo a passo de como o leitor pode baixar o seu código e executá-lo a partir de sua máquina ou seu repositório. Considere a explicação organizada em fase.*


## 🗃 Histórico de lançamentos

* 0.5.0 - XX/XX/2024
    * 
* 0.4.0 - XX/XX/2024
    * 
* 0.3.0 - XX/XX/2024
    * 
* 0.2.0 - XX/XX/2024
    * 
* 0.1.0 - XX/XX/2024
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

# Classificação de Grãos de Trigo — Seeds Dataset

> Projeto completo de Machine Learning seguindo a metodologia **CRISP-DM** para classificar automaticamente 3 variedades de trigo com base em características físicas dos grãos.

---

## Sobre o Projeto

Este projeto tem como objetivo identificar a variedade de um grão de trigo (**Kama**, **Rosa** ou **Canadian**) a partir de 7 medidas físicas obtidas por análise de imagem. O problema é tratado como uma **classificação multiclasse supervisionada**.

A metodologia adotada é o **CRISP-DM** (Cross-Industry Standard Process for Data Mining), que organiza o trabalho em ciclos iterativos:

1. Entendimento do negócio
2. Entendimento dos dados
3. Preparação dos dados
4. Modelagem
5. Avaliação
6. Implantação

---

## Dataset

- **Fonte:** UCI Machine Learning Repository — Seeds Dataset
- **Amostras:** 210 grãos de trigo
- **Classes:** 3 variedades balanceadas (70 amostras cada)
  - `1` → Kama
  - `2` → Rosa
  - `3` → Canadian
- **Features (7 características físicas):**

| Feature | Descrição |
|---|---|
| `area` | Área do grão |
| `perimetro` | Perímetro do grão |
| `compacidade` | Compacidade (4π × área / perímetro²) |
| `comprimento_nucleo` | Comprimento do núcleo |
| `largura_nucleo` | Largura do núcleo |
| `coef_assimetria` | Coeficiente de assimetria |
| `comprimento_sulco` | Comprimento do sulco do grão |

---

## Estrutura do Projeto

```
project/
├── data/
│   └── seeds_dataset.txt           # Dataset bruto (210 amostras, sem header)
├── notebooks/
│   └── seeds_classification.ipynb  # Notebook principal — executa todas as etapas
├── src/
│   ├── data_loader.py              # Carrega e valida o dataset
│   ├── preprocessing.py            # Padronização com StandardScaler
│   ├── visualization.py            # Geração de gráficos exploratórios
│   ├── train_models.py             # Treinamento de KNN, SVM e Random Forest
│   ├── evaluate.py                 # Métricas e tabela comparativa
│   ├── optimize.py                 # Otimização de KNN, SVM e RF com GridSearchCV
│   └── utils.py                    # Feature importance
├── reports/
│   ├── figures/                    # Gráficos salvos automaticamente
│   │   ├── histograms.png
│   │   ├── boxplots.png
│   │   ├── correlation.png
│   │   ├── pairplot.png
│   │   └── feature_importance.png
│   └── results.md                  # Relatório completo com conclusões
├── requirements.txt
└── README.md
```

---

## Etapas do Pipeline (CRISP-DM)

### 1. Carregamento dos Dados (`src/data_loader.py`)
Lê o arquivo `seeds_dataset.txt` com separador de espaço/tab variável, aplica os nomes de coluna e valida que o shape é (210, 8) e as classes estão no conjunto {1, 2, 3}.

### 2. Entendimento dos Dados
Análise estatística descritiva: shape, tipos, `.describe()`, média, mediana e desvio padrão por feature.

### 3. Valores Ausentes
Verificação via `df.isnull().sum()`. O dataset não possui valores ausentes — nenhuma linha foi removida.

### 4. Visualizações Exploratórias (`src/visualization.py`)
Quatro gráficos gerados e salvos em `reports/figures/`:
- **Histogramas** — distribuição de cada feature
- **Boxplots** — distribuição por classe (Kama / Rosa / Canadian)
- **Heatmap de correlação** — correlações entre features (area e perimetro têm r ≈ 0.99)
- **Pairplot** — relação entre pares de features colorida por classe

### 5. Pré-processamento (`src/preprocessing.py`)
- Separação de `X` (7 features) e `y` (classe)
- Padronização com `StandardScaler` (média 0, desvio padrão 1)
- Necessário especialmente para KNN e SVM, que são sensíveis à escala

### 6. Divisão Treino/Teste
- **70% treino** (147 amostras) / **30% teste** (63 amostras)
- `random_state=42`, `stratify=y` para manter proporção de classes

### 7. Treinamento dos Modelos (`src/train_models.py`)
Três algoritmos treinados no conjunto de treino:
- **KNN** — K-Nearest Neighbors
- **SVM** — Support Vector Machine (kernel RBF por padrão)
- **Random Forest** — ensemble de árvores de decisão (`random_state=42`)

### 8. Avaliação (`src/evaluate.py`)
Para cada modelo no conjunto de teste:
- Accuracy, Precision, Recall, F1-score (macro e weighted)
- Matriz de confusão e relatório de classificação por classe

### 9. Otimização dos Modelos (`src/optimize.py`)
`GridSearchCV` com validação cruzada de 5 folds para **os três modelos**, com reavaliação completa (accuracy, precisão, recall, F1 e matriz de confusão):
- **KNN:** `n_neighbors`, `weights`, `metric` → melhor: `n_neighbors=3, weights=uniform, metric=manhattan`
- **SVM:** `C`, `kernel`, `gamma` → melhor: `C=100, kernel=linear, gamma=scale`
- **Random Forest:** `n_estimators`, `max_depth`, `min_samples_split`, `max_features` → melhor: `n_estimators=300, max_depth=None, max_features=sqrt, min_samples_split=2`

KNN e SVM ganharam +1,6 p.p. de accuracy; o Random Forest manteve seu desempenho de baseline (já era o melhor).

### 10. Feature Importance (`src/utils.py`)
Importância das features extraída do Random Forest, ordenada de forma decrescente. As features `area` e `perimetro` respondem por ~44% da importância total.

---

## Resultados

| Modelo | Accuracy | Precision (macro) | Recall (macro) | F1 (macro) |
|---|---|---|---|---|
| KNN (padrão) | 87,3% | 87,2% | 87,3% | 87,1% |
| KNN (otimizado) | 88,9% | 88,8% | 88,9% | 88,8% |
| SVM (padrão) | 87,3% | 87,2% | 87,3% | 87,1% |
| SVM (otimizado) | 88,9% | 89,1% | 88,9% | 88,8% |
| **Random Forest** | **92,1%** | **92,4%** | **92,1%** | **91,9%** |

**Melhor modelo:** Random Forest com **92,1% de accuracy**.

### Feature Importance (Random Forest)

| Posição | Feature | Importância |
|---|---|---|
| 1 | area | 22,5% |
| 2 | perimetro | 21,8% |
| 3 | comprimento_sulco | 16,7% |
| 4 | largura_nucleo | 16,6% |
| 5 | comprimento_nucleo | 11,6% |
| 6 | coef_assimetria | 6,1% |
| 7 | compacidade | 4,7% |

---

## Como Executar

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

O notebook cobre todas as etapas (1–10) de forma sequencial, com células de código e explicações em markdown. Basta executar **Kernel → Restart & Run All**.

---

## Dependências

```
pandas>=2.0
numpy>=1.24
matplotlib>=3.7
seaborn>=0.12
scikit-learn>=1.3
jupyter>=1.0
nbformat>=5.9
nbconvert>=7.7
```

---

## Conclusão

O **Random Forest** foi o modelo de melhor desempenho (accuracy 92,1%), com boa generalização e sem sinais de overfitting. O modelo é **viável para uso em cooperativas agrícolas de pequeno porte**: as 7 medidas físicas são obtidas por equipamentos simples de análise de sementes, o treinamento ocorre em menos de 1 segundo em hardware convencional, e a interpretabilidade via feature importance permite que agrônomos entendam o processo de classificação.

Veja o relatório detalhado em [`reports/results.md`](reports/results.md).

