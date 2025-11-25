#Es 1
import numpy as np
arr = np.random.randint(1,101,15)

sum = np.sum(arr)
media = np.mean(arr)

print("arr: ", arr)
print("Sum: ", sum)
print("media: ", media)

print("-------------------------------ESERCIZIO 2-----------------------------------------------")
#Es2
arr2 = np.arange(1, 26).reshape(5,5)
print(arr2)
print("------------------------------------------------------------------------------")
print(arr2[1:2])
print("------------------------------------------------------------------------------")
print(arr2[2:3])
print("------------------------------------------------------------------------------")
diag = np.diag(arr2)
print(diag)
#Es3
print("-------------------------------ESERCIZIO 3-----------------------------------------------")
arr3 = np.random.randint(10,50 , size=(4,4))
print(arr3)
print("------------------------------------------------------------------------------")
indici = [[0,1],[1,3],[2,2],[3,0]]

righe, colonne = zip(*indici)
indix = arr3[np.array(righe),np.array(colonne)]
print(indix)
print("------------------------------------------------------------------------------")

even = arr3[1::2]
print(even)

print("------------------------------------------------------------------------------")
arr3[np.array(righe), np.array(colonne)] += 10
