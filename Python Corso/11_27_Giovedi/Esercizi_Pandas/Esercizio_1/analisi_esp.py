import pandas as pd

file_path = "Python Corso/11_27_Venerdi/Esercizi_Pandas/Esercizio_1/dati.csv"

def categoria(eta):
    if eta <= 18:
        return "Giovane"
    elif eta <= 64:
        return "Adulto"
    else:
        return "Senior"


print("--------------------------------caricamento df--------------------------------")
df = pd.read_csv(file_path)
print(df)

print("--------------------------------prime 5--------------------------------")
print(df.head())
print("\n--------------------------------ultime 5--------------------------------")
print(df.tail())

print("--------------------------------tipo dati--------------------------------")
print(df.info())

print("--------------------------------stast--------------------------------")
mee = df['Eta'].mean()
mes = df['Salario'].mean()
print("Media Età:", mee)
print("Media Salario:", mes)

mede = df['Eta'].median()
meds = df['Salario'].median()

print("Mediana Età:", mede)
print("Mediana Salario:", meds)

std_eta = df['Eta'].std()
std_sal = df['Salario'].std()
print("Deviazione Standard Età:", std_eta)
print("Deviazione Standard Salario:", std_sal)


df = df.drop_duplicates()
print(df)

print("--------------------------------Sost mancanti--------------------------------")
df['Eta'].fillna(df['Eta'].mean(), inplace=True)
df['Salario'].fillna(df['Salario'].mean(), inplace=True)
print(df)

print("--------------------------------rimuovi i dati vuoti (nome e citta)--------------------------------")
df = df.dropna()
print(df)

df['Eta'] = df['Eta'].round(0).astype(int)
print(df)


print("--------------------------------agg col 'Categoria--------------------------------'")

#'self.df['Age Category'] = ['Senior' if age > 65 else ('Adult' if age>18 else 'Young') for age in self.df['Age']]
df['Categoria'] = df['Eta'].apply(categoria)
print(df)

print("--------------------------------salvatagio--------------------------------")
df.to_csv("Python Corso/11_27_Venerdi/Esercizi_Pandas/Esercizio_1/dati_puliti.csv", index=False)
print("File salvato")


