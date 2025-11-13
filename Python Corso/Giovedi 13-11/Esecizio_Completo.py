# Esercizio completo – Cicli e Condizioni in Python

# Punto 1: Utilizzo di if
# Scrivi un programma che prende in input un numero e stampa "Pari" se il numero è pari,
# oppure "Dispari" se il numero è dispari.

num = int(input("Scrivi un numero: "))
if num % 2 == 0:
    print("Pari")
else:
    print("Dispari")

print("PROSIMO ESERCIZIO!")
# Punto 2: Utilizzo di while e range
# Scrivi un programma che prende in input un numero intero positivo n
# e stampa tutti i numeri da n a 0 (compreso), decrementando di 1.
# Il programma deve potersi ripetere all’infinito.

check_while = True
while check_while == True:
    for i in range(num,-1,-1):
        print(i)
        if i == 0:
            check = input("Vuoi continuare?").lower()
            if check == "no":
                check_while = False
                
print("PROSIMO ESERCIZIO")

# Punto 3: Utilizzo di for
# Scrivi un programma che prende in input una lista di numeri
# e stampa il quadrato di ciascun numero nella lista.

lista_numeri = []
lista_numeri_quadrato = []
check_while_listanumeri = True
while check_while_listanumeri == True:
    numero = int(input("Scrivi un numero da aggiungere alla lista: "))
    lista_numeri.append(numero)
    check2 = input("Vuoi continuare ad aggiungere? si/no").lower()
    if check2 == "no":
        check_while_listanumeri = False
        for i in lista_numeri:
            quadrato = i * i
            lista_numeri_quadrato.append(quadrato)
print(lista_numeri)
print(lista_numeri_quadrato)

print("PROSIMO ESERCIZIO")

# Punto 4: Utilizzo di if, while e for insieme
# Scrivi un programma che prende in input una lista di numeri interi
# che precedentemente è stata valorizzata dall’utente.
# Il programma deve:
# 1. Usare un ciclo for per trovare il numero massimo nella lista.
# 2. Usare un ciclo while per contare quanti numeri ci sono nella lista.
# 3. Usare una condizione if per stampare "Lista Vuota" se la lista è vuota,
#    altrimenti stampare il numero massimo trovato e il numero di elementi presenti.

numList_4 = []
checkTrue = True
numMax = 0
numAlto = 0
while checkTrue == True:
    nume4 = int(input("Scrivi un numero"))
    numList_4.append(nume4)
    checkFalse = input("Continuare s/n").lower()
    if checkFalse == "n":
        checkTrue = False
        if len(numList_4) == 0:
            print("Lista vuota ERRORE")
        else:
            for i in numList_4:
                numMax = numMax +1
                if i > numAlto:
                    numAlto = i
print("il numero piu alto è " + str(numAlto) + "\nInvece il numero di elementi dentro alla lista è pari a: " + str(numMax))

            



