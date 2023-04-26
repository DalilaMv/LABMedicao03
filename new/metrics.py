import statistics
import pandas as pd
import matplotlib.pyplot as plt

def separar_csv():
    df = pd.read_csv('resultado_final.csv', on_bad_lines='skip')

    merged_df = df[df['state'] == 'MERGED']

    merged_df.to_csv('prs_merged.csv', index=False)

    closed_df = df[df['state'] == 'CLOSED']

    closed_df.to_csv('prs_closed.csv', index=False)

df_merged = pd.read_csv('prs_merged.csv')
m_num_arquivos_median = statistics.median(df_merged["num_arquivos"]) 

df_closed = pd.read_csv('prs_closed.csv')
c_num_arquivos_median = statistics.median(df_closed["num_arquivos"]) 
print(c_num_arquivos_median)
print(m_num_arquivos_median)


labels = ['merged', 'closed']
values = [m_num_arquivos_median,c_num_arquivos_median]
plt.bar(labels, values)
#  Adicionar título e rótulos dos eixos
plt.title('Gráfico de barras')
plt.xlabel('status do pr')
plt.ylabel('qtd de arquivos')

# Mostrar o gráfico
plt.show()




