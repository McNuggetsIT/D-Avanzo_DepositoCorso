from moduli.metodopagamento import MetodoPagamento

class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di €{importo:.2f} effettuato con {self._nome}.")

class PayPal(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di €{importo:.2f} effettuato con {self._nome}.")

class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di €{importo:.2f} effettuato con {self._nome}.")