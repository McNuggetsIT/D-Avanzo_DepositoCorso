from moduli.controllomilitare import ControlloMilitare
from moduli.artiglieria import Artiglieria
from moduli.cavalleria import Cavalleria
from moduli.fanteria import Fanteria
from moduli.ricognitore import Ricognizione
from moduli.supportologistico import SupportoLogistico

def main():
    # Istanza del centro di comando
    comando = ControlloMilitare()

    # Creazione delle unità
    art = Artiglieria("Cannone Bravo", 15, "0N, 0E")
    cav = Cavalleria("Cavalleria Alfa", 20, 60)
    fan = Fanteria("Fanteria Delta", 30, 25)
    ric = Ricognizione("Scout Echo", 10, "notte")
    log = SupportoLogistico("Convoglio Zulu", 5, 20)

    # Registrazione delle unità
    comando.registra_unita(art)
    comando.registra_unita(cav)
    comando.registra_unita(fan)
    comando.registra_unita(ric)
    comando.registra_unita(log)

    print("\n--- Elenco unità ---")
    comando.mostra_unita()

    print("\n--- Dettagli unità specifica ---")
    comando.dettagli_unita("Fanteria Delta")

if __name__ == "__main__":
    main()
