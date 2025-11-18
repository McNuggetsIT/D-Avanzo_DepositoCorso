from moduli.membrosquadra import MembroSquadra

class Assistente(MembroSquadra):
    #nuovo init ocn nuovi attributi come special
    def __init__(self, nome, eta, special):
        self.nome = nome
        self.eta = eta
        self.special = special
        
    def supporta_team(self):
        return (f"L'assistente {self.nome} sta assistendo al squadra come {self.special}")