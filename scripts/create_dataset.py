import pandas as pd
from sklearn.datasets import load_diabetes

data = load_diabetes()
df = pd.DataFrame(data.data, columns=data.feature_names)
df["target"] = data.target

df.to_csv("data/raw_data.csv", index=False)
print("Dataset saved at data/raw_data.csv")
