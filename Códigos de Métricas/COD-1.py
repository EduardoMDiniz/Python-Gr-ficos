import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table

# Lê o arquivo CSV
df = pd.read_csv(r'C:\Users\edume\Desktop\Faculdade\Python-Gráficos\Valores das Métricas 02 - Página1.csv')

# Cria a figura e os eixos
fig, ax = plt.subplots(figsize=(12, 4))  # Ajuste o tamanho conforme necessário

# Desenha a tabela com fonte maior
table(ax, df, loc='center', fontsize=20)  # Ajuste o tamanho da fonte conforme necessário

# Remove os eixos para ter apenas a tabela
ax.axis('off')

# Salva a figura como imagem
plt.savefig('tabela_metricas.png')

# Mostra a tabela (opcional)
plt.show()