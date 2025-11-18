from moduli.unitamilitare import UnitaMilitare
import random
class Artiglieria(UnitaMilitare):
    def __init__(self,nome,num_soldati,cordinate):
        self.nome = nome
        self.num_soldati = num_soldati
        self.cordinate = cordinate
    
    
    def calibra_artiglieria(self, distanza, angolo):
        self.cordinate = f"{distanza * 0.5}N, {angolo * 0.3}E"
    
    def spara(self):
        colpiti = random.randint(1, 100)
        morti = random.randint(0,colpiti)
        self.cordinate = f"colpiti: {colpiti}, morti: {morti}"
        
    