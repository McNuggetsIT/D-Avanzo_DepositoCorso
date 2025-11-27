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
#ANDIAMO A FARE IL AGGFUNC (MEDIA) di VALUES (VENDITE) INDICE PRODOTTO E COLONNE CITTA
pivot_df = df.pivot_table(values="Vendite",index="Prodotto",columns="Città",aggfunc="mean")

print(pivot_df)
