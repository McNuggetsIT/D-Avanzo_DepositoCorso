# Importiamo le classi dai moduli
# Qui diciamo a Python: "vai nella cartella moduli e prendi le classi"
from moduli.giocatore import Giocatore
from moduli.assistente import Assistente
from moduli.allenatore import Allenatore

def main():
    # Creazione degli oggetti della squadra
    # Ogni classe eredita da MembroSquadra e aggiunge metodi specifici
    giocatore = Giocatore("Giovanni", "Attaccante", 25, 9)
    assistente = Assistente("Marco", 40, "Preparatore atletico")
    allenatore = Allenatore("Carlo", 55, "10 anni di esperienza")

    # Stampa informazioni sul giocatore
    print("=== Squadra di calcio ===")
    print(giocatore.descrivi())          # Metodo ereditato da MembroSquadra
    print(giocatore.gioca_partita())     # Metodo specifico di Giocatore
    print("--------------------------------------")

    # Stampa informazioni sull'assistente
    print(assistente.descrivi())         # Metodo ereditato da MembroSquadra
    print(assistente.supporta_team())    # Metodo specifico di Assistente
    print("--------------------------------------")

    # Stampa informazioni sull'allenatore
    print(allenatore.descrivi())         # Metodo ereditato da MembroSquadra
    print(allenatore.dirige_allenamento())  # Metodo specifico di Allenatore

if __name__ == "__main__":
    main()
