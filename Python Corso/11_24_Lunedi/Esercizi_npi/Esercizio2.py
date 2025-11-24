# Esercizio 2 – Slicing e Fancy Indexing
#
# Consegna:
# 1. Crea una matrice NumPy 2D di dimensioni 6x6 contenente numeri interi casuali tra 1 e 100.
# 2. Estrai la sotto-matrice centrale 4x4 dalla matrice originale.
# 3. Inverti le righe della matrice estratta (la prima diventa l’ultima, la seconda la penultima, ecc.).
# 4. Estrai la diagonale principale della matrice invertita e crea un array 1D con questi elementi.
# 5. Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1.
# 6. Stampa:
#    - la matrice originale
#    - la sotto-matrice centrale estratta
#    - la matrice invertita
#    - la diagonale principale
#    - la matrice invertita modificata
# Esercizio 2 – Slicing e Fancy Indexing
#
# Obiettivo:
# Esercitarsi con slicing e fancy indexing in NumPy per manipolare matrici 2D.

import numpy as np
mat2d = np.random.randint(1, 101, size=(6, 6))
print(mat2d)

mat4x4= mat2d[1:5 ,1:5 ]
print(mat4x4)

mat_inver = mat4x4[::-1, :]

print("\nMatrice invertita (righe invertite):\n", mat_inver)

mat_diago = np.diag(mat_inver)
mat_diag_pring = np.diag(mat2d)
print("Matrice principale:\n", mat_diag_pring)
print("Matrice invertita:\n", mat_diago)

