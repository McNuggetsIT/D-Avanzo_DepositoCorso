#La funzione linspace genera un array di numeri equidistanti tra un valore iniziale e uno finale.
import numpy as np
arr = np.linspace(0, 1, 5)
print(arr)  # Output: [0.   0.25  0.5  0.75  1.  ]

#Il modulo random di NumPy permette di generare array di numeri casuali.

random_arr = np.random.rand(3, 3)
# Matrice 3x3 con valori casuali uniformi tra 0 e 1
print(random_arr)

# sum, mean, std:
# NumPy fornisce diverse funzioni per eseguire operazioni matematiche sugli array.

# Esempio:
arr = np.array([1, 2, 3, 4, 5])

sum_value = np.sum(arr)          # Somma degli elementi → Output: 15
mean_value = np.mean(arr)        # Media degli elementi → Output: 3.0
std_value = np.std(arr)          # Deviazione standard → Output: 1.4142135623730951

print("Sum:", sum_value)
print("Mean:", mean_value)
print("Standard Deviation:", std_value)


