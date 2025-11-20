from moduli.metodopagamento import MetodoPagamento
from moduli.paymentmodes import CartaDiCredito,PayPal,BonificoBancario
from moduli.gestorepagamenti import GestorePagamenti

if __name__ == "__main__":
    gestore = GestorePagamenti()

    print("=== Sistema Pagamenti ===")
    print("1. Carta di Credito")
    print("2. PayPal")
    print("3. Bonifico Bancario")

    scelta = input("Scegli il metodo di pagamento (1-3): ")
    importo = float(input("Inserisci l'importo da pagare: "))

    if scelta == "1":
        metodo = CartaDiCredito("Carta di Credito")
    elif scelta == "2":
        metodo = PayPal("PayPal")
    elif scelta == "3":
        metodo = BonificoBancario("Bonifico Bancario")
    else:
        metodo = MetodoPagamento("Generico")

    gestore.paga(metodo, importo)