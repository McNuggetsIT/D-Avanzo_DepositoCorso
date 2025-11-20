from moduli.posto import Posto
from moduli.tipiposto import PostoVip,PostoStandard

class Teatro:
    def __init__(self):
        self._posti = []  # lista di Posto, PostoStandard, PostoVip

    def aggiungi_posto(self, posto):
        self._posti.append(posto)

    def prenota_posto(self, numero, fila, modalita=None):
        for posto in self._posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                if isinstance(posto, PostoStandard):
                    if modalita == "sala":
                        posto.prenota_in_sala()
                    elif modalita == "online":
                        posto.prenota_online()
                    else:
                        print("Modalità non valida per PostoStandard.")
                else:
                    posto.prenota()
                return
        print(f"Nessun posto trovato con numero {numero} e fila {fila}.")

    def stampa_posti_occupati(self):
        print("Posti occupati:")
        for posto in self._posti:
            if posto.is_occupato():
                print(posto)
    