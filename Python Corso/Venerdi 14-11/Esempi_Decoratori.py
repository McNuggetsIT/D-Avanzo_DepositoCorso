#i decoratori sono un funzione che modifica di comportamento di un altra funzione.
#il metodo senza modificarne direttamente il codice

#si utilizza spesso per aggiungere funzionalità extra come logging.

def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione della funzione")
        funzione()                      #qui vien sostituoto dal @decoratore sotto
        print("Dopo l'esecuzione della funzione")
    return wrapper #SEMPRE

@decoratore
def salutano():
    print("Ciao")

salutano()


#un wrapper(decoratore)è una funzione interna definita all'interno di un decoratore che avvolge la funzione originale pemettendo di aggiungere funzionalità extra prima o dopo l'esecuzone della 
#funzione decorata senza alterare il codice direttamente.

def decoratore_con_argomenti(func):
    def wrapper(*args,**kwargs):
        print("prima")
        risultato=func(*args,**kwargs)
        print("dopo")
        return risultato
    return wrapper

@decoratore_con_argomenti
def somma(a, b):
    print(a+b)
    return a+b

print("risultato è " , somma(3,4))

# • Funzioni come oggetti di prima classe:
#   In Python, le funzioni sono oggetti di prima classe.
#   Possono essere passate come argomenti, restituite da altre funzioni o assegnate a variabili.

# • Funzioni annidate:
#   I decoratori usano spesso funzioni definite dentro altre funzioni
#   per aggiungere comportamento prima o dopo l'esecuzione della funzione decorata.

# • Restituzione di una funzione modificata:
#   Un decoratore restituisce una nuova funzione che sostituisce quella originale,
#   modificandone il comportamento senza toccare il codice originale.

# • Uso di *args e **kwargs:
#   Permettono al decoratore di funzionare con qualsiasi funzione,
#   indipendentemente dal numero e tipo di parametri.

# • Sintassi @decoratore:
#   È una scorciatoia per scrivere: funzione = decoratore(funzione)
#   Si mette sopra la definizione della funzione da decorare.
