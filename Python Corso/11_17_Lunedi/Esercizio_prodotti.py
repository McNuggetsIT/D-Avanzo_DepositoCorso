class Prodotto:
    
    
    #La mia difficoltà è stata il fatto proprio capire come scrivere e tipo: self.inventario[nome][quantita] ecc 
    #Mi son aiutato per finire l'esercizio
    
    def __init__(self,nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        
    def calcola_profitto(self):
        profitto = self.prezzo_vendita - self.costo_produzione
        return profitto
    
class Elettronica:
    
    def __init__(self, tipo,costo_produzione, prezzo_vendita, marca, garanzia):
        self.tipo = tipo
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.marca = marca
        self.garanzia = garanzia
        
    def calcola_profitto(self):
        profitto = self.prezzo_vendita - self.costo_produzione
        return profitto
        
class Abbigliamento:
    
    def __init__(self, tipo,costo_produzione, prezzo_vendita, marca, tipo_tessuto):
        self.tipo = tipo
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.marca = marca
        self.tipo_tessuto = tipo_tessuto
        
    def calcola_profitto(self):
        profitto = self.prezzo_vendita - self.costo_produzione
        return profitto
        
class Fabbrica:
    
    def __init__(self):
        
        self.inventario = {}
        
    def aggiungi_prodotto(self, prodotto, quantita):
        nome = prodotto.nome
        if nome in self.inventario:
           self.inventario[nome]["quantità"] += quantita
        else:
            self.inventario[nome] = {
                "oggetto":prodotto,
                "quantita":quantita
            }
            
            print(f"Aggiunti {quantita} pezzi di {nome} all'inventario.")
    
    def vendi_prodotto(self, nome):
        if nome in self.inventario and self.inventario[nome]["quantita"] > 0:
            self.inventario[nome]["quantita"] -= 1
            profitto = Prodotto.calcola_profitto()
            print(f"Venduto {nome}. Profitto: €{profitto}")
        else:
            print(f"{nome} non disponibile o esaurito.")
    
    def resi_prodotto(self, nome):
        if nome in self.inventario:
            self.inventario[nome]["quantita"] += 1

    def mostra_inventario(self):
        print("\nInventario attuale:")  
        for nome, dati in self.inventario.items():
            print(f"- {nome}: {dati['quantita']} pezzi")
            
p1 = Prodotto("Borsa", 20, 50)
e1 = Elettronica("Smartphone", 200, 400, "Samsung", "2 anni")
a1 = Abbigliamento("Maglietta", 10, 25, "Nike", "Cotone")

fab = Fabbrica()

while True:
    print("\n--- MENU FABBRICA ---")
    print("1. Aggiungi prodotto")
    print("2. Vendi prodotto")
    print("3. Reso prodotto")
    print("4. Mostra inventario")
    print("0. Esci")

    scelta = input("Scegli un'opzione: ")
    
    if scelta == "1":
        print("Prodotti disponibili:")
        print("1. Borsa")
        print("2. Smartphone")
        print("3. Maglietta")
        tipo = input("Quale prodotto vuoi aggiungere? (1/2/3): ")
        qta = int(input("Quanti pezzi vuoi aggiungere?: "))
        if tipo == "1":
            fab.aggiungi_prodotto(p1,qta)
        elif tipo == "2":
            fab.aggiungi_prodotto(e1,qta)
        elif tipo == "3":
            fab.aggiungi_prodotto(a1,qta)
        else:
            print("Errore")
    elif scelta == "2":
        nome = input("Scrivi il nome del prodotto da vendere: ")
        fab.vendi_prodotto(nome)
    elif scelta == "3":
        nome = input("Scrivi che prodotto far il reso: ")
        fab.resi_prodotto(nome)
    elif scelta == "4":
        fab.mostra_inventario()