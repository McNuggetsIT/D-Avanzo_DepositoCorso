from moduli.unitamilitare import UnitaMilitare
import random
class Cavalleria(UnitaMilitare):
    def __init__(self,nome,num_soldati,velocita):
        self.nome = nome
        self.num_soldati = num_soldati
        self.velocita = velocita
    
    def esplora_terreno(self):
        pick_terreno= random.randint(1,3)
        pick_velocita= random.randint(20,50)
        
        match pick_terreno:
            case "1":
                print(f"La cavalleria {self.nome} sta esplorando un terreno montuoso: difficile da attraversare, ma ottimo per imboscata alla velocita di {pick_velocita} km orari ")
            case "2":
                print(f"La cavalleria {self.nome} sta esplorando una pianura: terreno aperto, perfetto per una carica veloce alla velocità di {pick_velocita} di km orari")
            case "3":
                print(f"La cavalleria {self.nome} sta esplorando una foresta: terreno fitto, visibilità ridotta ma copertura naturale. alla velocità di {pick_velocita} di km orari")