import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\edume\Desktop\Projetos\Python-Gráficos\Métricas GQM - Página1.csv")

#trtamennto df

df['Média'] = df['Média'].str.replace(',', '.').astype(float)
df['Desvio Padrão'] = df['Desvio Padrão'].str.replace(',', '.').astype(float)

# Assuming your DataFrame is named 'df'
plt.bar(df['Questão'], df['Média'])
plt.errorbar(df['Questão'], df['Média'], yerr=df['Desvio Padrão'], fmt='o', color='red', capsize=5, label='Desvio Padrão')

plt.xlabel("Questão")
plt.ylabel("Média")
plt.ylim(0, 5)
plt.title("Gráfico de Barra - GQM")
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for readability
plt.ylim(0, 6)
plt.legend()

plt.show()