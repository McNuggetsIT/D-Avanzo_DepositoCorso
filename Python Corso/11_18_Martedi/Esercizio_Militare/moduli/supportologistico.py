import random
from moduli.unitamilitare import UnitaMilitare

class SupportoLogistico(UnitaMilitare):
    def __init__(self, nome, num_soldati, rifornimenti):
        self.nome = nome
        self.num_soldati = num_soldati
        self.rifornimenti = rifornimenti
        
    def rifornisci_unita(self, unita_destinataria):

        if self.rifornimenti > 0:
            inviati = min(random.randint(1, 5), self.rifornimenti)
            self.rifornimenti -= inviati
            unita_destinataria.rifornimenti += inviati
            
            return (f"Il supporto logistico {self.nome} ha inviato {inviati} rifornimenti "
                    f"all'unità {unita_destinataria.nome}. "
                    f"Rifornimenti rimasti: {self.rifornimenti}")
        else:
            return (f"Il supporto logistico {self.nome} non ha più rifornimenti disponibili.")
