import random


class Elettrodomestico:
    def __init__(self, marca, anno_acquisto, guasto, modello):
        self.__marca = marca
        self.__aqq = anno_acquisto
        self.__guasto = guasto
        self.__modello = modello

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_anno_acquisto(self):
        return self.__aqq

    def set_anno_acquisto(self, anno):
        if anno > 2025:  
            print("L'anno di acquisto non può essere nel futuro")
        self.__aqq = anno

    def get_guasto(self):
        return self.__guasto

    def set_guasto(self, guasto):
        self.__guasto = guasto

    def get_modello(self):
        return self.__modello

    def set_modello(self, modello):
        self.__modello = modello

    def descrizione(self):
        return f"Marca: {self.__marca}, Modello: {self.__modello}, Anno: {self.__aqq}, Guasto: {self.__guasto}"

    def stima_costo_base(self):
        return random.randint(50,300)