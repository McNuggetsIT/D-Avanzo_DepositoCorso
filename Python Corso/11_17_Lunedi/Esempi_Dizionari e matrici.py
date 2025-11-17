#in py i dizionari sno strutture dati che consentono di memoreizzare coppie di chiavi e valori
#i dizionari sono rappresentati dal tipo di dato dict e sono racchiusi tra parantesi graffe { }

#un dizionare non è assegnato ad un index ma ad una chiave valore

#ESEMPIO

studente = {
    "nome":"Alice",
    "eta": 20,
    "sesso":"Femmina"
}

#possiamo accedere ai valori di un dizionario tramite:
print(studente["nome"])
print(studente["eta"])
print(studente["sesso"])

#per modificarlo si fa cosi:

(studente["eta"]) = 21

#per aggiungere un valore:

(studente["citta"]) = "Roma"

print(studente)

#in py ci sono diversi metodi:

#Keys() ottenere la lista di chiavi TUTTE
#valus() ottenere una lista di tutti i valori
#items() per ottenere una lista di tutte le coppie chiave-valore
#get() per ottenere il valore associato a una chiave senza generare erori riporta solo true o false

print(studente.keys())
print(studente.values())
print("PROVAA")
print(studente.get("citta")) 
print("PROVAA")
print(studente.items())


#Esercizio di prova?
stud_maggiorenne ={
    "nome" : "Mario",
    "eta" : 17,
    "maggiorenne" : False
}

for _ in stud_maggiorenne :
    (stud_maggiorenne["nome"]) = input("Inserisci nuovo nome")
    (stud_maggiorenne["eta"]) =  input("Inserisci eta nuova")
    if stud_maggiorenne["eta"] >= "18":
        stud_maggiorenne["maggiorenne"] = True

print(stud_maggiorenne)

booleano = input("bool")
intero = input("int")
stringa = input("str")


dati2 = {
    "numero" : intero,
    "booleano" : booleano,
    "stringa" : stringa
}

lista = [dati2]

dati = {
    "tipididato": [booleano, intero, stringa],
    "dizionari": lista
}

for x,y in dati2.items():
    print("chiave ", x)
    print("chiave ", y)


# una matrice può essere rappresentata come una lista di liste, in cui ogni lista interna rappresenta una riga della matrice. 
#Questa rappresentazione permette di creare matrici di dimensioni arbitrarie e di accedere agli elementi utilizzando gli indici delle righe e delle colonne

matrice = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#precedente abbiamo creato una matrice 3x3 in cui ogni elemento è un numero intero. 
#Possiamo accedere agli elementi utilizzando gli indici delle righe e delle colonne, come mostrato di seguito:

elemento = matrice[0][1]
print(elemento)

#puoi anche iterare sugli elementi di una matrice utilizzando i cicli for, sia per le righe che per le colonne. Ad esempio:

for riga in matrice:
    for elemento in riga:
        print(elemento)
        
#Questa iterazione stamperebbe tutti gli elementi della matrice uno per uno.