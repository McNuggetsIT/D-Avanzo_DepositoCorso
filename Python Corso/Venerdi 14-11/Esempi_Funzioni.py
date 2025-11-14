#Le funzioni in py sono blocchi di codice autonomi che eseguono determinate operazioni
#Le funzioni consentono di organizzare il copdice in unità modulari che possono essere richiamate e riutilizzate in deversi parti di un programma

#Definire una funzione:
#Si definisce con def nome(): all'interno delle () si chiama parametro

#ad esempio: 

def saluta(nome):
    print("Ciao, " , nome)
    
#Chiamate della funzione

#per richiamarla si fa nomeFunzione()
def somma(a, b):
    risultato = a + b
    print("La somma è:", risultato)
    
saluta("alice")
somma(5,3)


#Valore di ritorno;
#Le funzioni possono restituire un valore utilizzano il RETURN
#Puoi specificare tu o se non specifichi nulla il return è NONE di default.

def quadrato(numero):
    return numero * numero

risultato = quadrato(4)
print(risultato)