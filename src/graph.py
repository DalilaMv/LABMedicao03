import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from sklearn.linear_model import LinearRegression

# Ler o arquivo CSV usando o Pandas
data = pd.read_csv('arquivo_modificado.csv')

# Variáveis x e y
x_vars = ['age', 'stargazerCount', 'releases', 'loc']
y_vars = ['status', 'num_reviews']

# Loop através de cada variável x
for x_var in x_vars:
    # Cria um subconjunto dos dados contendo todas as variáveis y
    subset = data[[x_var] + y_vars]

    # Loop através de cada variável y
    for y_var in y_vars:
        # Calcula a correlação de Spearman
        spearman_corr, spearman_pvalue = spearmanr(subset[x_var], subset[y_var])

        # Cria um gráfico de scatter plot para cada combinação de x e y
        plt.scatter(subset[x_var], subset[y_var], color='blue')

        # Adiciona um título descritivo ao gráfico
        plt.title('{} X {}'.format(x_var, y_var))

        # Adiciona labels aos eixos X e Y
        plt.xlabel(x_var)
        plt.ylabel(y_var)

        # Calcula a linha de regressão
        lr = LinearRegression()
        lr.fit(subset[[x_var]], subset[[y_var]])
        y_pred = lr.predict(subset[[x_var]])

        # Adiciona a linha de regressão ao gráfico
        plt.plot(subset[x_var], y_pred, color='red')

        # Adiciona a correlação de Spearman ao gráfico
        plt.text(subset[x_var].max()*0.8, subset[y_var].max()*0.7, f"Spearman Corr: {spearman_corr}", fontsize=12)

        # Salva o gráfico em formato PNG com um nome baseado nas variáveis x e y
        plt.savefig('_{}_vs_{}.png'.format(x_var, y_var), dpi=550, bbox_inches='tight')

        # Limpa a figura atual para que a próxima iteração do loop possa começar com uma figura vazia
        plt.clf()
