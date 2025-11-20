from moduli.posto import Posto
from moduli.tipiposto import PostoVip, PostoStandard
from moduli.teatro import Teatro


def main():
    teatro = Teatro()

    # Aggiungo alcuni posti di esempio
    teatro.aggiungi_posto(PostoVip(1, "A"))
    teatro.aggiungi_posto(PostoVip(2, "A"))
    teatro.aggiungi_posto(PostoStandard(3, "B", 12.0))
    teatro.aggiungi_posto(PostoStandard(4, "B", 15.0))

    while True:
        print("\n--- MENU TEATRO ---")
        print("1. Prenota un posto")
        print("2. Stampa posti occupati")
        print("3. Esci")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            print()
            fila = input("Inserisci la fila (es. A o B): ").upper()
            numero = int(input("Inserisci il numero del posto: "))

            # Controllo se è un PostoStandard per chiedere la modalità
            modalita = None
            for posto in teatro._posti:
                if posto.get_numero() == numero and posto.get_fila() == fila:
                    if isinstance(posto, PostoStandard):
                        modalita = input("Vuoi prenotare 'sala' o 'online'? ").lower()
                    break

            teatro.prenota_posto(numero, fila, modalita)

        elif scelta == "2":
            teatro.stampa_posti_occupati()

        elif scelta == "3":
            print("Uscita dal programma. A presto 👋")
            break

        else:
            print("Scelta non valida, riprova!")

if __name__ == "__main__":
    main()
