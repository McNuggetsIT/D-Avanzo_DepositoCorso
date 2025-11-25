#Crea un array utilizzando linespace, cambiala sua forma con reshape
#genera un array casuale e calcola la somma degli elementi

import numpy as np

arr = np.linspace(0,1,12)
matrice = arr.reshape(3,4)

matrice2 = np.random.randint(0,2,size=(3,4))

sum = np.sum(matrice)
sum2 = np.sum(matrice2)

print(arr)
print(matrice)
print(matrice2)
print(sum)
print(sum2)