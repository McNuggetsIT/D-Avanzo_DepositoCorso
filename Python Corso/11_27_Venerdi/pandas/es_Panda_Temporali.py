# Pandas - Serie Temporali

# Pandas offre strumenti specifici per manipolare date e tempi,
# permettendo di analizzare serie temporali, cambiare la frequenza dei dati
# e generare periodi di tempo.

# Esempio 1: Generazione di una serie di date
import pandas as pd
file_path = "Python Corso/11_27_Venerdi/Esercizi_Pandas/Esercizio2/dati.csv"
df = pd.read_csv(file_path)
date_range = pd.date_range(start='2021-01-01', periods=10, freq='M')

# Esempio 2: Resampling dei dati di una serie temporale
#df_resampled = df.resample('M').mean()

# Esempio: conversione della colonna "date" da stringa a datetime
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
pd.to_datetime()

# Converte un indice o una colonna in formato datetime,
# permettendo di sfruttare tutte le funzionalità di time series di Python.

import pandas as pd

# Esempio: conversione della colonna "date" da stringa a datetime
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# Oppure per creare un indice datetime
df.index = pd.to_datetime(df['date'])

# DataFrame.resample()
# Ridimensiona (aggregate o down/up-sample) la frequenza temporale dei dati,
# specificando l’intervallo desiderato (‘D’ = giorno, ‘M’ = mese, ‘H’ = ora, ecc.)

# Esempi:
df_daily = df.resample('D').mean()       # media giornaliera
df_monthly = df.resample('M').sum()      # somma mensile


pd.Series.shift()
# "Sposta" i valori lungo l’asse temporale di un numero di periodi.
# Utile per calcolare differenze ritardate, tassi di crescita, ecc.

# Esempio: aggiunge una colonna con il valore del giorno precedente
df['prev_day'] = df['value'].shift(1)

# Tasso di variazione giornaliero
df['daily_return'] = df['value'].pct_change()
# (equivalente a shift + calcolo della percentuale)

pd.Series.rolling()
# Calcola statistiche mobili su una finestra temporale scorrevole.

# Esempio: finestra mobile di 7 giorni — media e deviazione standard
df['rolling_mean7'] = df['value'].rolling(window=7).mean()
df['rolling_std7']  = df['value'].rolling(window=7).std()
