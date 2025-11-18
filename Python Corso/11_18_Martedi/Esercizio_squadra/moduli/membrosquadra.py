class MembroSquadra:
    #creo un init come "base per le altre classi"
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        #metodo descrivi
        
    def descrivi(self):
        return (f"Il suo nome è: {self.nome} e ha {self.eta} anni")