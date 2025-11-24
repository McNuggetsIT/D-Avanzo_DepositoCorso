# Esercizio: Slicing con NumPy
#
# Obiettivo:
# Esercitarsi nell'utilizzo dello slicing per estrarre e modificare sottoarray da un array NumPy.
#
# Consegna:
# 1. Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.
# 2. Estrai i primi 10 elementi dell'array.
# 3. Estrai gli ultimi 5 elementi dell'array.
# 4. Estrai gli elementi dall'indice 5 all'indice 15 (escluso).
# 5. Estrai ogni terzo elemento dell'array.
# 6. Modifica gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
# 7. Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing.
import numpy as np

arr = np.random.randint(10, 51, size=20)
print(f"Prind base: {arr}"
      )
arr_slice = arr[:10]
print("\nPrimi 10 elementi:\n", arr_slice)

arr_slice_last = arr[-5:]
print("\nUltimi 5 elementi:\n", arr_slice_last)

arr_slice_4 = arr[5:15]
print("\nTra 5 e 15 :\n", arr_slice_4)

arr_mult3 = arr[::3]
print("\n 3,3,3 :\n", arr_mult3)

arrLine = arr[5:10] = 99
print("\nArray modificato (indici 5 9 = 99):\n", arr)

