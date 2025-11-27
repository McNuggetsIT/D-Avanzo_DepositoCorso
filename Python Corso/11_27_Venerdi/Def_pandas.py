import pandas as pd

#pandas è una libreria software di scrittura per il linguaggio id programmazione python per la manipolazione e l'analisi dei dati.
#Si usa per 2 cose: PREPARAZIONE DEI DATI ( PRE ANALISI) e PULIZIA DEI DATI 
#Oggi panda è il core della pulizia e preparazione dei dati

#Pandas introduce 2 struttre dati fondamentali: DataFrame e Series

#DataFrame: deve essere diviso fra bidimensioanle
#DataFrame viene vista come un foglioe excel / tabella sqp o foglio di calcolo dove ha colonne e righe
#Series: è una struttura UNIDIMENSIONALE che può essere vista come una sola colonna di DataFrame.


#Pandas è apprezzato per diverse funzionalità:
#Manipolazione dei dati:permette di esegiore operazioni ompklesse su dati come selet filter e fuse
#Pulizia dei dati: offre molteplici funzioni per trattare i dati mancati, rimuovere i duplicati e convertire formati di dati
#Analisi dei dati: supporta operazioni come aggregazioni sommario statistico e altra funz analitiche per estrarre insight dai dati
#Introspettibilità  : Si integra bene con le libr python per la visibilità dei dati come Matplotlib e analisi statistica come scipy

import pandas as pd

data = {
    'Nome': ['Alice', 'Bob','Carla','Luca'],
    'Eta': [25,30,22,15],
    'Citta': ['Roma','Milano','Napoli','Spagna']
}

df = pd.DataFrame(data)

#Stampa del DataFrame originale
print("DataFrame Originale: ")
print(df)

#Selezione delle righe dove l'età è superiore a 23
df_older = df[df['Eta']>23]

#Stampa delle righe selezionate
print("Persone con età superiore a 23 anni: ")
print(df_older)

#Aggiungiamo una nuova colonna la persona maggiorenne
df['Maggiorenne'] = df['Eta'] >= 18

#Stampa del DataFrame con la nuova colonna
print("DataFrame con colonna 'maggiorenne': ")
print(df)

