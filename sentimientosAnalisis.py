import pandas as pd
import matplotlib.pyplot as plt

ruta_archivo = "Data/Pen Sales Data.xlsx"
datos_ventas = pd.read_excel(ruta_archivo, sheet_name="Pen Sales")
criticas = datos_ventas["Review"]

positivas = ["love", "great", "good", "amazing", "excellent", "best"]
negativas = ["bad", "poor", "dislike", "terrible", "worst", "disappointed", "unfortunately"]

total_positivas = criticas.str.contains("|".join(positivas), case=False, na=False).sum()
total_negativas = criticas.str.contains("|".join(negativas), case=False, na=False).sum()

print("CRÍTICAS POSITIVAS:", total_positivas)
print("CRÍTICAS NEGATIVAS:", total_negativas)

plt.figure(figsize=(6, 6))
plt.pie([total_positivas, total_negativas],
        labels=["Críticas Positivas", "Críticas Negativas"],
        autopct="%1.1f%%", colors=["green", "red"], startangle=140)
plt.title("Reseñas de Sentimientos")
plt.tight_layout()
plt.show()
