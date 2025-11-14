#Hai 60 min per creare un esercizio che rappresenti tutto quello che 
#hai imparato nella settimana precedente, riprendi la tabella delle conoscenze per maggiori info.

#Da fare: Gestione profilo utente
# lista utenti: nome eta ecc
# step 2 funzioni 
# step 3 decoratori

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

def find_person(nome_cercato):
    for persona in persone:
        if persona[0].lower() == nome_cercato.lower():
            return persona
    return "persona non trovata"

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
    
def delete_person(nome_cercato):    
        for persona in persone:
            if persona[0].lower() == nome_cercato():
                persona.remove(nome_cercato)
        return "Persona non trovata"        
def modify_person():
    
print("Fai una scelta:  \n1: Cerca persona  \n2: Aggiungi una persona \n3: Modifica una persona  \n5: Elimina una persona")

scelta = input("Scegli cosa vuoi fare digitando un numero: ")
match scelta :
    case "1":
        trovapersona= find_person(input("Scrivi chi vuoi cercare: "))
        print(trovapersona)
    case "2":
        add_person()
    case "3":
        pass
    case "4":
        pass
    case _:
        print("ERRORE")
    
        