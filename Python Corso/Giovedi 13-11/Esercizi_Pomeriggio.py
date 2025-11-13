# 1. Livello Base – Numeri pari e dispari o sequenza
# Scrivi un programma che chiede all’utente di scegliere se inserire un numero o una stringa.
# Se è un numero, determina se è pari o dispari e stampa il risultato.
# Se stringa contare le lettere
# Poi chiedi se deve ripetere o stampare e poi ripetere.

# ==========================
# ESERCIZIO 1 – Uso di isinstance()
# ==========================

check = True

while check:
    textOrNum = input("Inserisci un numero o una stringa: ")

    try:
        # Provo a convertire l'input in numero intero
        numero = int(textOrNum)
        
        if isinstance(numero, int):
            if numero % 2 == 0:
                print("Pari")
            else:
                print("Dispari")

    except ValueError:
        #Lo uso come try catch ( se mi da errore sopra e non trasforma in int va sotto)
        # Se non è convertibile in int, rimane una stringa
        #So che non servirebbe fare istance anche sotto ma troppo pigro a pensare ad altro 
        #o toglierlo
        if isinstance(textOrNum, str):
            print("La stringa ha", len(textOrNum), "caratteri")

    scelta = input("Vuoi ripetere? (s/n): ").lower()
    if scelta != "s":
        check = False

# 2. Livello Intermedio – Numeri primi in un intervallo
# Chiedi all’utente di inserire due numeri che definiscono un intervallo (es. 10 e 50).
# Il programma deve stampare tutti i numeri primi compresi in quell’intervallo,
# oppure i non primi, oppure entrambi (a scelta).
# Salva i risultati in due gruppi separati.
# Alla fine chiedi se deve ripetere.

check2 = True
primeList = []
while check2 == True:
    number1 = int(input("Inserisci primo numero "))
    number2 = int(input("Inserisci secondo numero "))
    
    number1, number2 = sorted([number1, number2])
    

    # ciclo principale che scorre tutti i numeri nell'intervallo
    for i in range(number1 , number2, +1):
        if i > 1:
            # controllo se il numero ha divisori fino alla radice quadrata
            for y in range(2, int(i**0.5), 1):
                if i % y == 0:
                    break
                else:
                    primeList.append(i)
    print("numeri primi trovati: ", primeList)
    
    scelta = input("Vuoi continuare? s/n: ").lower()
    if scelta != "s":
        check2 = False


# 3. Livello Avanzato – Fattori comuni
# Chiedi all’utente di inserire due numeri.
# Il programma deve stampare i fattori comuni.
# Se l’unico fattore comune è 1, stampa “I numeri sono coprimi”.
# Fai lo stesso anche per due stringhe:
# confronta se sono “complementari”, cioè se hanno tutte le lettere in comune (es. "abs" e "sab").
# Alla fine chiedi se deve ripetere.
