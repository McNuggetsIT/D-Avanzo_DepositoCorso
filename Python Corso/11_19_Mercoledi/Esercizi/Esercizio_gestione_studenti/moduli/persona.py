class Persona:
    def __init__(self, nome, eta):
        self.__nome = nome
        self.__eta = eta
    
    def set_nome(self, nuovo_nome):
        if nuovo_nome != "":
            self.__nome = nuovo_nome
        else:
            print("Nome non valido")
            
    def set_eta(self, nuova_eta):
        if nuova_eta > 0:
            self.__eta = nuova_eta
            
    def get_nome(self):
        return self.__nome

    def get_eta(self):
        return self.__eta

    def presentazione(self):
        print(f"Il nome è {self.__nome} e ha {self.__eta} anni")