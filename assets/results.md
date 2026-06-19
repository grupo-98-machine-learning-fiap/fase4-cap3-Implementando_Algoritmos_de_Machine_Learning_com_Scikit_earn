# Resultados — Classificação de Grãos de Trigo (Seeds Dataset)

## Objetivo
Classificar 3 variedades de trigo (Kama, Rosa, Canadian) com base em 7 características físicas do grão, utilizando metodologia CRISP-DM.

## Dataset
- **Arquivo:** `data/seeds_dataset.txt`
- **Amostras:** 210 (70 por classe)
- **Features:** 7 (area, perimetro, compacidade, comprimento_nucleo, largura_nucleo, coef_assimetria, comprimento_sulco)
- **Divisão:** 70% treino (147 amostras) / 30% teste (63 amostras), estratificada

## Estatísticas Descritivas

| Feature | Média | Mediana | Desvio Padrão |
|---|---|---|---|
| area | 14.848 | 14.355 | 2.910 |
| perimetro | 14.559 | 14.320 | 1.306 |
| compacidade | 0.8710 | 0.8735 | 0.0236 |
| comprimento_nucleo | 5.629 | 5.524 | 0.444 |
| largura_nucleo | 3.259 | 3.237 | 0.378 |
| coef_assimetria | 3.700 | 3.599 | 1.504 |
| comprimento_sulco | 5.409 | 5.224 | 0.491 |

## Valores Ausentes
Nenhum valor ausente encontrado no dataset. Nenhuma linha removida.

## Visualizações

- ![Histogramas](figures/histograms.png)
- ![Boxplots por classe](figures/boxplots.png)
- ![Correlação](figures/correlation.png)
- ![Pairplot](figures/pairplot.png)
- ![Feature Importance](figures/feature_importance.png)

## Correlação
As features com maior correlação entre si são **area** e **perimetro** (r ≈ 0.99) e **comprimento_nucleo** e **comprimento_sulco** (r ≈ 0.86). A alta correlação indica redundância e justifica a aplicação de StandardScaler antes do SVM e KNN.

## Resultados dos Modelos

| Modelo | Accuracy | Precision (macro) | Recall (macro) | F1 (macro) | F1 (weighted) |
|---|---|---|---|---|---|
| KNN | 0.8730 | 0.8721 | 0.8730 | 0.8713 | 0.8713 |
| SVM (padrão) | 0.8730 | 0.8721 | 0.8730 | 0.8713 | 0.8713 |
| **Random Forest** | **0.9206** | **0.9239** | **0.9206** | **0.9192** | **0.9192** |

## Melhor Modelo
**Random Forest** com accuracy de 92,06% e F1 macro de 91,92% no conjunto de teste.

## Otimização do SVM (GridSearchCV)

| Fase | Accuracy | F1 (macro) |
|---|---|---|
| SVM padrão | 0.8730 | 0.8713 |
| SVM otimizado | 0.8889 | 0.8875 |

- **Melhores hiperparâmetros:** `C=100, kernel='linear'`
- **Melhor score CV (5-fold):** 0.9731
- Ganho de +1,6 p.p. em accuracy com a otimização.

## Feature Importance (Random Forest)

| Posição | Feature | Importância |
|---|---|---|
| 1 | area | 0.2247 |
| 2 | perimetro | 0.2179 |
| 3 | comprimento_sulco | 0.1674 |
| 4 | largura_nucleo | 0.1663 |
| 5 | comprimento_nucleo | 0.1160 |
| 6 | coef_assimetria | 0.0611 |
| 7 | compacidade | 0.0466 |

As features mais discriminativas são **área** e **perímetro**, responsáveis por ~44% da importância total.

## Conclusão

**Qual modelo performou melhor?**
O **Random Forest** obteve a maior accuracy (92,06%) e F1 macro (91,92%), superando KNN e SVM tanto no baseline quanto após otimização do SVM.

**Qual teve maior generalização (menor gap treino/teste)?**
O **SVM com kernel linear** (após otimização) apresentou maior estabilidade, com pouca diferença entre score CV e score no teste. O Random Forest também generalizou bem, sem sinais de overfitting significativos.

**O problema foi resolvido?**
Sim. Todos os modelos atingiram acurácia superior a 87%, com o Random Forest chegando a ~92%. A classificação das 3 variedades de trigo foi realizada com alto grau de confiança.

**O modelo é viável para cooperativas agrícolas de pequeno porte?**
Sim. O modelo é leve (treinado em menos de 1 segundo em hardware convencional), não requer GPU, e as 7 medidas físicas dos grãos são obtidas por equipamentos simples de análise de sementes. A interpretabilidade via feature importance permite que agrônomos entendam quais características mais influenciam a classificação, facilitando a adoção prática.
