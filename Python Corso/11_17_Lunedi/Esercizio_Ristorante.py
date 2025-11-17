class Ristorante:
    
    
    #Da finire (Parecchio complicato)
    
    def __init__(self,nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
    
    def apri(self):
        self.aperto = True
        
    def chiudi_ristorante(self):
        self.aperto = False
    
    menu = [
        {"piatto" : "spaghetti col sugo","prezzo" : 12},
        {"piatto" : "pasta col sugo","prezzo" : 12},
        {"piatto" : "lasagna col sugo","prezzo" : 12}
    ]
    
    def descrivi_ristorante(self):
        return f"Il miglior ristorante di {self.tipo_cucina} è {self.nome}"
    
    def stato_apertura(self):
        if self.aperto == True:
            print(f"Il ristorante {self.nome} è aperto")
        else:
            print(f"Il ristorante {self.nome} è chiuso")
    
    def aggiungi_al_menu(self):
        nome = input("Scrivi nome del piatto")
        prezzo = int(input("Scrivi che prezzo"))
        
        (self.menu["nome"]) = nome
        (self.prezzo["prezzo"]) = prezzo
        
    def togli_dal_menu(self):
        nome_piatto = input("Scrivi che piatto eliminare: ")
        self.menu.pop(nome_piatto)
    
    def stampa_menu(self):
        print(self.menu)
        
ristorante1 = Ristorante("la grande mela", "americana")
ristorante2 = Ristorante("la zucca ubriaca", "algerina")
ristorante3 = Ristorante("cacio e pepe", "italiana")

ristoranti = {
    ristorante1.nome: ristorante1,
    ristorante2.nome: ristorante2,
    ristorante3.nome: ristorante3
}

print("1:Descrivi ristorante")
print("2: Stato Apertura")
print("3:Apri o chiudi ristorante")
print("4: Aggiungi o rimuovi un piatto al menu")
print("5: Stampa menu")

scelta = input("Scegli cosa vuoi fare: ")

match scelta:
    case "1":
        scelta_ristorante = input("Scegli nome del ristorante o del tipo di cucina: ")
        
        rist = ristoranti.get(scelta_ristorante)
        if not rist:
            for ristorante in ristoranti.values():
                if ristorante.tipo_cucina.lower() == scelta_ristorante.lower():
                    rist = ristorante
        if rist:
            print(rist.descrivi_ristorante())
            scelta = False
            
    case "2":
        scelta_ristorante = input("Scegli nome del ristorante: ").lower()
        
        rist = ristoranti.get(scelta_ristorante)
        if rist:
            print(rist.stato_apertura())
        else:
            print("non trovato")
        
    case "3":
        scelta_ristorante = input("Scegli nome del ristorante: ").lower()
        apri_chiudi = input("Vuoi aprire o chiudere A/C? ").lower()
        
        rist = ristoranti.get(scelta_ristorante)
        if apri_chiudi == "a":
            rist.apert = True
            print(f"Il ristorante {rist.nome} è ora aperto.")
        else:
            rist.aperto = False
            print(f"Il ristorante {rist.nome} è ora chiuso.")
    case "4":
        scelta = input("Scegli se vuoi aggiungere o togliere un piatto A/G").lower()
        if scelta == "a":
            Ristorante.aggiungi_al_menu()
        else:
            Ristorante.togli_dal_menu()
        
    case "5":
        pass
    case _:
        print("errore")