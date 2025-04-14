import pandas as pd
import matplotlib.pyplot as plt

ruta_archivo = "Data/Pen Sales Data.xlsx"
datos_ventas = pd.read_excel(ruta_archivo, sheet_name="Pen Sales")
datos_ventas["Producto"] = datos_ventas["Item"].str.strip()

conteo_productos = datos_ventas["Producto"].value_counts()
print("Conteo de productos vendidos:")
print(conteo_productos)

plt.figure(figsize=(9, 5))
conteo_productos.plot(kind="barh", color="green")
plt.title("Productos Más Vendidos")
plt.xlabel("Cantidad de Ventas")
plt.ylabel("Tipos de Productos")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
