import random
# ================================
# 📘 Esercizi - Sezione "Def"
# ================================

# 1. Esercizio Base: Indovina il numero
# Descrizione: Scrivi un programma che genera un numero casuale tra 1 e 100 (inclusi).
# L'utente deve indovinare quale numero è stato generato.
# Dopo ogni tentativo, il programma dovrebbe dire all'utente se il numero da indovinare
# è più alto o più basso rispetto al numero inserito.
# Il gioco termina quando l'utente indovina il numero o decide di uscire.

def checknum(x,y):
    if x == y:
        print("Congratulazioni hai vinto!!")
    elif x > y:
        print("Il numero è troppo alto!")
    else:
        print("Il numero è troppo basso")

def fibonaccisequence(limite):
    x, y = 0, 1
    while x <= limite:
        print(x, end= " ")
        x, y = y, x + y


numToFind = random.randint(1, 100)
numTry = None

while numTry != numToFind:
    numTry = int(input("Prova a indovinare il numero da (1-100): "))
    checknum(numTry , numToFind)

# 2. Esercizio Avanzato: Sequenza di Fibonacci fino a N
# Descrizione: Chiedi all'utente di inserire un numero N.
# Il programma dovrebbe stampare la sequenza di Fibonacci fino a N.
# Ad esempio, se l'utente inserisce 100, il programma dovrebbe stampare
# tutti i numeri della sequenza di Fibonacci minori o uguali a 100.

numFibo = int(input("inserisci un numero: "))
fibonaccisequence(numFibo)