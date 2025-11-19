from moduli.persona import Persona
from moduli.studente import Studente
from moduli.professore import Professore

def main():

    studenti = [
        Studente("Luca Bianchi", 20, {"italiano": [7, 8, 6], "matematica": [5, 6, 7]}),
        Studente("Anna Verdi", 22, {"italiano": [9, 8, 10], "storia": [7, 6, 8]}),
    ]
    professori = [
        Professore("Mario Rossi", 50, "Matematica"),
        Professore("Giovanna Neri", 45, "Italiano"),
    ]

    while True:
        print("\n--- MENU PRINCIPALE ---")
        print("1. Mostra Studenti")
        print("2. Mostra Professori")
        print("3. Calcola media di uno studente")
        print("4. Aggiungi Studente")
        print("5. Aggiungi Professore")
        print("0. Esci")

        scelta = input("Seleziona un'opzione: ").strip()

        if scelta == "1":
            if not studenti:
                print("Nessuno studente registrato.")
            else:
                print("Studenti registrati:")
                for stud in studenti:
                    stud.presentazione()

        elif scelta == "2":
            if not professori:
                print("Nessun professore registrato.")
            else:
                print("Professori registrati:")
                for prof in professori:
                    prof.presentazione()

        elif scelta == "3":
            if not studenti:
                print("Nessuno studente registrato.")
                continue

            print("Studenti registrati:")
            for stud in studenti:
                print("-", stud.get_nome())

            nome_input = input("Inserisci il nome (anche parziale): ").strip().lower()
            materia = input("Inserisci la materia: ").strip().lower()

            trovato = False
            for stud in studenti:
                if nome_input in stud.get_nome().lower():
                    print(stud.calcola_media(materia))
                    trovato = True
                    break

            if not trovato:
                print("Studente non trovato.")

        elif scelta == "4":
            nome = input("Nome studente: ").strip()
            try:
                eta = int(input("Età studente: ").strip())
            except ValueError:
                print("Età non valida.")
                continue

            voti = {}
            while True:
                materia = input("Inserisci materia (X per terminare): ").strip().lower()
                if materia == "x":
                    break
                if not materia:
                    print("Materia non valida.")
                    continue
                voti[materia] = []
                while True:
                    voto_str = input(f"Inserisci voto per {materia} (X per terminare): ").strip().lower()
                    if voto_str == "x":
                        break
                    try:
                        voto = int(voto_str)
                        if 1 <= voto <= 10:
                            voti[materia].append(voto)
                        else:
                            print("Il voto deve essere tra 1 e 10.")
                    except ValueError:
                        print("Inserisci un numero valido.")
            studenti.append(Studente(nome, eta, voti))
            print("Studente aggiunto.")

        elif scelta == "5":
            nome = input("Nome professore: ").strip()
            try:
                eta = int(input("Età professore: ").strip())
            except ValueError:
                print("Età non valida.")
                continue
            materia = input("Materia insegnata: ").strip()
            professori.append(Professore(nome, eta, materia))
            print("Professore aggiunto.")

        elif scelta == "0":
            print("Chiusura programma...")
            break

        else:
            print("Scelta non valida, riprova.")

if __name__ == "__main__":
    main()
