# Esercizio: Polimorfismo con metodi di pagamento
# 1. Creare una classe base MetodoPagamento con il metodo effettua_pagamento(importo)
#    → Ogni sottoclasse dovrà implementare questo metodo.
#
# 2. Creare le sottoclassi:
#    - CartaDiCredito: simula pagamento con carta
#    - PayPal: simula pagamento tramite PayPal
#    - BonificoBancario: simula pagamento con bonifico
#
# 3. Creare la classe GestorePagamenti
#    → Usa un'istanza di MetodoPagamento per effettuare il pagamento
#    → Non si preoccupa del tipo specifico: sfrutta il polimorfismo
