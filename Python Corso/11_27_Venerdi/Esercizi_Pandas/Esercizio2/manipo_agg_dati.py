import pandas as pd

file_path = "Python Corso/11_27_Venerdi/Esercizi_Pandas/Esercizio2/dati.csv"

df = pd.read_csv(file_path)

df['TotVendite'] = df['Prezzo Unitario'] * df['Quantità']

print(df)
print("AAAAAAAAAAAAAAAAAAAAA")
prodotto_top = df.groupby('Prodotto')['Quantità'].sum().idxmax()
quantita_top = df.groupby('Prodotto')['Quantità'].sum().max()
print(f"{prodotto_top} con {quantita_top} pezzi venduti")

print("AAAAAAAAAAAAAAAAAAAAA")
citta_top = df.groupby('Città')['TotVendite'].sum().idxmax()
vendite_tot = df.groupby('Città')['TotVendite'].sum().max()
print(f"{citta_top} con {vendite_tot:.2f}") #2f perhè semplifio il numero a 0.XX



