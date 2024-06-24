import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Pontuação Px SUS to PLOT - Página1.csv")

#tratamento do DF 

df['Pontuação Px'] = df['Pontuação Px'].str.replace(',', '.')
df['Pontuação Px'] = pd.to_numeric(df['Pontuação Px'])

sns.boxplot(data=df)
plt.title("Gráfica de Caixa - SUS")
plt.xlabel("Todos os Participantes")
plt.ylabel("Pontuação em %") 
plt.show()
print(df)