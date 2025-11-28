from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

file =  "Python Corso/11_27_Venerdi/Esercizi_Pandas/Esercizi_3_pivot/vendite_gennaio2021.csv"

datagen = pd.date_range(start="2025-10-01", end="2025-11-27")
citta = ['Roma', 'Milano', 'Napoli']
prodotti = ['Mouse', 'Tastiera', 'Monitor']

data = {
    'Data': np.random.choice(datagen,size=100),
    'Città': np.random.choice(citta,size=100),
    'Prodotto':np.random.choice(prodotti,size=100),
    'Vendite': np.random.randint(50,100,size=100)
    
}

df2 = pd.DataFrame(data)

df = pd.read_csv(file)
print(df.head())

print(df)

pivot_df = df.pivot_table(values="Vendite",index="Prodotto", columns="Città", aggfunc="mean")
print(pivot_df)
gcitta= df.groupby('Città')['Vendite'].sum()
print(gcitta)

gcitta.plot(kind='bar', title='Vendite totali per città')
plt.xlabel('Città')
plt.ylabel('Quantità')
plt.tight_layout()
plt.show()

print("CON GENERATOREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
pivot_df2 = df2.pivot_table(values="Vendite",index="Prodotto", columns="Città", aggfunc="mean")
print(pivot_df2)
gcitta2= df2.groupby('Città')['Vendite'].sum()
print(gcitta2)

gcitta2.plot(kind='bar', title='Vendite totali per città')
plt.xlabel('Città')
plt.ylabel('Quantità')
plt.tight_layout()
plt.show()

