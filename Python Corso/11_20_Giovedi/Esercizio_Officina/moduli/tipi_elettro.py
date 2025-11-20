import random
from moduli.elettrodomestico import Elettrodomestico

class Lavatrice(Elettrodomestico):
    def __init__(self,marca, modello, anno, guasto,capacita_kg, giri_centrfuga):
        super().__init__(marca, modello, anno, guasto)
        self.capkg = capacita_kg
        self.gir_cent = giri_centrfuga
        
    def stima_costo_base(self):
        if self._capkg > 3:
            return random.randint(200,300)
        
class Forno(Elettrodomestico):
    def __init__(self, marca, modello, anno, guasto, tipo_alimentazione, ha_ventilato):
        super().__init__(marca, modello, anno, guasto)
        self.tipo_alimentazione = tipo_alimentazione
        self.ha_ventilato = ha_ventilato

    def stima_costo_base(self):
        base = random.randint(70, 120)
        if self.tipo_alimentazione == "gas":
            base += 20
        if self.ha_ventilato:
            base += 30
        return base
    
class Frigorifero(Elettrodomestico):
    def __init__(self, marca, modello, anno, guasto, litri, ha_freezer):
        super().__init__(marca, modello, anno, guasto)
        self.litri = litri
        self.ha_freezer = ha_freezer

    def stima_costo_base(self):
        base = random.randint(80, 150)
        if self.ha_freezer:
            base += 50
        if self.litri > 300:
            base += 30
        return base