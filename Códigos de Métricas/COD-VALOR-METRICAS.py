import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table

# Read the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\edume\Desktop\Faculdade\Python-Gráficos\Valores das Métricas - Página1.csv')

# Define a primeira coluna como índice
df = df.set_index(df.columns[0]) 

# Transpõe o DataFrame
df_transposed = df.transpose()

# Cria uma figura e eixos para a tabela
fig, ax = plt.subplots(figsize=(7, 4))  # Ajuste o tamanho conforme necessário

# Desenha a tabela transposta no eixo
table(ax, df_transposed, loc='center')

# Remove os eixos (opcional, para ter apenas a tabela)
ax.axis('off')

# Salva a figura como imagem (por exemplo, PNG)
plt.savefig('Tabela com Valores-Médias das Métricas.png')

# Mostra a tabela (opcional)
plt.show()