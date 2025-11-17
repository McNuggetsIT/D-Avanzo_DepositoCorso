import random

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
        

def ripeti(funzione):
    def wrapper(*args, **kwargs):
        continua = "si"
        while continua.lower() == "si":
            funzione(*args, **kwargs)   # esegue la funzione originale
            continua = input("Vuoi continuare? (si/no): ")
        print("Hai scelto di terminare. Fine del programma.")
    return wrapper

# ================================
# 📘 Esercizi - Sezione "Def"
# ================================

# 1. Esercizio Base: Indovina il numero
# Descrizione: Scrivi un programma che genera un numero casuale tra 1 e 100 (inclusi).
# L'utente deve indovinare quale numero è stato generato.
# Dopo ogni tentativo, il programma dovrebbe dire all'utente se il numero da indovinare
# è più alto o più basso rispetto al numero inserito.
# Il gioco termina quando l'utente indovina il numero o decide di uscire.


@ripeti
def find_num ():
    num_ToFind = random.randint(1, 100)
    num_Try = None   

    while num_Try != num_ToFind:
        num_Try = int(input("Prova a indovinare il numero da (1-100): "))
        checknum(num_Try , num_ToFind)
        if num_Try == 101:
            break
find_num()

# 2. Esercizio Avanzato: Sequenza di Fibonacci fino a N
# Descrizione: Chiedi all'utente di inserire un numero N.
# Il programma dovrebbe stampare la sequenza di Fibonacci fino a N.
# Ad esempio, se l'utente inserisce 100, il programma dovrebbe stampare
# tutti i numeri della sequenza di Fibonacci minori o uguali a 100.

@ripeti
def esegui_fibonacci():
    numfibo = int(input("inserisci un numero: "))
    fibonaccisequence(numfibo)

esegui_fibonacci()