import pandas as pd

file_path = "Python Corso/11_27_Venerdi/pandas/vendite.csv"
df = pd.read_csv(file_path)
print(df.head(2))