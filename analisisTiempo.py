import pandas as pd
import matplotlib.pyplot as plt

ruta_archivo = "Data/Pen Sales Data.xlsx"
datos_ventas = pd.read_excel(ruta_archivo, sheet_name="Pen Sales")
datos_ventas["Producto"] = datos_ventas["Item"].str.strip()
datos_ventas["Tiempo de Entrega"] = (datos_ventas["Delivery Date"] - datos_ventas["Purchase Date"]).dt.days

tiempo_promedio = datos_ventas.groupby("Producto")["Tiempo de Entrega"].mean().sort_values()
print("Tiempo promedio de entrega por tipo de bolígrafo:")
print(tiempo_promedio)

plt.figure(figsize=(9, 5))
tiempo_promedio.plot(kind="bar", color="orange")
plt.title("Tiempo Promedio de Entrega por Tipo de Bolígrafo")
plt.xlabel("Tipo de Bolígrafo")
plt.ylabel("Tiempo Promedio de Entrega (Días)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
