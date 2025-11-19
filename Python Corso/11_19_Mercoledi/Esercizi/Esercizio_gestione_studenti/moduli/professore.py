from moduli.persona import Persona

class Professore(Persona):
    def __init__(self, nome, eta, materia):
        super().__init__(nome, eta)
        self.__materia = materia
        
    def set_materia(self, nuova_materia):
        if nuova_materia != "":
            self.__materia = nuova_materia
        
    def get_materia(self):
        return self.__materia

    def presentazione(self):
        print(f"Sono il professore {self.get_nome()}, ho {self.get_eta()} anni e insegno {self.__materia}")