import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV data into a DataFrame
df = pd.read_csv("SUS NEW.csv")

# Extract the data for the stacked bar chart
participantes = df["Participante"].tolist()  # Assuming "Participante" is the column name for participant IDs
suso1 = df["SUS1"].tolist()
suso2 = df["SUS2"].tolist()
suso3 = df["SUS3"].tolist()
suso4 = df["SUS4"].tolist()
suso5 = df["SUS5"].tolist()
suso6 = df["SUS6"].tolist()
suso7 = df["SUS7"].tolist()
suso8 = df["SUS8"].tolist()
suso9 = df["SUS9"].tolist()
suso10 = df["SUS10"].tolist()

# Create the stacked bar chart
x = range(len(participantes))  # Define the x-axis positions
width = 0.35  # Define the width of the bars

fig, ax = plt.subplots(figsize=(12, 8))  # Create a figure and an axis

rects1 = ax.bar(x - width/2, suso1, width, label='SUS1', color='b')
rects2 = ax.bar(x + width/2, suso2, width, label='SUS2', color='g')
rects3 = ax.bar(x + 3*width/2, suso3, width, label='SUS3', color='r')
rects4 = ax.bar(x + 5*width/2, suso4, width, label='SUS4', color='c')
rects5 = ax.bar(x + 7*width/2, suso5, width, label='SUS5', color='m')
rects6 = ax.bar(x + 9*width/2, suso6, width, label='SUS6', color='y')
rects7 = ax.bar(x - width/2, suso7, width, label='SUS7', color='b', alpha=0.5)

# Add labels and title
ax.set_xticks(x)
ax.set_xticklabels(participantes, rotation=45, ha='right')  # Rotate participant labels for better readability
ax.set_xlabel("Participante")
ax.set_ylabel("Valor")
ax.set_title("Comparação de Valores por Participante")

# Add legend
ax.legend()

# Adjust the layout of the chart
plt.tight_layout()

# Show the chart
plt.show()