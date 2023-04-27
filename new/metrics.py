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


def time_to_minutes(time_str):
    hours, minutes = time_str.split('h')
    total_minutes = int(hours) * 60 + int(minutes.strip('m'))
    return total_minutes


def graficosScatterPlot(variable):

    df_resultadosFinais = pd.read_csv('resultado_final.csv')
    # Variáveis x e y
    x_vars = [variable]
    y_var = ['num_reviews']

    # Loop através de cada variável x
    for x_var in x_vars:
        # Cria um subconjunto dos dados contendo todas as variáveis y
        subset = df_resultadosFinais[[x_var] + y_var]

        # Calcula a correlação de Spearman
        spearman_corr, spearman_pvalue = spearmanr(
            subset[x_var], subset[y_var[0]])

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
        plt.savefig('_{}_vs_{}.png'.format(x_var, y_var),
                    dpi=550, bbox_inches='tight')

        # Limpa a figura atual para que a próxima iteração do loop possa começar com uma figura vazia
        plt.clf()


def graficosRQ1(df_merged, df_closed):
    fig, ax = plt.subplots()

    # G1
    ax.boxplot([df_merged['num_arquivos'], df_closed['num_arquivos']])

    ax.set_xticklabels(['Merged', 'Closed'])
    ax.set_title('Nº de arquivos x State')
    ax.set_xlabel('State')
    ax.set_ylabel('Número de arquivos')

    plt.show()

    fig, ax = plt.subplots()

    # G2
    ax.boxplot([df_merged['num_additions'], df_closed['num_additions']])

    ax.set_xticklabels(['Merged', 'Closed'])
    ax.set_title('Nº de linhas adicionadas x State')
    ax.set_xlabel('State')
    ax.set_ylabel('Número de linhas adicionadas')

    plt.show()

    fig, ax = plt.subplots()

    # G3
    ax.boxplot([df_merged['num_deletions'], df_closed['num_deletions']])

    ax.set_xticklabels(['Merged', 'Closed'])
    ax.set_title('Nº de linhas removidas x State')
    ax.set_xlabel('State')
    ax.set_ylabel('Número de linhas removidas')

    plt.show()


def graficosRQ2(df_merged, df_closed):
    fig, ax = plt.subplots()
    time_list_closed = list(map(time_to_minutes, df_closed['review_time']))
    time_list_merged = list(map(time_to_minutes, df_merged['review_time']))

    ax.boxplot([time_list_closed, time_list_merged])

    ax.set_xticklabels(['Merged', 'Closed'])
    ax.set_title('Tempo de review em minutos x State')
    ax.set_xlabel('State')
    ax.set_ylabel('Tempo de review em minutos')

    plt.show()


def graficosRQ3(df_merged, df_closed):
    fig, ax = plt.subplots()
    ax.boxplot([df_merged['num_caracteres'], df_closed['num_caracteres']])

    ax.set_xticklabels(['Merged', 'Closed'])
    ax.set_title('Tamanho da descrição x State')
    ax.set_xlabel('State')
    ax.set_ylabel('Tamanho da descrição')

    plt.show()


def graficosRQ4(df_merged, df_closed):
    fig, ax = plt.subplots()

    # G1
    ax.boxplot([df_merged['num_comments'], df_closed['num_comments']])
    ax.set_xticklabels(['Merged', 'Closed'])
    ax.set_title('Nº de comentários x State')
    ax.set_xlabel('State')
    ax.set_ylabel('Nº de comentários')

    plt.show()

    # G2
    ax.boxplot([df_merged['num_participants'], df_closed['num_participants']])
    ax.set_xticklabels(['Merged', 'Closed'])
    ax.set_title('Nº de participantes x State')
    ax.set_xlabel('State')
    ax.set_ylabel('Nº de participantes')

    plt.show()


def main():
    df_merged = pd.read_csv('prs_merged.csv')

    df_closed = pd.read_csv('prs_closed.csv')

    graficosRQ1(df_merged, df_closed)
    graficosRQ2(df_merged, df_closed)
    graficosRQ3(df_merged, df_closed)
    graficosRQ4(df_merged, df_closed)


main()
