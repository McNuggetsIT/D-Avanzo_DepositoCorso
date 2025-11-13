#ESERCIZIO:
#chiedi utente  di inserire un numero. il programma deve quindi fare un conto alla rovescia a partire da quel numero fino a zero. stampa ogni numero e chiedi se ripetere o no

num = int(input("Seleziona un numero: "))

check = True
while check:
    for i in range(num, -1, -1):
        print(i)

    # chiedi se ripetere alla fine del countdown
    blocco = input("Vuoi ripetere? (si/no): ").lower()
    if blocco == "si":
        
        # se vuole ripetere, chiedi un nuovo numero
        num = int(input("Seleziona un nuovo numero: "))
    else:
        check = False
        print("Programma terminato.")
            
    
    


#Chiedi all utente di inserire un numero. il programma dovrebbe controllare se il numero inserito è pari o dispari. Se è primo lo salva e stampa il numero è primo
#stampa è primo. Altrimenti stampa il numero non è primo. si ferma il tutto quando ha 5 numeri primi

def is_prime(x):
    if x < 2:  # 0 e 1 non sono primi
        return False
    for i in range(2, int(x**0.5) + 1):  # controllo fino alla radice quadrata
        if x % i == 0:
            return False
    return True

numeri_primi = []

# Il ciclo for con range(5) garantisce che raccogliamo 5 numeri primi
for _ in range(5):
    while True:  # continua finché non inserisci un numero primo
        numero = int(input("Inserisci un numero: "))

        # Controllo pari/dispari
        if numero % 2 == 0:
            print("Il numero è pari")
        else:
            print("Il numero è dispari")

        # Controllo se è primo
        if is_prime(numero):
            numeri_primi.append(numero)
            print("Il numero è primo")
            break  # esci dal while e passa al prossimo giro del for
        else:
            print("Il numero non è primo, riprova")

print("Hai inserito 5 numeri primi:", numeri_primi)

    