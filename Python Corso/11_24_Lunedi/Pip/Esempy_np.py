import numpy as np
num = "1,2,3,4,5,6,7,8,9,10"
print(np.array([1, 2, 3]) + 1)

# Keyword base di NumPy:
# - ndarray: array multidimensionale, più veloce ed efficiente delle liste Python.
# - dtype: tipo di dato degli elementi (int, float, bool, ecc.).
# - shape: dimensioni dell'array, es. (3, 4) per 3 righe e 4 colonne.
# - arange: crea array con valori sequenziali, simile a range().
# - reshape: cambia la shape dell'array senza alterare i dati.
# - linspace: genera valori equamente distribuiti tra due estremi.
# - random: modulo per array casuali (uniformi, normali, ecc.).
# - sum, mean, std: somma, media e deviazione standard degli elementi.

#NDARRAY

#Creazione di un array unidimensionale
arr2 = np.array([1,2,3,4,5])
arr = np.array([[1,2,3], [4,5,6]])
#Creazione di un array bidimensionale


#è possibile creare un array con array, np.zeros() , np.ones() , np.arrange(), e np.linspace()

# Utilizzo di alcuni metodi
print("Forma dell'array:", arr.shape) # Output: (5,)
print("Dimensioni dell'array:", arr.ndim) # Output: 1
print("Tipo di dati:", arr.dtype) # Output: int64 (varia a seconda della piattaforma)
print("Numero di elementi:", arr.size) # Output: 5
print("Somma degli elementi:", arr.sum()) # Output: 15
print("Media degli elementi:", arr.mean()) # Output: 3.0
print("Valore massimo:", arr.max()) # Output: 5
print("Indice del valore massimo:", arr.argmax()) # Output: 4

#dtype
arr3= np.array([1,2,3], dtype ="int32")
print(arr3.dtype)

#shape
arr4= np.array([[1,2,3],[4,5,6]])
print(arr4.shape)

#arange

arr5= np.arange(10)
print(arr5)

#reshape

arr6 = np.arange(6)
reshaped_arr = arr6.reshape((2,3))
print(reshaped_arr) 


#Indexing e Slicing

#Esempio:

arr7= np.array([1,2,3,4,5])
#Indexing
print(arr7[0])

#Slicing
print(arr7[1:3])
print(arr7[3:5])

#Boolean Indexing
print(arr7[arr7 > 3])

arr_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

#Slicing sulle righe
print("Slice riga")
print(arr_2d[1:3]) #Output [(5 6 7 8) (9 10 11 12)]
print("Slice colonna")
print(arr_2d[:, 1:3]) #Output [[2 3] [6 7] [10 11]]
print("Slice misto")
print(arr_2d[1:, 1:3]) #Output [[6 7] [10 11]]

# Slicing in NumPy:
# È una tecnica per estrarre una parte di un array o sequenza.
# Simile allo slicing delle liste Python, ma più potente e versatile.
# Permette di ottenere subarray senza copiare i dati, migliorando l'efficienza in memoria.
#
# Sintassi base: array[start:stop:step]
# - start: indice di inizio (inclusivo), default = 0
# - stop: indice di fine (esclusivo), default = dimensione dell'array
# - step: passo tra gli elementi, default = 1


import numpy as np

# Array di base
arr8 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Slicing di base: da indice 2 a 6 (stop escluso)
print("arr[2:7] →", arr8[2:7])  # [2 3 4 5 6]

# Slicing con passo: da 1 a 7 con step 2
print("arr[1:8:2] →", arr8[1:8:2])  # [1 3 5 7]

# Omettere start e stop
print("arr[:5] →", arr8[:5])    # [0 1 2 3 4]
print("arr[5:] →", arr8[5:])    # [5 6 7 8 9]

# Indici negativi
print("arr[-5:] →", arr8[-5:])  # [5 6 7 8 9]
print("arr[:-5] →", arr8[:-5])  # [0 1 2 3 4]


# Fancy Indexing in NumPy:
# È una tecnica che permette di selezionare elementi da un array usando array o liste di indici interi.
# A differenza dello slicing, che seleziona intervalli regolari, la fancy indexing consente selezioni non contigue e personalizzate.
# Utile per estrarre elementi specifici, riorganizzare dati o applicare filtri complessi.

# Array di base
arr9 = np.array([10, 20, 30, 40, 50])

# Fancy indexing con array di indici
indices_array = np.array([1, 3])
print("arr[indices_array] →", arr9[indices_array])  # [20 40]

# Fancy indexing con lista di indici
indices_list = [0, 2, 4]
print("arr[indices_list] →", arr9[indices_list])    # [10 30 50]

# Differenze tra Slicing e Fancy Indexing in NumPy:
#
# Slicing:
# - Seleziona intervalli regolari (rettangolari) di elementi.
# - Restituisce una *vista* dell'array originale (non crea una copia).
# - Usa la sintassi array[start:stop:step].
#
# Fancy Indexing:
# - Permette selezioni non contigue e in ordine arbitrario.
# - Restituisce sempre una *copia* dei dati selezionati.
# - Usa array o liste di indici interi per accedere agli elementi.

