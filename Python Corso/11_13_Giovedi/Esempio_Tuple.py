# ==========================
# TUPLE
# ==========================
# Le tuple sono costanti: i valori al loro interno NON possono cambiare.
# Si usano per raggruppare valori correlati (coordinate, RGB, dati persona).

punto = (3, 4)
colore_rgb = (255, 128, 0)
informazioni_persona = ("Alice", 25, "Femmina")

# Accesso agli elementi con indice (come le liste):
print(punto[0])  # 3
print(punto[1])  # 4

# Creazione senza parentesi:
punto1 = 3, 4
x, y = punto1
print(x, y)      # 3 4

# ==========================
# SET (INSIEMI)
# ==========================
# Gli insiemi non accettano duplicati e non mantengono l'ordine.

set1 = {1, 2, 3, 4, 5}   # da letterale, più semplice e leggibile
set2 = {4,5,6,7,8}        # direttamente con {}

# Duplicati ignorati:
set3 = {1,2,3,4,5}
print(set3)   # {1,2,3,4,5}

# Operazioni insiemistiche:
set4 = {1,2,3,4,5}
set5 = {3,4,5,6,7}

print(set4.union(set5))              # {1,2,3,4,5,6,7}
print(set4.intersection(set5))       # {3,4,5}
print(set4.difference(set5))         # {1,2}
print(set5.difference(set4))         # {6,7}
print(set4.symmetric_difference(set5)) # {1,2,6,7}

# Metodi principali:
numeri = {1, 2, 3}
numeri.add(4)        # aggiunta
numeri.remove(2)     # rimozione (errore se non esiste)
numeri.discard(10)   # rimozione (nessun errore se non esiste)
print(len(numeri))   # lunghezza
print(1 in numeri)   # controllo presenza
copia = numeri.copy() # copia indipendente

# Nota:
# - Nessun duplicato
# - Ordine non garantito
