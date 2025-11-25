#Broadcasting
#è il concetto piu potente di NumPy che permette di eseguire operazione su array di forma diverse

#___Principi del broadcasting
#rende piu semplice e veloce per la scrittura di codice per element-wise operazioni.

#___Allineamento delle dimensioni__
#Prima controlla se sono allineate se sono uguali O una delle due sono dimensioni è 1

'Aggiunge dimensioni leading: se gli array hanno numeri divewrsi di dimensioni, aggiunge dimensioni leading di 1 all array di 1 all array di meno dimensioni'
'allineamento da destra a sinistra  allallineare gli array partendo dalla dimensione piu a destra'

#Esapnsione delle dimensioni:
#Se le dimensioni non sono compatibili numpy espande l'array piu corto in automatico.
#l'array con la dimensione 1 viene espanso epr avere la stessa dimensione dell'altro array

'compatibilòità delle dimensioni: Due dimensioni compatibili se sono uguali o se una delle due è 1'
#Applicazione dell'Operazione:

'Espansione Automatica: Espanede le dimensioni di 1 per adattarsi alla dimensione dell altro aray'
#una volta che hanno la stessa dimensione numpy esegue l'operazione element-wise.
#L'array piu piccolo viene replicato per riempire l'array piu grande

#Vantaggi del broadcasting

#Efficenza: Evita la necessità di creare copie espliccite di array per adattarsi le dimensioni
#Semplicita: Rende il codice piu leggibile e conciso, eliminando la necessita di scrivere loop espliciti
"""
ESEMPI COMPLETI DI BROADCASTING IN NUMPY
----------------------------------------
Questo file contiene una serie di esempi prattici e commentati
per mostrare come funziona il broadcasting in NumPy.
"""

import numpy as np

print("\n=== 1) Broadcasting con scalare ===")
a = np.array([1, 2, 3])
b = 10
print("Array a:", a)
print("Scalare b:", b)
print("a + b =", a + b)   # Ogni elemento di a riceve +10


print("\n=== 2) Somma tra vettore riga e vettore colonna ===")
row = np.array([1, 2, 3])        # shape (3,)
col = np.array([[10], [20]])     # shape (2,1)
print("row shape:", row.shape)
print("col shape:", col.shape)
print("row + col =\n", row + col)
# Broadcasting crea una matrice 2x3


print("\n=== 3) Broadcasting tra matrice e vettore riga ===")
A = np.array([[1, 2, 3], [4, 5, 6]])
v = np.array([10, 20, 30])       # shape (3,)
print("A shape:", A.shape)
print("v shape:", v.shape)
print("A + v =\n", A + v)
# v viene replicato per ogni riga


print("\n=== 4) Broadcasting tra matrice e vetore colonna ===")
A = np.array([[1, 2, 3], [4, 5, 6]])
v_col = np.array([[10], [20]])   # shape (2,1)
print("A + v_col =\n", A + v_col)
# v_col viene replicato per colonna


print("\n=== 5) Moltiplicazione matrice × vetore riga ===")
A = np.arange(12).reshape(3, 4)
v = np.array([1, 2, 3, 4])
print("A:\n", A)
print("v:", v)
print("A * v =\n", A * v)
# v scala le colonne


print("\n=== 6) Broadcasting 3D: matrice 2D + vettore 1D ===")
M = np.ones((2, 3, 4))    # shape (2,3,4)
v = np.array([1, 2, 3, 4]) # shape (4,)
print("M shape:", M.shape)
print("v shape:", v.shape)
print("M + v =\n", M + v)
# v viene applicato all'ultima dimensione


print("\n=== 7) Broadcasting per normalizzazione ===")
X = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])
mean = X.mean(axis=0)   # media per colonna
print("Media per colonna:", mean)
print("X normalizzato =\n", X - mean)
# Il vettore media viene sottratto automaticamente a tutte le righe


print("\n=== 8) Broadcasting per distanze euclidee ===")
points = np.array([[0, 0],
                   [1, 0],
                   [0, 1]])
origin = np.array([0, 0])
print("Distanza dei punti dall'origine =", np.sqrt(((points - origin)**2).sum(axis=1)))
# origin shape (2,) viene broadcastato sull'array (3,2)


print("\n=== 9) Broadcasting con maschere booleane ===")
x = np.arange(10)
mask = np.array([True, False, True, False, True, False, True, False, True, False])
# mask shape (10,) → perfetta per x shape (10,)
print("x[mask] =", x[mask])
# Qui non è esattamente broadcasting, ma funziona come selezione vettoriale


print("\n=== 10) Broadcasting con reshape manuale ===")
a = np.arange(4)       # shape (4,)
b = np.arange(3).reshape(3,1)   # shape (3,1)
print("a:", a)
print("b:\n", b)
print("a + b =\n", a + b)
# Forza broadcasting su due dimensioni compatibili

print("\n=== FINE ESEMPI ===\n")

arry = np.array([1,2,3,4])
scalar = 10

result = arry + scalar
print(result)