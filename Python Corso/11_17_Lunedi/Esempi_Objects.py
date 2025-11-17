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
# ============================================================
# Riepilogo: Tipi di metodi nelle classi Python
# ============================================================

# @staticmethod
# - Funziona come una funzione ordinaria, ma è definita all'interno della classe.
# - Non accede né a self né a cls.
# - Utile per raggruppare funzioni di utilità logicamente collegate alla classe.

# @classmethod
# - Riceve la classe (cls) come primo parametro.
# - Può modificare gli attributi di classe.
# - Spesso usato per creare metodi factory.
# - Utile per gestire comportamenti legati alla classe e sfruttare il polimorfismo.

# Metodo di istanza (senza decoratore)
# - Definito senza decoratori particolari.
# - Riceve come primo parametro l'istanza (self).
# - Opera sui dati specifici di quell'istanza.



class Automobile:
    numero_di_ruote = 4
    
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
    
    def stampa_info(self):
        print("l'automobile è una", self.marca, self.modello)
        
    # metodo speciale per stampare in modo leggibile
    def __str__(self):
        return f"Automobile(marca={self.marca}, modello={self.modello})"
        
#Creazione di oggetti da una classe
#AUTO1 Sarebbe il self.
auto1 = Automobile("Fiat","500")
auto2 = Automobile("BMW","X3")

auto1.stampa_info()
auto2.stampa_info()

print(auto1) # Ora stampa in modo leggibile grazie a __str__

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


# Creazione dell'oggetto con la classe giusta
p1 = Persona2("Luca", 28)
print(p1.saluta())


#- Metodi di classe:
# Operano sulla classe non specifica. SOno definiti come il decoratore @classmethod e ricevono come primo parametro la classe (cls)

class Persona3:
    popolazione = 0

    def __init__(self, nome):
        self.nome = nome
        Persona3.popolazione += 1

    @classmethod
    def conta_persone(cls):
        return f"Ci sono {cls.popolazione} persone create."

p1 = Persona3("Luca")
p2 = Persona3("Giulia")
print(Persona3.conta_persone())  # Ci sono 2 persone create.


#- Metodi statici:
#Funzioni legate alla classe ma non operano ne sull'istanza ne sulla classe. Sono definiti con il decoratre @staticmethod

class Calcolatrice:
    @staticmethod
    def somma(a, b):
        return a + b
risultato = Calcolatrice.somma(5,3)
print(risultato)

#Esempio di metodo decorato

#il metodo mostra_numero_istanze è un metodo di classe che utilizza il decoratore
# @classmethod il parametro cls rappresenta la classe stessa e permette di accedere ad atrtributi di classe.

class Contatore:
    numero_istanza = 0
    
    def __init__(self):
        Contatore.numero_istanza += 1
    
    @classmethod
    def mostra_numero_istanza(cls):
        print(f"Sono state create {cls.numero_istanza} istanze")

#Creazione di alcuni istanze
c1 = Contatore()
c2 = Contatore()

Contatore.mostra_numero_istanza()
