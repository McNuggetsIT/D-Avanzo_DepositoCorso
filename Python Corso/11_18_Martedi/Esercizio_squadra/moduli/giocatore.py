from moduli.membrosquadra import MembroSquadra

class Giocatore(MembroSquadra):
    
    def __init__(self, nome, ruolo, eta, numero_maglia):
        self.nome = nome
        self.ruolo = ruolo
        self.eta = eta
        self.numero_maglia = numero_maglia
        
    def gioca_partita(self):
        return (f"Il giocatore {self.nome} con il numero {self.numero_maglia} che gioca nel ruolo di {self.ruolo} e ha {self.eta}anni sta giocando una partita eccezzionale ")
    