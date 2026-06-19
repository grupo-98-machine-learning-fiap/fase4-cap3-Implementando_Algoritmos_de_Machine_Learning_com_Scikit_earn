# Relatório de Auditoria

**Data:** 2026-06-19
**Auditor:** Claude Code (claude-sonnet-4-6)
**Projeto:** Classificação de Grãos de Trigo — Seeds Dataset

---

## Resumo

**APROVADO** — Todos os problemas identificados na auditoria inicial foram corrigidos. O projeto está estruturalmente completo, o notebook executa do início ao fim sem erros, e os números reportados são reproduzíveis.

---

## Checklist de Completude

| Item | Status | Observação |
|---|---|---|
| `src/data/seeds_dataset.txt` | OK | 210 linhas, sem cabeçalho, separador tab |
| `notebooks/seeds_classification.ipynb` | OK | Executado, todas as células têm output |
| `src/data_loader.py` | OK | Presente e não vazio |
| `src/preprocessing.py` | OK | Corrigido — sem data leakage |
| `src/visualization.py` | OK | Presente e não vazio |
| `src/train_models.py` | OK | Presente e não vazio |
| `src/evaluate.py` | OK | Presente e não vazio |
| `src/optimize.py` | OK | Presente e não vazio |
| `src/utils.py` | OK | Presente e não vazio |
| `assets/histograms.png` | OK | Arquivo existe |
| `assets/boxplots.png` | OK | Arquivo existe |
| `assets/correlation.png` | OK | Arquivo existe |
| `assets/pairplot.png` | OK | Arquivo existe |
| `assets/feature_importance.png` | OK | Arquivo existe |
| `assets/results.md` | OK | Números corretos e verificados |
| `requirements.txt` | OK | Cobre todas as dependências importadas |
| `README.md` | OK | Preenchido com instruções de instalação e execução |

---

## Problemas Encontrados na Auditoria Inicial e Correções Aplicadas

### CRÍTICO — Corrigido

**[C1] Data leakage — `src/preprocessing.py`**

`StandardScaler` era ajustado com `fit_transform(X)` no dataset completo (210 amostras) antes do train/test split.

**Correção:** `preprocessing.py` agora retorna apenas `X, y` sem scaling. O `StandardScaler` é instanciado no notebook após o split: `scaler.fit_transform(X_train)` + `scaler.transform(X_test)`.

---

### MÉDIO — Corrigido

**[M1] Score CV errado — `assets/results.md`**

Score CV reportado como `~0.90`; valor real era `0.9731`.

**Correção:** Valor corrigido para `0.9731`.

**[M2] F1 macro SVM otimizado — `assets/results.md`**

F1 macro reportado como `0.8877`; valor real era `0.8875`.

**Correção:** Valor corrigido para `0.8875`.

---

### BAIXO — Corrigido

**[B1] `SVC(random_state=42)` sem efeito — `src/train_models.py`**

`random_state` em SVC só tem efeito com `probability=True`.

**Correção:** Parâmetro removido. SVC agora é instanciado como `SVC()`.

---

## Data Leakage

**Não há vazamento de dados.** Verificação pós-correção:

| Ponto de verificação | Resultado |
|---|---|
| `StandardScaler.fit` apenas em `X_train` | OK — `scaler.fit_transform(X_train)` no notebook após o split |
| `train_test_split` com `random_state=42` | OK |
| `train_test_split` com `stratify=y` | OK |
| `GridSearchCV.fit` apenas em `X_train` | OK — `grid.fit(X_train, y_train)` em `optimize.py` |
| `X_test` usado apenas na avaliação final | OK |

---

## Recomendações

Nenhuma pendência. O projeto está pronto para uso.
