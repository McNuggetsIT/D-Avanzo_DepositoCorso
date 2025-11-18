class UnitaMilitare:
    def __init__(self, nome, num_soldati):
        self.nome = nome
        self.num_soldati = num_soldati
    
    def muovi(self, direzione):
        return f"L'unità {self.nome} si muove verso {direzione} con {self.num_soldati} soldati."
    
    def attacca(self, bersaglio):
        return f"L'unità {self.nome} attacca il bersaglio {bersaglio} con {self.num_soldati} soldati."
    
    def ritira(self):
        return f"L'unità {self.nome} si ritira per riorganizzarsi."

