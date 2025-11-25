import numpy as np

base = np.arange(50)
arrcasual = np.random.randint(49,102, size=50)
arrf = np.concatenate((base,arrcasual))
print(arrf)
print(np.shape(arrf))

arrType = arrf.astype(np.float64)
print(arrType.dtype)

arrslice1= arrf[:10]
print("Primi 10",arrslice1)
arrslice2= arrf[:-7]
print("Ultimi",arrslice2)
arrslice3= arrf[5:20]
print("5-20", arrslice3)
arrslice4= arrf[:: 4]
print("Saltelli" ,arrslice4)

arrmodify = arrf.copy()
arrmodify[10:15] = 999


indici = [0,3,7,12,25,33,48]
sindarr = arrf[indici]
print("\nElementi in posizione:\n", indici)

pari = arrf[arrf % 2 == 0]
print("\nElementi pari:\n", pari)

media = arrf.mean()
mdm = arrf[arrf > media]
print(f"\nMedia dell'array: {media:.2f}")
print("Elementi maggiori della media:\n", mdm)