#GroupBy Split_Apply_Combine
import pandas as pd

file_path = "Python Corso/11_27_Venerdi/pandas/pivot.csv"

data = {
    'Data': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
    'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],
    'Vendite': [100, 200, 150, 300, 250]
}



df = pd.DataFrame(data)
print(df)

grouped_df = df.groupby('Prodotto').sum()
print(grouped_df)