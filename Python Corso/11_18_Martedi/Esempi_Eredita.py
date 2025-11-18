# Metodi dell'Ereditarietà in Python

# L'ereditarietà permette a una classe (sottoclasse) di ereditare attributi e metodi
# da un'altra classe (superclasse). Ecco i principali strumenti:

# 1. super():
#    - Richiama il costruttore o i metodi della superclasse.
#    - Utile per estendere o modificare il comportamento della superclasse.

# 2. Sovrascrittura di metodi:
#    - La sottoclasse può ridefinire metodi della superclasse.
#    - Serve per personalizzare il comportamento ereditato.

# 3. Ereditarietà Multipla:
#    - Una classe può ereditare da più superclassi.
#    - Si specificano tutte le classi base tra parentesi nella definizione.

class Animale:
    def __init__(self,nome):
        self.nome = nome
    
    def parla(self):
        print(f"{self.nome} fa suono generico")

        #classe cane CHE EREDITA DA CHI?? (ANIMALE)
class Cane(Animale):
    def parla(self):
        print(f"{self.nome} abbaia!")
        
class Lupo(Animale):
    def parla(self):
        print(f"{self.nome} ulula")
        
animale_generico = Animale("AnimaleGenerico")
lupo = Lupo("Lupetto")
cane = Cane("Fido")

animale_generico.parla()
lupo.parla()
cane.parla()