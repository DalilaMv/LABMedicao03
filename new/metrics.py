import statistics
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from sklearn.linear_model import LinearRegression


def separar_csv():
    df = pd.read_csv('resultado_final.csv', on_bad_lines='skip')

    merged_df = df[df['state'] == 'MERGED']

    merged_df.to_csv('prs_merged.csv', index=False)

    closed_df = df[df['state'] == 'CLOSED']

    closed_df.to_csv('prs_closed.csv', index=False)

def graficosScatterPlot():

    df_resultadosFinais = pd.read_csv('resultado_final.csv')
    # Variáveis x e y
    x_vars = ['num_arquivos', 'num_additions', 'num_deletions']
    y_var = ['num_reviews']

    # Loop através de cada variável x
    for x_var in x_vars:
        # Cria um subconjunto dos dados contendo todas as variáveis y
        subset = df_resultadosFinais[[x_var] + y_var]

        # Calcula a correlação de Spearman
        spearman_corr, spearman_pvalue = spearmanr(subset[x_var], subset[y_var[0]])

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
        plt.text(subset[x_var].max() * 0.8, subset[y_var].max() * 0.7, f"Spearman Corr: {spearman_corr}",
                     fontsize=12)

        # Salva o gráfico em formato PNG com um nome baseado nas variáveis x e y
        plt.savefig('_{}_vs_{}.png'.format(x_var, y_var), dpi=550, bbox_inches='tight')

        # Limpa a figura atual para que a próxima iteração do loop possa começar com uma figura vazia
        plt.clf()


def graficosRQ1(m_mediana_arquivos, c_mediana_arquivos, m_mediana_additions,
                c_mediana_additions, m_median_deletions, c_mediana_deletions):
    states = ['merged', 'closed']
    values1 = [m_mediana_arquivos, c_mediana_arquivos]
    values2 = [m_mediana_additions, c_mediana_additions]
    values3 = [m_median_deletions, c_mediana_deletions]

    # G1
    plt.bar(states, values1)
    plt.title('Gráfico de barras')
    plt.xlabel('status do pr')
    plt.ylabel('qtd de arquivos')
    plt.show()

    # G2
    plt.bar(states, values2)
    plt.title('Gráfico de barras')
    plt.xlabel('status do pr')
    plt.ylabel('qtd de linhas adicionadas')
    plt.show()

    # G3
    plt.bar(states, values3)
    plt.title('Gráfico de barras')
    plt.xlabel('status do pr')
    plt.ylabel('qtd de linhas adicionadas')
    plt.show()

def graficosRQ2(m_median_review_time, c_median_review_time):
    states = ['merged', 'closed']
    values1 = [c_median_review_time, m_median_review_time]

    # G1
    plt.bar(states, values1)
    plt.title('Gráfico de barras')
    plt.xlabel('status do pr')
    plt.ylabel('review time')
    plt.show()


def graficosRQ3(c_median_num_caracteres, m_median_num_caracteres):
    states = ['merged', 'closed']
    values1 = [c_median_num_caracteres, m_median_num_caracteres]

    # G1
    plt.bar(states, values1)
    plt.title('Gráfico de barras')
    plt.xlabel('status do pr')
    plt.ylabel('tamanho descrição')
    plt.show()

def graficosRQ4(c_median_num_comments, m_median_num_comments,c_median_num_participants, m_median_num_participants):
    states = ['merged', 'closed']
    values1 = [c_median_num_comments, m_median_num_comments]
    values2 = [m_median_num_participants, m_median_num_participants]

    # G1
    plt.bar(states, values1)
    plt.title('Gráfico de barras')
    plt.xlabel('status do pr')
    plt.ylabel('numero comentários')
    plt.show()

    # G2
    plt.bar(states, values2)
    plt.title('Gráfico de barras')
    plt.xlabel('status do pr')
    plt.ylabel('numero participantes')
    plt.show()


def main():
    df_merged = pd.read_csv('prs_merged.csv')
    m_mediana_arquivos = statistics.median(df_merged["num_arquivos"])
    m_mediana_additions = statistics.median(df_merged["num_additions"])
    m_median_deletions = statistics.median(df_merged["num_deletions"])
    m_median_review_time = statistics.median(df_merged["review_time"])
    m_median_num_caracteres = statistics.median(df_merged["num_caracteres"])
    m_median_num_participants = statistics.median(df_merged["num_participants"])
    m_median_num_comments = statistics.median(df_merged["num_comments"])

    df_closed = pd.read_csv('prs_closed.csv')
    c_mediana_arquivos = statistics.median(df_closed["num_arquivos"])
    c_mediana_additions = statistics.median(df_closed["num_additions"])
    c_mediana_deletions = statistics.median(df_closed["num_deletions"])
    c_median_review_time = statistics.median(df_closed["review_time"])
    c_median_num_caracteres = statistics.median(df_closed["num_caracteres"])
    c_median_num_participants = statistics.median(df_closed["num_participants"])
    c_median_num_comments = statistics.median(df_closed["num_comments"])


    graficosRQ1(m_mediana_arquivos, c_mediana_arquivos, m_mediana_additions,
                c_mediana_additions, m_median_deletions, c_mediana_deletions)
    graficosRQ2(m_median_review_time, c_median_review_time)
    graficosRQ3(m_median_num_caracteres,c_median_num_caracteres)
    graficosRQ4(c_median_num_comments, m_median_num_comments,c_median_num_participants, m_median_num_participants)
    graficosScatterPlot()



    # graficosRQ5() - scatter plot
    # graficosRQ6() - scatter plot
    # graficosRQ7() - scatter plot
    # graficosRQ8() - scatter plot


main()
