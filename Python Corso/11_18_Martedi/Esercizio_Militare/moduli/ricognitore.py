from moduli.unitamilitare import UnitaMilitare
import random
class Ricognizione(UnitaMilitare):
    def __init__(self,nome,num_soldati,orario):
        self.nome = nome
        self.num_soldati = num_soldati
        self.orario = orario
    
class Ricognizione(UnitaMilitare):
    def __init__(self, nome, num_soldati, orario):
        self.nome = nome
        self.num_soldati = num_soldati
        self.orario = orario
    
    def conduci_ricognizione(self):

        pick_orario = random.choice(["mattina", "giorno", "notte"])
        
        match pick_orario:
            case "mattina":
                nemici_visti = random.choice([True, False])
                allertati = random.choice([True, False])
                return (f"Ricognizione mattutina: "
                        f"Nemici visti: {nemici_visti}, Nemici allertati: {allertati}")
            
            case "giorno":
                nemici_visti = random.choice([True, False])
                allertati = random.choice([True, False])
                return (f"Ricognizione diurna: "
                        f"Nemici visti: {nemici_visti}, Nemici allertati: {allertati}")
            
            case "notte":
                nemici_visti = random.choice([True, False])
                allertati = random.choice([True, False])
                return (f"Ricognizione notturna: "
                        f"Nemici visti: {nemici_visti}, Nemici allertati: {allertati}")
        