import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Pontuação Px SUS to PLOT - Página1.csv")

#tratamento do DF 

df['Pontuação Px'] = df['Pontuação Px'].str.replace(',', '.')
df['Pontuação Px'] = pd.to_numeric(df['Pontuação Px'])


plt.figure(figsize=(6.5, 5.2))
sns.boxplot(data=df, x='Participantes', y='Pontuação Px')
plt.title("Gráfico de Caixa Individual- SUS")
plt.xlabel("Participantes")
plt.ylabel("Pontuação em %")
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for readability
plt.show()

print(df)