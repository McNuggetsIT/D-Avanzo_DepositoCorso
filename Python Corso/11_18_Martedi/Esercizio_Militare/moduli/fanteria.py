from moduli.unitamilitare import UnitaMilitare
class Fanteria(UnitaMilitare):
    def __init__(self,nome,num_soldati,num_materiali):
        self.nome = nome
        self.num_soldati = num_soldati
        self.num_materiali = num_materiali
        
def costruisci_trincea(self):
    # Controllo che ci siano sia materiali che soldati disponibili
    if self.num_materiali > 0 and self.num_soldati > 0:
        mats_usati = min(5, self.num_materiali)       # massimo 5 materiali usati
        soldati_impegnati = min(3, self.num_soldati)  # massimo 3 soldati impegnati
        
        # Aggiorna le risorse
        self.num_materiali -= mats_usati
        self.num_soldati -= soldati_impegnati
        
        return (f"La fanteria {self.nome} ha costruito una trincea usando "
                f"{mats_usati} materiali e {soldati_impegnati} soldati. "
                f"Materiali rimasti: {self.num_materiali}, Soldati disponibili: {self.num_soldati}")
    else:
        return (f"La fanteria {self.nome} non ha abbastanza risorse per costruire una trincea.")
    