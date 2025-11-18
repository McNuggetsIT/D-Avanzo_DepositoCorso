from moduli.unitamilitare import UnitaMilitare
from moduli.fanteria import Fanteria
from moduli.artiglieria import Artiglieria
from moduli.cavalleria import Cavalleria
from moduli.supportologistico import SupportoLogistico
from moduli.ricognitore import Ricognizione

class ControlloMilitare(UnitaMilitare, Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione):
    def __init__(self, nome, num_soldati, cordinate, velocita, num_materiali, orario, rifornimenti):
        # Attributi comuni e aggregati
        self.nome = nome
        self.num_soldati = num_soldati
        self.cordinate = cordinate
        self.velocita = velocita
        self.num_materiali = num_materiali
        self.orario = orario
        self.rifornimenti = rifornimenti

        # Puoi anche aggiungere un registro interno
        self.unita_registrate = {}

    def registra_unita(self, unita):
        self.unita_registrate[unita.nome] = unita
        print(f"Unità '{unita.nome}' registrata nel comando centrale.")

    def mostra_unita(self):
        if not self.unita_registrate:
            print("Nessuna unità registrata.")
        else:
            print("Unità sotto controllo:")
            for nome in self.unita_registrate:
                print(f"- {nome}")

    def dettagli_unita(self, nome):
        unita = self.unita_registrate.get(nome)
        if unita:
            print(f"Dettagli per '{nome}':")
            print(f"Tipo: {type(unita).__name__}")
            print(f"Soldati: {unita.num_soldati}")
            if hasattr(unita, "cordinate"):
                print(f"Coordinate: {unita.cordinate}")
            if hasattr(unita, "velocita"):
                print(f"Velocità: {unita.velocita}")
            if hasattr(unita, "num_materiali"):
                print(f"Materiali: {unita.num_materiali}")
            if hasattr(unita, "orario"):
                print(f"Orario: {unita.orario}")
            if hasattr(unita, "rifornimenti"):
                print(f"Rifornimenti: {unita.rifornimenti}")
        else:
            print(f"Unità '{nome}' non trovata.")
