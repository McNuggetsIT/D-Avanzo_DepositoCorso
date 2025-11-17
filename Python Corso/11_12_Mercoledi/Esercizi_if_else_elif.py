#1 Creare una serie di condizioni una dentro l'altra che a fronte di un input per ogni if decidano se farti passare o no ( 3 livelli, fate un paragone con == )

username = input("Inserisci il tuo username: ")

if username == "giuseppe":
    password = input("Inserisci la password: ")
    
    if password == "12345":
        ruolo = input("Sei studente o professore? ")
        
        if ruolo == "studente": 
            print("Accesso consentito ✅ Benvenuto studente!")
        else:
            print("Accesso negato  Ruolo non autorizzato")
    else:
        print("Accesso negato  Password errata")
else:
    print("Accesso negato  Username non valido")


#2 Andare a creare un if con vari elif e un else finale che gestica un menu con la selezione di un crud basilare 



print("A- Aggiungi un nome")
print("B- trova una persona")
print("C- rinomina una persona")
print("D- elimina una persona")

scelta = input("Scegli un opzione: ")

if scelta == str("a"):
    nome = input("Scrivi un nome")
    print(nome)
elif scelta == str("b"):
    print("Persona trovata")
elif scelta == str("c"):
    print("persona rinominata")
elif scelta == str("d"):
    print("persona eliminata")
else:
    print("ERRORE")
    
    



#3 Creare un if con esle semplice, dentro l'if inserire una struttura di creazuone di dati ( nome,password,id dato dal sistema a crescere) 
# e nell'else il controllo automatico la dove è presente l'account nel sistema e solo se si passa dall'else conludere lo script

persona = {"nome": "Giuseppe", "password":"giuseppe44"}


