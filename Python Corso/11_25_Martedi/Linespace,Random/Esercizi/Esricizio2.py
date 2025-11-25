import numpy as np   # Importa la libreria NumPy per gestire array e calcoli matematici

# Funzione per leggere i dati da file (dati.txt)
def leggi_dati(file_name="dati.txt"):
    with open(file_name, "r") as f:   # apre il file in lettura
        dati = [float(x) for x in f.read().split()]  # legge tutti i numeri e li converte in float
    return np.array(dati)  # restituisce un array NumPy

# Funzione per salvare i risultati dei calcoli su file (risultati.txt)
def salva_risultati(info, file_name="risultati.txt"):
    scelta = input("Vuoi sovrascrivere il file (w) o aggiungere (a)? [w/a]: ").strip().lower()
    mode = "w" if scelta == "w" else "a"

    with open(file_name, mode) as f:
        if isinstance(info, list):
            for dato in info:
                f.write(str(dato) + "\n")
        else:
            f.write(str(info) + "\n")
    print(f"Risultati salvati in {file_name} (modo: {mode})")


# Funzione per salvare un array su file (dati.txt)
def salva_dati(arr, file_name="dati.txt"):
    scelta = input("Vuoi sovrascrivere il file (w) o aggiungere (a)? [w/a]: ").lower()
    mode = "w" if scelta == "w" else "a"
    with open(file_name, mode) as f:
        for valore in arr:   # scrive ogni valore dell'array su una riga
            f.write(str(valore) + "\n")
    print(f"Array salvato in {file_name} (modo: {scelta})")

# Funzione per creare un array
def crea_array():
    print("\n=== CREA ARRAY ===")
    print("1. Linspace (numeri equidistanti)")
    print("2. Random (valori casuali tra 0 e 1)")

    scelta = input("Cosa vuoi creare? ")

    if scelta == "1":
        arr = np.linspace(0, 10, 50)   # crea 50 numeri equidistanti tra 0 e 10
        print("\nArray LINSPACE:\n", arr)
    elif scelta == "2":
        arr = np.random.randint(0, 10, 50)   # crea 50 numeri interi casuali tra 0 e 9
        print("\nArray RANDOM:\n", arr)
    else:
        print("Scelta non valida.")
        return None
    salva_dati(arr)   # salva l’array creato su dati.txt

# Funzione per calcolare valori sull’array letto da dati.txt
def calcola_array():
    print("\n=== MENU CALCOLA ===")
    print("1. Calcola la somma totale degli elementi del nuovo array")
    print("2. Calcola la somma degli elementi del nuovo array maggiori di 5")
    print("3. Calcola la media degli elementi")
    print("4. Calcola la deviazione standard")
    print("5. Calcola massimo e minimo")

    dati = leggi_dati()   # legge l’array da dati.txt
    scelta = input("Quale operazione vuoi eseguire? ")

    if scelta == "1":
        risultato = f"Somma totale: {np.sum(dati)}"
    elif scelta == "2":
        risultato = f"Somma condizionata (>5): {np.sum(dati[dati > 5])}"
    elif scelta == "3":
        risultato = f"Media: {np.mean(dati)}"
    elif scelta == "4":
        risultato = f"Deviazione standard: {np.std(dati)}"
    elif scelta == "5":
        risultato = f"Max: {np.max(dati)}, Min: {np.min(dati)}"
    else:
        print("Scelta non valida.")
        return

    print(risultato)          # stampa il risultato a schermo
    salva_risultati(risultato)  # salva il risultato su risultati.txt

# Funzione per mostrare il menu principale
def menu():
    print("\n=== MENU PRINCIPALE ===")
    print("1. Crea array (linspace, random)")
    print("2. Calcola (somma totale, somma condizionata, media, std)")
    print("0. Esci")

# Ciclo principale del programma
while True:
    menu()   # mostra il menu principale
    scelta = input("Seleziona un'opzione: ")

    if scelta == "0":
        print("Uscita dal programma...")
        break   # esce dal ciclo e termina il programma
    elif scelta == "1":
        print("Hai scelto CREA.")
        crea_array()   # richiama la funzione per creare array
    elif scelta == "2":
        calcola_array()   # richiama la funzione per calcolare valori
    else:
        print("Scelta non valida, riprova.")
