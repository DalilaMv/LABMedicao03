import statistics
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from sklearn.linear_model import LinearRegression
import numpy as np
import scipy.stats as stats


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


def boxPlotGenerator(valor_merged, valor_closed, label):
    fig, ax = plt.subplots()

    ax.boxplot([valor_merged, valor_closed])

    ax.set_xticklabels(['Merged', 'Closed'])
    ax.set_title(label)
    ax.set_xlabel('State')
    ax.set_ylabel(label)

    plt.show()


def scatterPlotGenerator(num_reviews, eixoy, label):
    plt.scatter(num_reviews, eixoy)

    corr_coef, _ = spearmanr(num_reviews, eixoy)
    plt.text(0.1, 0.9, f'Coeficiente de correlação de Spearman: {corr_coef:.2f}',
             transform=plt.gca().transAxes)

    # Cálculo da regressão linear
    x = np.array(num_reviews)
    y = np.array(eixoy)
    m, b = np.polyfit(x, y, 1)

    # Desenho da linha de regressão
    plt.plot(x, m*x+b, color='red')

    plt.xlabel('Número de Reviews')
    plt.ylabel(label)

    plt.show()


def main():
    df = pd.read_csv('resultado_final.csv', on_bad_lines='skip')
    df.dropna(subset=['review_time'], inplace=True)
    df_merged = pd.read_csv('prs_merged.csv')
    df_closed = pd.read_csv('prs_closed.csv')

    m_num_arquivos = df_merged['num_arquivos']
    c_num_arquivos = df_closed['num_arquivos']
    label_arquivos = "Número de Arquivos"
    m_num_additions = df_merged['num_additions']
    c_num_additions = df_closed['num_additions']
    label_additions = "Número de linhas adicionadas"
    m_num_deletions = df_merged['num_deletions']
    c_num_deletions = df_closed['num_deletions']
    label_deletions = "Número de linhas removidas"
    m_review_time = list(map(time_to_minutes, df_merged['review_time']))
    c_review_time = list(map(time_to_minutes, df_closed['review_time']))
    label_time = "Tempo de análise em minutos"
    m_num_caracteres = df_merged['num_caracteres']
    c_num_caracteres = df_closed['num_caracteres']
    label_caracteres = "Número de caracteres na descrição"
    m_num_comments = df_merged['num_comments']
    c_num_comments = df_closed['num_comments']
    label_comments = "Número de comentários"
    m_num_participants = df_merged['num_participants']
    c_num_participants = df_closed['num_participants']
    label_participants = "Número de participantes"

    boxPlotGenerator(m_num_arquivos, c_num_arquivos, label_arquivos)
    boxPlotGenerator(m_num_additions, c_num_additions, label_additions)
    boxPlotGenerator(m_num_deletions, c_num_deletions, label_deletions)
    boxPlotGenerator(m_review_time, c_review_time, label_time)
    boxPlotGenerator(m_num_caracteres, c_num_caracteres, label_caracteres)
    boxPlotGenerator(m_num_comments, c_num_comments, label_comments)
    boxPlotGenerator(m_num_participants,
                     c_num_participants, label_participants)

    num_reviews = df['num_reviews']
    num_arquivos = df['num_arquivos']
    num_additions = df['num_additions']
    num_deletions = df['num_deletions']
    review_time = list(map(time_to_minutes, df['review_time']))
    num_caracteres = df['num_caracteres']
    num_comments = df['num_comments']
    num_participants = df['num_participants']

    scatterPlotGenerator(num_reviews, num_arquivos, label_arquivos)
    scatterPlotGenerator(num_reviews, num_additions, label_additions)
    scatterPlotGenerator(num_reviews, num_deletions, label_deletions)
    scatterPlotGenerator(num_reviews, review_time, label_time)
    scatterPlotGenerator(num_reviews, num_caracteres, label_caracteres)
    scatterPlotGenerator(num_reviews, num_comments, label_comments)
    scatterPlotGenerator(num_reviews, num_participants, label_participants)


main()
