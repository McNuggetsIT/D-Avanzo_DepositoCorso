#Classi in py
#in py le classi sono fondamentali per programmazzione orientata agli oggetti (oop)
#Le classi consentono di definire strutture che raggruppano dati (attributi) e comportamenti (metodi) correlati in un unico oggetto di un determinato tipo.

#le classi sono un astrazione dei concetti.
#in py una classe è un modello per la crazione di oggetti
#un oggetto è instanza di una classe , cioè una copia univoca della classe e delle sue proprietà
#le classi sono definite da una parola chiave class seguita dal nome
#le classi possono contenere metodi e attributi

#Gli attributi sono variabili associate ad una classe
#rappresentano le proprietà di un oggetto
#gli attr di classe sono condivisi tra tutte le istanze della classe.

#I metodi sono funzioni associate a una classe.
#I metodi rappresentano il comportamento di un oggetto.

#Creazione di una classe:

class Automobile:
    numero_di_ruote = 4
    
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
    
    def stampa_info(self):
        print("l'automobileè una", self.marca, self.modello)
        
#Creazione di oggetti da una classe
#AUTO1 Sarebbe il self.
auto1 = Automobile("Fiat","500")
auto2 = Automobile("BMW","X3")

auto1.stampa_info()
auto2.stampa_info()

print(auto1) #<__main__.Automobile object at 0x00000272D0C36A50> Stampa questo

class Persona:
    #Rappresenta una persona come nome ed eta
    
    #il metodo str restituisce una stringa descrittiva dell'oggetto.
    #COSTRUTTORE:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        
        #Metodo di stampa
    def __str__(self):
        return f"Persona(nome={self.nome}, eta={self.eta})"
    

#il costruttore è un metodo speciale che viene invocato automaticamente al momento della crazione:
#in py il costruttore è rappresentato da __init__


#I metodi: sono funzioni definite all'interno di una classe che operano sugli oggetti(le istanze) della classe stessa.

#Tipi di metodi:
#- Metodi di istanza:
# Operano su un'istanza specifica e accedono ai dati dell'oggetto tramite self.

class Persona2:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    # metodo di istanza
    def saluta(self):
        return f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni."

p1 = Persona("Luca", 28)
print(p1.saluta())  # Ciao, mi chiamo Luca e ho 28 anni.


#- Metodi di classe:
# Operano sulla classe non specifica. SOno definiti come il decoratore @classmethod e ricevono come primo parametro la classe (cls)

class Persona3:
    popolazione = 0

    def __init__(self, nome):
        self.nome = nome
        Persona.popolazione += 1

    @classmethod
    def conta_persone(cls):
        return f"Ci sono {cls.popolazione} persone create."

p1 = Persona("Luca")
p2 = Persona("Giulia")
print(Persona.conta_persone())  # Ci sono 2 persone create.


#- Metodi statici:
#Funzioni legate alla classe ma non operano ne sull'istanza ne sulla classe. Sono definiti con il decoratre @staticmethod

class Calcolatrice:
    @staticmethod
    def somma(a, b):
        return a + b

print(Calcolatrice.somma(3, 5))  # 8
