import pandas as pd
import matplotlib.pyplot as plt

file_path = "Data/Pen Sales Data.xlsx"
df_pen_sales = pd.read_excel(file_path, sheet_name="Pen Sales")

df_pen_sales["Item"] = df_pen_sales["Item"].str.strip()

df_avg_pen_costs = df_pen_sales.groupby("Item")["Shipping Cost"].mean().sort_values()

print("Tipos de datos del DataFrame:")
print(df_pen_sales.dtypes)
print("\nCosto promedio de envío por tipo de producto:")
print(df_avg_pen_costs)

plt.figure(figsize=(10, 5))
df_avg_pen_costs.plot(kind="barh", color="green")
plt.title("Costo de envío promedio por producto")
plt.xlabel("Costo medio de envío")
plt.ylabel("Tipo de producto")
plt.tight_layout()
plt.show()

conteo_de_productos = df_pen_sales["Item"].value_counts()

print("\nConteo de productos vendidos:")
print(conteo_de_productos)

plt.figure(figsize=(10, 5))
conteo_de_productos.plot(kind="barh", color="green")
plt.title("Ranking de popularidad de productos")
plt.xlabel("Cantidad de ventas")
plt.ylabel("Tipo de producto")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

print("\nFechas de entrega:")
print(df_pen_sales["Delivery Date"])

tiempo_de_entrega = (df_pen_sales["Delivery Date"] - df_pen_sales["Purchase Date"])
print("\nTiempo de entrega por pedido:")
print(tiempo_de_entrega)

df_pen_sales["Tiempo de entrega"] = tiempo_de_entrega.dt.days
promedio_entrega = df_pen_sales.groupby("Item")["Tiempo de entrega"].mean().sort_values()

plt.figure(figsize=(10, 5))
promedio_entrega.plot(kind="barh", color="orange")
plt.title("Tiempo promedio de entrega por producto")
plt.xlabel("Días")
plt.ylabel("Tipo de producto")
plt.tight_layout()
plt.show()
