import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("train.csv")

data = df[["GrLivArea", "BedroomAbvGr", "FullBath", "SalePrice"]]

print(data.head())

sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

plt.scatter(df["GrLivArea"], df["SalePrice"])
plt.title("Size vs Price")
plt.show()

plt.hist(df["SalePrice"], bins=30)
plt.title("Price Distribution")
plt.show()
