import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Univariate
print(df["kategori"].value_counts())

df["kategori"].value_counts().plot(kind="bar")
plt.title("Distribusi Kategori Sampah")
plt.show()