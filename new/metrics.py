import statistics
import pandas as pd
import matplotlib.pyplot as plt


def separar_csv():
    df = pd.read_csv('resultado_final.csv', on_bad_lines='skip')

    merged_df = df[df['state'] == 'MERGED']

    merged_df.to_csv('prs_merged.csv', index=False)

    closed_df = df[df['state'] == 'CLOSED']

    closed_df.to_csv('prs_closed.csv', index=False)


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


def main():
    df_merged = pd.read_csv('prs_merged.csv')
    m_mediana_arquivos = statistics.median(df_merged["num_arquivos"])
    m_mediana_additions = statistics.median(df_merged["num_additions"])
    m_median_deletions = statistics.median(df_merged["num_deletions"])

    df_closed = pd.read_csv('prs_closed.csv')
    c_mediana_arquivos = statistics.median(df_closed["num_arquivos"])
    c_mediana_additions = statistics.median(df_merged["num_additions"])
    c_mediana_deletions = statistics.median(df_merged["num_deletions"])

    graficosRQ1(m_mediana_arquivos, c_mediana_arquivos, m_mediana_additions,
                c_mediana_additions, m_median_deletions, c_mediana_deletions)


main()
