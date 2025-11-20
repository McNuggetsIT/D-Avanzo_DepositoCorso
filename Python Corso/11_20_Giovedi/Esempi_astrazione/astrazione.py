# ============================================================
# ASTRATTAZIONE IN PYTHON
# ============================================================
# L'astrazione si realizza con classi astratte e metodi astratti.
# Una classe astratta (es. Animale) non può essere istanziata direttamente.
# Serve come modello per le sottoclassi (es. Cane, Pesce).
# I metodi astratti (decorati con @abstractmethod) devono essere implementati nelle sottoclassi.
#
# Esempio:
from abc import ABC, abstractmethod
#
class Animale(ABC):
    @abstractmethod
    def muovi(self):
        pass
    
class Cane(Animale):
    def muovi(self):
        print("Corro")
        
class Pesce(Animale):
    def muovi(self):
        print("Nuoto")
        
# Questo garantisce che ogni sottoclasse definisca il proprio comportamento specifico.

# ============================================================
# ASTRATTAZIONE IN PYTHON
# ============================================================
# Una classe astratta è una classe che non può essere istanziata da sola,
# ma serve come modello per altre classi.
# I metodi astratti definiti all'interno di una classe astratta devono essere
# implementati nelle classi derivate che ereditano dalla classe astratta.
#
from abc import ABC, abstractmethod
class Animale(ABC):
    @abstractmethod
    def muovi(self):
        pass
class Cane(Animale):
    def muovi(self):
        print("Corro")
class Pesce(Animale):
    def muovi(self):
        print("Nuoto")
        
# Nell'esempio sopra, Animale è una classe astratta che definisce un metodo astratto muovi().
# Le classi Cane e Pesce sono classi concrete che ereditano da Animale e implementano il metodo muovi.
# Questo assicura che ogni sottoclasse di Animale abbia il proprio modo specifico di muoversi.
#
# ============================================================
# ALTRO ESEMPIO CON METODI ASTRATTI MULTIPLI
# ============================================================
# from abc import ABC, abstractmethod
#

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass
class Rettangolo(Forma):
    def __init__(self, larghezza, altezza):
        self.larghezza = larghezza
        self.altezza = altezza
    def area(self):
        return self.larghezza * self.altezza
    def perimetro(self):
        return 2 * (self.larghezza + self.altezza)
f = Forma()  # TypeError: Can't instantiate abstract class Forma
r = Rettangolo(5, 10)
print(r.area())      # Output: 50
print(r.perimetro()) # Output: 30

# ============================================================
# ASTRATTAZIONE E INTERFACCE IN PYTHON
# ============================================================
# In Python, il concetto di interfacce come è definito in linguaggi come Java o C#
# non esiste nella stessa forma, principalmente a causa della natura flessibile
# e dinamica del linguaggio stesso.
#
# Python segue il principio del "duck typing", che è una forma di polimorfismo.
# Il duck typing permette di non specificare esplicitamente le interfacce tra componenti.
# Se un oggetto "si comporta come un'anatra", allora può essere trattato come tale,
# indipendentemente dalla sua classe.
