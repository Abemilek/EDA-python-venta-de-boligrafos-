import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo Excel
df = pd.read_excel("Data/Pen Sales Data.xlsx")

# Convertir la columna 'Purchase Date' a formato datetime
df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])

# Crear una nueva columna con año y mes
df['Year-Month'] = df['Purchase Date'].dt.to_period('M')

# Contar el número de ventas por mes
ventas_por_mes = df.groupby('Year-Month').size()

# Convertir el índice a string para graficar bien
ventas_por_mes.index = ventas_por_mes.index.astype(str)

# Graficar
plt.figure(figsize=(10, 5))
plt.plot(ventas_por_mes.index, ventas_por_mes.values, marker='o', color='teal')
plt.title("Ventas de bolígrafos por mes")
plt.xlabel("Mes")
plt.ylabel("Número de ventas")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
