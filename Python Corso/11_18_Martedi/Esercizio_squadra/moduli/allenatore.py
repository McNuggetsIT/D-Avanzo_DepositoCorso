from moduli.membrosquadra import MembroSquadra

class Allenatore(MembroSquadra):
     #nuovo init ocn nuovi attributi come anni esperienza (an_es)
    def __init__(self, nome, eta, an_es):
        self.nome = nome
        self.eta = eta
        self.an_es = an_es
    
    def dirige_allenamento(self):
        return (f"{self.nome} sta dirigendo un allenamento")
    
        