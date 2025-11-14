# 1. Ciclo while
# Scrivi un programma che chiede all’utente di inserire numeri interi.
# Continua finché l’utente non inserisce 0.
# Alla fine, calcola e stampa la somma di tutti i numeri inseriti.

numList = []
totale = 0

check = True
while check == True:
    numero = int(input("Scrivi dei numeri e per concludere la tua selezione inserisci 0: "))
    if numero != 0:
        numList.append(numero)
    else:
        for numero in numList:
            totale += numero
        print(totale)
        break
    


# 2. Ciclo for
# Scrivi un programma che chiede all’utente una parola.
# Usa un ciclo for per stampare ogni lettera della parola su una nuova riga.

frase = input("Scrivi una parola o frase: ")
for char in frase:
    print(char)



# 3. Ciclo for con range
# Scrivi un programma che chiede all’utente un numero massimo N e uno step.
# Usa un ciclo for con range per stampare i numeri da 0 a N con lo step indicato.

numero = int(input("Scrivi un numero"))
numeroStop = int(input("Scrivi quanti step"))
stepNumero = int(input("Scrivi un numero per cui il tuo numero base deve fare uno step in avanti"))
    
for i in range(numero, numeroStop +1 ,stepNumero):
    print(i)
    