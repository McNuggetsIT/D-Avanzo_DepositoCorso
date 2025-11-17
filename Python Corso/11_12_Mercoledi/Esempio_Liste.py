#Le liste in py sono strutture date con elementi e son modificabili

numeri = [1,2,3,4,5]
nomi = ["Alice", "Bob","Charlie"]
misto = [1, "due", True, 4.5]



#e si può accedere agli elementi in questo modo:

numeri = [1,2,3,4,5]
print(numeri[0])
print(numeri[1])
print(numeri[2])
print(numeri[3])
print(numeri[4])

#Py fornisce una varietà di metodi tipo len() per ottenere la lunghezza , append() per aggiungere un elemento , insert() per un elemento di una posizione specifica, remove() per rimuovere 
# e sort() per ordinare la lista

numeri = [3, 1, 4, 2, 5]
print(len(numeri))
numeri.append(6)
print(numeri) 
numeri.insert(2, 10)
print(numeri) 
numeri.remove(4)
print(numeri) 
numeri.sort()
print(numeri)

