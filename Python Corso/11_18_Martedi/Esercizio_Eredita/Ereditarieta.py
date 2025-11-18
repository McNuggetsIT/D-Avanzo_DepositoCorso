# Classe base Animale
class Animale:
    def __init__(self, nome, eta):       # Costruttore corretto (__init__)
        self.nome = nome                 # Nome dell'animale
        self.eta = eta                   # Età dell'animale
        
    def fai_suono(self):                 # Metodo generico
        print(f"{self.nome} fa suono generico")
        

# Classe Leone che eredita da Animale
class Leone(Animale):
    def fai_suono(self):                 # Sovrascrive il metodo fai_suono
        print(f"{self.nome} ruggisce")
    def caccia(self):                    # Metodo specifico del Leone
        print(f"{self.nome} sta cacciando")
    def putEta(self):
        print(f"Il {self.nome} ha {self.eta} anni")
        

# Classe Giraffa che eredita da Animale
class Giraffa(Animale):
    def fai_suono(self):                 # Sovrascrive il metodo fai_suono
        print(f"{self.nome} nitrisce")
    def mangia(self):                    # Metodo specifico della Giraffa
        print(f"{self.nome} sta mangiando le foglie su un albero")
    def putEta(self):
        print(f"Il {self.nome} ha {self.eta} anni")


# Classe Pinguino che eredita da Animale
class Pinguino(Animale):
    def fai_suono(self):                 # Sovrascrive il metodo fai_suono
        print(f"{self.nome} fa un suono gutturale")
    def scivola(self):                   # Metodo specifico del Pinguino
        print(f"{self.nome} sta scivolando sulla pancia")
    def putEta(self):
        print(f"Il {self.nome} ha {self.eta} anni")


# Creazione delle istanze
pingu = Pinguino("Gino il pinguino", 3)
leone = Leone("Mufasa", 5)
giraffa = Giraffa("Giro la giraffa", 7)

# Uso dei metodi
pingu.fai_suono()
pingu.scivola()
pingu.putEta()
print("--------------------------------------")
leone.fai_suono()
leone.caccia()
leone.putEta()
print("--------------------------------------")
giraffa.fai_suono()
giraffa.mangia()
giraffa.putEta()
