# Esercizio con NumPy
# Parte UNO:
# Scrivere un sistema che utilizza NumPy per gestire un array 2D.
# Il programma deve presentare un menu interattivo che consente all'utente di eseguire varie operazioni sull'array.
# Ogni volta che il sistema conclude un calcolo, il risultato va salvato su un file .txt.

# Operazioni disponibili:
# 1. Creare un nuovo array 2D di dimensioni specificate dall'utente con numeri casuali.
# 2. Estrarre e stampare la sotto-matrice centrale.
# 3. Trasporre l'array e stamparlo.
# 4. Calcolare e stampare la somma di tutti gli elementi dell'array.
# 5. Uscire dal programma o ripetere.

# Parte DUE:
# Specializzare il sistema aggiungendo nuove operazioni:
# 6. Moltiplicazione elemento per elemento con un altro array: 
#    l'utente può creare una seconda matrice delle stesse dimensioni e moltiplicarle elemento per elemento.
# 7. Calcolo della media degli elementi dell'array.
import numpy as np
from io import StringIO

def puliscitxt(file_name="dati.txt"):
    with open(file_name, "r") as f:
        righe = [riga.replace("[", "").replace("]", "") for riga in f]
    matrice2d = np.loadtxt(StringIO("\n".join(righe)))
    return matrice2d

def salva_dati(arr, file_name="dati.txt"):
    scelta = input("Vuoi sovrascrivere il file (w) o aggiungere (a)? [w/a]: ").lower()
    mode = "w" if scelta == "w" else "a"
    with open(file_name, mode) as f:
        for riga in arr:   # scrive ogni riga della matrice
            f.write(" ".join(map(str, riga)) + "\n")
        f.write("\n")  # separatore tra matrici
    print(f"Array salvato in {file_name} (modo: {scelta})")
    
import numpy as np

def leggi_dati(file_name="dati.txt"): 
    with open(file_name, "r") as f: 
        dati = [float(x) for x in f.read().split()] 
        return np.array(dati) # 


    
def crea_arr():
    nc = int(input("Quante colonne?: "))
    nr = int(input("Quante righe?: "))
    nmin = int(input("Numero minimo"))
    nmax = int(input("Numero Max"))
    
    arr = np.random.randint(nmin,nmax, size=(nc,nr))
    print(arr)
    salva_dati(arr)
    
def crea_arr_no_salva(shape):
    nmin = int(input("Numero minimo: "))
    nmax = int(input("Numero Max: "))
    
    arr = np.random.randint(nmin, nmax, size=shape)  # stessa forma della matrice originale
    print("Seconda matrice:\n", arr)
    return arr

def estrai_mc(file_name="dati.txt"):
    arr = puliscitxt(file_name)
    
    righe = arr.shape[0]
    indice_riga_centrale = righe // 2
    riga_centrale = arr[indice_riga_centrale]
    print("Riga centrale:", riga_centrale)

def trasponi(file_name="dati.txt"):
    arr = puliscitxt(file_name)
    
    trasposta = arr.T
    print("Matrice originale:\n", arr)
    print("Matrice trasposta:\n", trasposta)

def som(file_name="dati.txt"):
    arr = puliscitxt(file_name)
    som = np.sum(arr)
    print("Matrice summata: ", som)
    
def moltip(file_name="dati.txt"):
    arr = puliscitxt(file_name)
    arr2 = crea_arr_no_salva(arr.shape)
    
    somma = np.multiply(arr,arr2)
    print(somma)
    
def media(file_name="dati.txt"):
    arr = puliscitxt(file_name)
    
    media = arr.mean()
    print(media)

while True:
    print("\n=== MENU PRINCIPALE ===")
    print("1. Creare un nuovo array 2D")
    print("2. Estrarre la sotto-matrice centrale")
    print("3. Trasporre l'array")
    print("4. Calcolare la somma degli elementi")
    print("5  Moltiplicazione")
    print("6  Media")
    print("0. Uscire")

    scelta = input("Seleziona un'opzione: ")

    if scelta == "1":
        print("Hai scelto: Creare un nuovo array 2D")
        crea_arr()
        
    elif scelta == "2":
        print("Hai scelto: Estrarre la sotto-matrice centrale")
        estrai_mc()
    elif scelta == "3":
        print("Hai scelto: Trasporre l'array")
        trasponi()
    elif scelta == "4":
        print("Hai scelto: Calcolare la somma degli elementi")
        som()
    elif scelta == "5":
        print("Hai scelto la moltiplicazione: ")
        moltip()
    elif scelta == "6":
        print("Scelta media:  ")
        media()
    elif scelta == "0":
        print("Uscita dal programma...")
        break
    else:
        print("Scelta non valida, riprova.")
