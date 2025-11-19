from moduli.veicolo import Veicolo

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, num_porte, alimentazione, colore):
        super().__init__(marca, modello, anno)
        self._num_porte = num_porte
        self._alimentazione = alimentazione
        self._colore = colore

    def suona_clacson(self):
        print("Beep beep!")

    def cambia_colore(self, nuovo_colore):
        self._colore = nuovo_colore
        print(f"Colore cambiato in {nuovo_colore}")

    def info_alimentazione(self):
        print(f"Alimentazione: {self._alimentazione}")

    def __str__(self):
        return f"{self._marca} {self._modello} ({self._anno}) - {self._num_porte} porte, {self._alimentazione}, {self._colore}"



class Furgone(Veicolo):
    def __init__(self, marca, modello, anno, num_porte, cap_carico, altezza, lunghezza):
        super().__init__(marca, modello, anno)
        self._num_porte = num_porte
        self._cap_carico = cap_carico
        self._altezza = altezza
        self._lunghezza = lunghezza
        self._carico_attuale = 0

    def carica(self, peso):
        if self._carico_attuale + peso <= self._cap_carico:
            self._carico_attuale += peso
            print(f"Caricati {peso} kg. Totale: {self._carico_attuale} kg")
        else:
            print("Capacità di carico superata!")

    def scarica(self, peso):
        if peso <= self._carico_attuale:
            self._carico_attuale -= peso
            print(f"Scaricati {peso} kg. Totale: {self._carico_attuale} kg")
        else:
            print("Non hai così tanto carico da scaricare!")

    def stato_carico(self):
        print(f"Carico attuale: {self._carico_attuale}/{self._cap_carico} kg")

    def __str__(self):
        return f"{self._marca} {self._modello} ({self._anno}) - {self._cap_carico}kg, {self._num_porte} porte"



class Motocicletta(Veicolo):
    def __init__(self, marca, modello, anno, tipo, cilindrata, colore):
        super().__init__(marca, modello, anno)
        self._tipo = tipo
        self._cilindrata = cilindrata
        self._colore = colore

    def esegui_wheelie(self):
        print("La motocicletta fa un'impennata!")

    def cambia_colore(self, nuovo_colore):
        self._colore = nuovo_colore
        print(f"Colore cambiato in {nuovo_colore}")

    def info_cilindrata(self):
        print(f"Cilindrata: {self._cilindrata} cc")

    def __str__(self):
        return f"{self._marca} {self._modello} ({self._anno}) - {self._tipo}, {self._cilindrata}cc, {self._colore}"

