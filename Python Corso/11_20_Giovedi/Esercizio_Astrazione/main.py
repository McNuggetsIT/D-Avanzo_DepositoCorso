from moduli.impiegati import ImpiegatoFisso, ImpiegatoAProvvigione
from moduli.impiegato import Impiegato

def main():
    imp1 = ImpiegatoFisso("Mario", "Rossi", 1500)
    imp2 = ImpiegatoAProvvigione("Luca", "Bianchi", 1200, 500)
    imp3 = ImpiegatoAProvvigione("Giuseppe", "Verdi", 1000, 800)

    imp1.stampa_info()
    imp2.stampa_info()
    imp3.stampa_info()

if __name__ == "__main__":
    main()