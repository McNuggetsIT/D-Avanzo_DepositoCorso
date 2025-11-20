class MetodoPagamento:
    def __init__(self,nome):
        self._nome = nome
        
    def effettua_pagamento(self,importo):
        print(f"[Base] Pagamento di €{importo:.2f} con metodo generico: {self.nome}")
    