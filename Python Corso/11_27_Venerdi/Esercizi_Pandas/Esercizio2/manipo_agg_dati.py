import pandas as pd
import matplotlib.pyplot as plt
#istanzio file come path di dati.csv
file_path = "Python Corso/11_27_Venerdi/Esercizi_Pandas/Esercizio2/dati.csv"
#lo converto
df = pd.read_csv(file_path)
#creo tabella tot vendite (facendo prezzo U * quantita)
df['TotVendite'] = df['Prezzo Unitario'] * df['Quantità']
print(df)

print("AAAAAAAAAAAAAAAAAAAAA")

#Credo il prodotto e quantita e li raggruppo tramite GroupBy insieme a prodotto e quantità // .sum (somma) e idxmax come id
prodotto_top = df.groupby('Prodotto')['Quantità'].sum().idxmax()
quantita_top = df.groupby('Prodotto')['Quantità'].sum().max()
print(f"{prodotto_top} con {quantita_top} pezzi venduti")

print("AAAAAAAAAAAAAAAAAAAAA")
#stessa cosa di sopra
citta_top = df.groupby('Città')['TotVendite'].sum().idxmax()
vendite_tot = df.groupby('Città')['TotVendite'].sum().max()
print(f"{citta_top} con {vendite_tot:.2f}") #2f perhè semplifio il numero a 0.XX

print("AAAAAAAAAAAAAAAAAAAAA")
#Filtro le Tot Vendite sopra i 1000 e creo un df nuovo
df_filtrato = df[df['TotVendite']> 1000]
print(df_filtrato)

print("AAAAAAAAAAAAAAAAAAAAA")
#Creo il csv di filtrato
df_filtrato.to_csv("Python Corso/11_27_Venerdi/Esercizi_Pandas/Esercizio2/venditemag.csv")

print("AAAAAAAAAAAAAAAAAAAAA")
#Sorto i value ToTVendite -> Modo Decrescente
totven = df.sort_values(by='TotVendite', ascending=False)
print(totven)

print("AAAAAAAAAAAAAAAAAAAAA")
#Creo le vendite raggruppando Citta e quantità
vendite_citta= df.groupby('Città')['Quantità'].sum()
print(vendite_citta)

#VA BEH ADORO installato matplotlib e creato un grafico
vendite_citta.plot(kind='bar', title='Quantità vendute per città')
plt.xlabel('Città')
plt.ylabel('Quantità')
plt.tight_layout()
plt.show()