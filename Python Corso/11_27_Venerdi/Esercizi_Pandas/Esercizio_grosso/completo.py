# Pandas - Analisi Churn Clienti Telecomunicazioni

# Obiettivo:
# Utilizzare pandas e numpy per esplorare, pulire, trasformare e analizzare un dataset di clienti.
# L'esercizio mira a costruire un modello predittivo di base per la churn rate
# e scoprire correlazioni tra attributi del cliente e la loro fedeltà.

# Dataset:
# • ID_Cliente: Identificativo unico per ogni cliente
# • Età: Età del cliente
# • Durata_Abbonamento: Mesi di abbonamento
# • Tariffa_Mensile: Costo mensile
# • Dati_Consumati: GB consumati al mese
# • Servizio_Clienti_Contatti: Numero di contatti con il servizio clienti
# • Churn: Se il cliente ha lasciato la compagnia (Sì/No)

# 1. Caricamento e Esplorazione Iniziale:
#    - Caricare i dati da CSV
#    - Usare info(), describe(), value_counts() per esplorare e trovare valori mancanti

# 2. Pulizia dei Dati:
#    - Gestire valori mancanti (imputazione o rimozione)
#    - Correggere anomalie (es. età negative, tariffe irrealistiche)

# 3. Analisi Esplorativa (EDA):
#    - Creare nuove colonne utili, es. Costo_per_GB = Tariffa_Mensile / Dati_Consumati
#    - Usare groupby() per analizzare relazioni tra variabili e churn
#    - Usare corr() per trovare correlazioni

# 4. Preparazione per la Modellazione:
#    - Convertire Churn in numerico (0 = No, 1 = Sì)
#    - Normalizzare le colonne numeriche con numpy

# 5. Analisi Statistica e Predittiva:
#    - Implementare regressione logistica con scikit-learn
#    - Valutare il modello con accuratezza e AUC (Area Under Curve)


import numpy as np
import pandas as pd

colonne_numeriche = [
    'Età', 
    'Durata_Abbonamento', 
    'Tariffa_Mensile', 
    'Dati_Consumati', 
    'Servizio_Clienti_Contatti'
]

def categorize_age(age):
    if age > 65:
        return 'Senior'
    elif age > 18:
        return 'Adult'
    else:
        return 'Young'

#    - Caricare i dati da CSV

file = "Python Corso/11_27_Venerdi/Esercizi_Pandas/Esercizio_grosso/telecom_clienti.csv"
df = pd.read_csv(file)

#    - Usare info(), describe(), value_counts() per esplorare e trovare valori mancanti

df.info()
print(df.describe())
print(df['Churn'].value_counts())

#    - Gestire valori mancanti (imputazione o rimozione)
df = df.drop_duplicates()
df['Età'].fillna(df['Età'].mean(), inplace=True)
df['Tariffa_Mensile'].fillna(df['Tariffa_Mensile'].mean(), inplace=True)
df['Durata_Abbonamento'].fillna(df['Durata_Abbonamento'].mean(), inplace=True)
df['Dati_Consumati'].fillna(df['Dati_Consumati'].mean(), inplace=True)
df['Servizio_Clienti_Contatti'].fillna(df['Servizio_Clienti_Contatti'].mean(), inplace=True)

print(df)

df = df.dropna()
#    - Correggere anomalie (es. età negative, tariffe irrealistiche)

df = df[(df['Età'] >= 18) & (df['Età'] <= 120)]
df = df[(df['Tariffa_Mensile'] >= 10) & (df['Tariffa_Mensile'] <= 100)]
df['Età'] = df['Età'].round(0).astype(int)
print(df)

#    - Creare nuove colonne utili, es. Costo_per_GB = Tariffa_Mensile / Dati_Consumati
df['Age Category'] = df['Età'].apply(categorize_age)
df['Costo_per_GB'] = df['Tariffa_Mensile'] / df['Dati_Consumati']
df['CostoTot'] = df['Costo_per_GB'] * df['Dati_Consumati']


consumoToT = df.groupby('Age Category')['Dati_Consumati'].sum()
consumoCorr = df['Età'].corr(df['Dati_Consumati'])
costoTot = df.groupby('Età')['CostoTot'].sum()

print(costoTot)
print(consumoToT)
print("CONSUMO CORR PROVA" + "--------" * 3)
print(consumoCorr)

#    - Convertire Churn in numerico (0 = No, 1 = Sì)

df['Churn_Num'] = df['Churn'].replace({'No': 0, 'Sì': 1})

#    - Normalizzare le colonne numeriche con numpy

for col in colonne_numeriche:
    minimo = df[col].min()
    massimo = df[col].max()
    df[col + '_norm'] = (df[col] - minimo) / (massimo - minimo)