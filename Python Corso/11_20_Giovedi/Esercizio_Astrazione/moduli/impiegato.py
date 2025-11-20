from abc import ABC , abstractmethod
class Impiegato(ABC):
    def __init__(self, nome, cognome, stipendio_base):
        self.nome = nome
        self.cognome = cognome
        self.stip_b = stipendio_base
        
    @abstractmethod
    def calcolo_stipendio(self):
        pass
    
    def stampa_info(self):
        print(f"Nome: {self.nome} {self.cognome}")
        print(f"Stipendio: {self.calcolo_stipendio()}")
        print("-" * 30)