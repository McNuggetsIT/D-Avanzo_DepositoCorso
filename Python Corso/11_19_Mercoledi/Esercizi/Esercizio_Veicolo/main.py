from moduli.derivati import Auto, Furgone, Motocicletta
from moduli.gestparco import GestoreParcoVeicoli

def main():
    gpv = GestoreParcoVeicoli()

    while True:
        print("\n--- MENU PRINCIPALE ---")
        print("1. Aggiungi veicolo")
        print("2. Lista veicoli")
        print("3. Rimuovi veicolo")
        print("0. Esci")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            print("\nChe tipo di veicolo vuoi aggiungere?")
            print("1: Auto")
            print("2: Furgone")
            print("3: Motocicletta")
            tipo = input("Scelta: ")

            marca = input("Marca: ")
            modello = input("Modello: ")
            anno = int(input("Anno: "))

            if tipo == "1":
                num_porte = int(input("Numero porte: "))
                alimentazione = input("Alimentazione: ")
                colore = input("Colore: ")
                veicolo = Auto(marca, modello, anno, num_porte, alimentazione, colore)

            elif tipo == "2":
                num_porte = int(input("Numero porte: "))
                cap_carico = int(input("Capacità di carico (kg): "))
                altezza = float(input("Altezza vano (m): "))
                lunghezza = float(input("Lunghezza vano (m): "))
                veicolo = Furgone(marca, modello, anno, num_porte, cap_carico, altezza, lunghezza)

            elif tipo == "3":
                tipo_moto = input("Tipo (sportiva, naked, touring...): ")
                cilindrata = int(input("Cilindrata (cc): "))
                colore = input("Colore: ")
                veicolo = Motocicletta(marca, modello, anno, tipo_moto, cilindrata, colore)

            else:
                print("Tipo non valido.")
                continue

            gpv.aggiungi_veicolo(veicolo)
            print("Veicolo aggiunto con successo!")

        elif scelta == "2":
            veicoli = gpv.lista_veicoli()
            if not veicoli:
                print("Nessun veicolo nel parco.")
            else:
                print("\n--- Veicoli nel parco ---")
                for v in veicoli:
                    print("-", v)

        elif scelta == "3":
            marca = input("Inserisci la marca del veicolo da rimuovere: ")
            modello = input("Inserisci il modello del veicolo da rimuovere: ")
            gpv.rimuovi_veicolo(modello, marca)

        elif scelta == "0":
            print("Chiusura programma...")
            break

        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()
