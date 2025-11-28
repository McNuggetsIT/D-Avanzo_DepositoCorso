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

# Pandas permette un'indicizzazione flessibile e sofisticata, facilitando l'accesso ai dati
# e la loro manipolazione. Ad esempio, l'uso di indici gerarchici (MultiIndex)
# consente di lavorare con dati ad alta dimensionalità all'interno di strutture tabulari bidimensionali.

# Unione e concatenazione: con Pandas è possibile combinare facilmente diverse fonti di dati
# tramite operazioni come merge, per unire DataFrame in modo simile ai join SQL,
# oppure concat, per concatenare DataFrame lungo un asse specifico,
# gestendo correttamente anche indici che non si allineano.


# PIVOT e PIVOT_TABLE sono due metodi che permettono di trasformare i dati,
# facilitando la ristrutturazione e la creazione di tabelle pivot.
# Sono utili per riorganizzare i dati in un formato più appropriato all’analisi.

# GroupBy (approccio SPLIT–APPLY–COMBINE) permette di dividere i dati in gruppi,
# applicare una funzione a ciascun gruppo e combinare i risultati in una nuova struttura.
# È utile per aggregazioni complesse, trasformazioni e operazioni di filtraggio.

# Gestione del tempo: Pandas offre funzionalità avanzate per la manipolazione delle serie temporali.
# Include la generazione di periodi di tempo, la conversione di frequenze,
# operazioni di windowing o rolling statistics e la gestione di date e orari.
