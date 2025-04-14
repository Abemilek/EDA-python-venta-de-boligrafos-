#%%
import pandas as pd
import matplotlib.pyplot as plt


file_path = "./Pen Sales Data.xlsx"
df_pen_sales = pd.read_excel(file_path, sheet_name="Pen Sales")

df_pen_sales["Item"] = df_pen_sales["Item"].str.strip()

df_avg_pen_costs = df_pen_sales.groupby("Item")["Shipping Cost"].mean().sort_values()

print(df_pen_sales.dtypes)
print(df_avg_pen_costs)

plt.figure(figsize=(10, 5))
df_avg_pen_costs.plot(kind="barh", color="green")
plt.title("Costo de envío promedio por producto")
plt.xlabel("Costo medio de envío")
plt.ylabel("Tipo de producto")
plt.tight_layout()
plt.show()

#%%
#randink de boligrafos
#%%
conteo_de_productos = df_pen_sales["Item"].value_counts()
#%%
print(conteo_de_productos)
#%%
plt.figure(figsize=(10,5))
conteo_de_productos.plot(kind="barh", color="green")
plt.title("randink de popularidad de productos")
plt.xlabel("cantidad de ventas")
plt.ylabel("tipo de producto")
plt.gca().invert_yaxis()
plt.show()
#%%

#%%
#analisis de tiempo de entrega
#%%
print (df_pen_sales["Delivery Date"])
#%%
tiempo_de_entrega = (df_pen_sales["Delivery Date"] - df_pen_sales["Purchase Date"])
#%%
print (tiempo_de_entrega )
#%%
