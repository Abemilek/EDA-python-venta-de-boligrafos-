import pandas as pd
import matplotlib.pyplot as plt

#graficos de randink de boligrafos

file_path = "Data/Pen Sales Data.xlsx"

df_pen_sales = pd.read_excel(file_path, sheet_name="Pen Sales")

df_pen_sales["Item"] = df_pen_sales["Item"].str.strip()

conteo_de_productos = df_pen_sales["Item"].value_counts()

print("Conteo de productos vendidos:")
print(conteo_de_productos)

plt.figure(figsize=(10, 5))
conteo_de_productos.plot(kind="barh", color="green")

plt.title("Ranking de popularidad de bolígrafos")
plt.xlabel("Cantidad de ventas")
plt.ylabel("Tipo de producto")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show(block=True)
plt.show()