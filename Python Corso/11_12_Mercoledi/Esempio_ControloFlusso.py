#Flusso e condizionamenti

#if si esegue solo se uan condizione è vera o soddisfatta

numero = int(input("inserisci un numero:"))
if numero > 0:
    print("il nhumero è positivo")
    
#if - else !! Se la condizione è vera fai X altrimenti fai Y
if numero < 5:
    print("il numero è positivo - Blocco True")
else:
    print("Il numero è negativo - Blocco ELSE")
    
#if - else - elif 


if numero > 0:
    print("il numero è positivo")
    if numero == 100:
        print("wow")
elif numero < 0:
    print("il numero è negativo")
else:
    print("il Numero è zero")
    
#Match serve per confrontare un valore con un pattern riprende lo switch case di java
#match comando = Python valuta il cvalore della varaibile comando

comando = input("Inserisci un comando")

match comando:
    case "start":
        print("Avvio del programma.")
    case "stop":
        print("Chiusura del programma.")
    case "pausa":
        print("Programma in pausa.")
    case _:
        print("Comando non riconosciuto.")