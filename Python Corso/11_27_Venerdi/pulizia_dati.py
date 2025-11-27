import pandas as pd
import numpy as np

#DF con dati doppi e mancanti
data = {
    'Nome': ['Alice', 'Bob','Carla','Bob','Franco','Gennaro', None],
    'Eta': [25,30,22,30,np.nan,29,30],
    'Citta': ['Roma','Milano','Napoli','Milano','Roma','Milano','Roma']
}

df = pd.DataFrame(data)

#Stampa 
print("DataFrame Originale")
print(df)

#Rimozuone dupliati
df = df.drop_duplicates()

#Gestione dei dati
#RImoz delle righe dove almeno un elemento è manante
df_clean = df.dropna()

#Possiamo sost dati mananti on valore di def
df['Eta'].fillna(df['Eta'].mean(),inplace=True)

#Stampa DataFrame pulito
print("Df dopo pulizia")
print(df_clean)

#Stampa df con dati mancanti sostitutiti
print("Df con dati mancanti")
print(df)