utenti = {
    "giuseppe": {"password": "12345"},
    "maria": {"password": "abcde"}
}

# Menu
print("Fai una scelta:\nA: Login \nB: Registra un nuovo utente \nC: Modifica un utente")
comando = input("Inserisci la tua scelta!").lower()

match comando:
    case "a":  # LOGIN
        id = input("Inserisci nome utente: ").lower()
        pws = input("Inserisci password: ")
        
        # Controllo se l'utente esiste e la password sia corretta
        if id not in utenti or utenti[id]["password"] != pws:
            print("Utente non esiste o password errata")
        else:
            print("Accesso riuscito")

    case "b":  # REGISTRAZIONE NUOVO UTENTE
        new_username = input("Inserisci username: ").lower()
        new_password = input("Inserisci password: ")
        
        # Controllo se l'utente esiste
        if new_username in utenti:
            print("Utente già presente")
        else:
            utenti[new_username] = {"password": new_password}
            print("Nuovo utente aggiunto")
        print(utenti)

    case "c":  # MODIFICA UTENTE
        username = input("Scegli chi vuoi modificare: ").lower()
        if username in utenti:
            scelta = input("Scegli cosa modificare (A:ID, B:PW): ").lower()
            
            if scelta == "a":  # Modifica ID
                new_username = input("Inserisci un nuovo id: ").lower()
                utenti[new_username] = utenti.pop(username)
                print(f"Username '{username}' cambiato in '{new_username}'")
            
            elif scelta == "b":  # Modifica Password
                new_password = input("Inserisci nuova password: ")
                utenti[username]["password"] = new_password
                print(f"Password di '{username}' aggiornata")
        else:
            print("Utente non trovato")

    case _:  # SCELTA NON VALIDA
        print("Comando non riconosciuto.")
