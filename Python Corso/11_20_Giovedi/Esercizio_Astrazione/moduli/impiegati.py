from moduli.impiegato import Impiegato

class ImpiegatoFisso(Impiegato):
    
    def calcolo_stipendio(self):
        return self.stip_b

class ImpiegatoAProvvigione(Impiegato):
    def __init__(self, nome, cognome, stipendio_base, vendite):
        super().__init__(nome,cognome,stipendio_base)
        self.vendite = vendite
        self.nome = nome
        self.cognome = cognome
        self.stip_b = stipendio_base
    
    def calcolo_stipendio(self):
        return self.stip_b + self.vendite