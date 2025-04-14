import pandas as pd
import matplotlib.pyplot as plt

ruta_archivo = "Data/Pen Sales Data.xlsx"
datos_ventas = pd.read_excel(ruta_archivo, sheet_name="Pen Sales")
datos_ventas["Producto"] = datos_ventas["Item"].str.strip()

promedio_envio = datos_ventas.groupby("Producto")["Shipping Cost"].mean().sort_values()
print("Costo promedio de envío por producto:")
print(promedio_envio)

plt.figure(figsize=(9, 5))
promedio_envio.plot(kind="barh", color="purple")
plt.title("Costo Promedio de Envío por Producto")
plt.xlabel("Costo Promedio de Envío")
plt.ylabel("Producto")
plt.tight_layout()
plt.show()
