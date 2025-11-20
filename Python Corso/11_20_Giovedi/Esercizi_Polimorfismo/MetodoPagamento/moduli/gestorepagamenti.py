from moduli.metodopagamento import MetodoPagamento
class GestorePagamenti:
    def paga(self, metodo: MetodoPagamento, importo):
        metodo.effettua_pagamento(importo)