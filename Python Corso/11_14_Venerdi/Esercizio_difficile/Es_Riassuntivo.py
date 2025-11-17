#Hai 60 min per creare un esercizio che rappresenti tutto quello che 
#hai imparato nella settimana precedente, riprendi la tabella delle conoscenze per maggiori info.

#Da fare: Gestione profilo utente
# lista utenti: nome eta ecc
# step 2 funzioni 
# step 3 decoratori

#Lista delle mie persone
persone = [
    ("Luca", "Rossi", 28),
    ("Giulia", "Bianchi", 34),
    ("Marco", "Verdi", 19),
    ("Sara", "Neri", 45),
    ("Davide", "Gallo", 22),
    ("Elena", "Fontana", 31),
    ("Francesco", "Russo", 17),
    ("Alice", "Ferrari", 26),
    ("Matteo", "Costa", 40),
    ("Chiara", "Romano", 23)
]

#Qui sfrutto una funzione per stampare le persone
def stampa_persone(persone):
    for nome, cognome, eta in persone:
        print(f"Nome: {nome:<10} Cognome: {cognome:<10} Età: {eta}")

#Qui sfrutto una funzione per cercare una persona
def find_person(nome_cercato):
    for persona in persone:
        if persona[0].lower() == nome_cercato.lower():
            return persona
    return "persona non trovata"

#Qui sfrutto una funzione per aggiungere una persona
def add_person():
    new_name = input("Inserisci nome: ").lower()
    new_surname = input("Inserisci cognome: ").lower()
    new_age = input("Inserisci l'età: ")
    
    new_person = (new_name, new_surname, new_age)
    
    if new_person in persone:
        print("Persona già esistente")
    else:
        persone.append(new_person)
    print(persone)

#Qui sfrutto una funzione per modificare una persona    
def modify_person():
    stampa_persone(persone)
    persona = input("Scegli chi modificare").lower()
    if persona in persone:
        scelta = input("Cosa vuoi modificare? A: Nome B: Cognome : C Eta").lower()
        
        if scelta == "a":
            new_name = input("Scegli nuovo nome: ").lower()
            persone[new_name] = persone.pop(persona)
            print(f"Nome '{persona}' cambiato in '{new_name}'")
        if scelta == "b":
            new_surname = input("Scegli nuovo cognome: ").lower()
            persone[new_surname] = persone.pop(persona)
            print(f"Cognome '{persona}' cambiato in '{new_surname}'")
        if scelta == "c":
            new_age = int(input("Scegli la nuova età: "))
            persone[new_age] = persone.pop(persona)
            print(f"Nome '{persona}' cambiato in '{new_age}'")
        else:
            print("Persona non trovata")    

#Qui sfrutto una funzione per eliminare una persona    
def delete_person(nome_cercato):
    stampa_persone(persone)
    for persona in persone:
        if persona[0].lower() == nome_cercato():
            persone.remove(nome_cercato)
            print(f"{nome_cercato} eliminato con successo")
            return
    return "Persona non trovata"

print("Fai una scelta:  \n1: Cerca persona  \n2: Aggiungi una persona \n3: Modifica una persona  \n5: Elimina una persona")

scelta = input("Scegli cosa vuoi fare digitando un numero: ")

#Menu per la scelta del crud
match scelta :
    case "1":
        trovapersona= find_person(input("Scrivi chi vuoi cercare: "))
        print(trovapersona)
    case "2":
        add_person()
    case "3":
        modify_person()
    case "4":
        nome = input("Chi vuoi eliminare?")
        delete_person(nome)
    case _:
        print("ERRORE")
    
        