class ContoBancario:
    def __init__(self, titolare, saldo):
        self.__titolare = titolare
        self.__saldo = saldo
        
    def get_saldo(self):
        return self.__saldo
    
    def get_titolare(self):
        return self.__titolare
    
    def get_titolare(self):
        return self.__titolare
    
    def set_titolare(self, nuovo_titolare):
        if nuovo_titolare and nuovo_titolare.strip():
            self.__titolare = nuovo_titolare
        else:
            print("Titolare non valido")
            
    def set_saldo(self,nuovo_saldo):
        pass
        

cb = ContoBancario("Giuseppe",100)

def deposita():
    
    while True:
        titolare = cb.get_titolare()
        
        importo = int(input("Quanto vuoi depositare? "))

        if importo > 0:
            nuovo_saldo = cb.get_saldo() + importo
            cb.set_saldo(nuovo_saldo)
            print(f"Deposito effettuato. Nuovo saldo: {nuovo_saldo}€")
            break
        elif importo <= 0:
            print("Importo non valido inserisci un valore da 1+€")
        else:
            print("Errore inserisci un valore valdido da 1+€")
        
        
def preleva():
    while True:
        importo = int(input("Quanto vuoi prelevare?"))
        
        if importo > 0 & importo < cb.get_saldo():
            nuovo_saldo = cb.get_saldo() - importo
            print(f"Prelievo effettuato. Nuovo saldo: {nuovo_saldo}€")
            break
        elif importo <= 0:
            print("Importo non valido inserisci un valore da 1+€")
        else:
            print("Errore inserisci un valore valdido da 1+€")
            
def visualiza_saldo():
    return cb.get_saldo()
        
print("===MENU===")
print("Fai una scelta:")
print("1:Deposita")
print("2:Preleva")
print("3:Visualizza")

scelta = input("Fai una scelta")

match scelta:
    case "1":
        deposita()
    case "2":
        pass
    case "3":
        pass
    case _:
        print("Errore scelta")
