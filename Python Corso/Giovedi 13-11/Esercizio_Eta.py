"""
Descrizione: Scrivi un programma che chieda all'utente la sua età. Se l'età è inferiore a 18 anni, il programma dovrebbe stampare "Mi dispiace, non puoi vedere questo film".
Altrimenti, dovrebbe stampare "Puoi vedere questo film"."""


controllo = int(input("Scrivi la tua eta"))
if controllo > 18:
    print("puoi vedere questo film")
else:
    print("Non puoi vedere questo film")





"""
Descrizione: Scrivi un programma che chieda all'utente di inserire due numeri e un'operazione da eseguire tra 
addizione (+), sottrazione (-), moltiplicazione (*) e divisione (/). Il programma dovrebbe poi eseguire l'operazione e stampare il risultato.
Tuttavia, se l'utente tenta di dividere per zero, il programma dovrebbe stampare "Errore: Divisione per zero". Se l'operazione inserita non è riconosciuta, dovrebbe stampare "Operazione non valida". """

print("Fai una scelta:\n1: Sottrazione \n2: Addizione \n3: Moltiplicazione \n4: Divisione" )
selection = input("Seleziona un operazione")

list = [10,3,8]

def number_pick(): #Definisco una nuova funzione per evitare di riscrivere 200 volte la stessa cosa
    first_number = input("Inserisci il primo numero: ") #Prendo primo numero
    second_number = input("inserisci il secondo numero: ") #Prendo il secondo
    return first_number, second_number

match selection:
    case "1":
        a,b =  number_pick() #Con A,B prendo il return della funzione di number_pick
        risultato = a - b
        print(risultato)
    case "2":
        a,b =  number_pick()
        risultato = a + b
        print(risultato)
    case "3":
        a,b =  number_pick()
        risultato = a * b
        print(risultato)
    case "4":
        a,b =  number_pick()
        if a or b != 0:
            risultato = a / b
            print(risultato)
        else:
            print("errore")
            
    case "5":   #Boh ho fatto questo credo che sia questo?
        somma = list[0] + list[1] + list[2]
        prodotto = list[0] * list[1] * list[2]
        sottrazione = list[0] - list[1] - list[2]
        divisione = list[0] / list[1] / list[2]
        
    case _:
        print("Errore")
        
#Gestire il calcolo di piu fattori tramite una lista