from moduli.persona import Persona

class Studente(Persona):
    def __init__(self, nome, eta, voti):
        super().__init__(nome, eta)
        self.__voti = voti

    def get_voti(self):
        return self.__voti
    
    def set_voti(self, nuovi_voti):
        self.__voti = nuovi_voti

    def calcola_media(self, materia):
        if materia in self.__voti and len(self.__voti[materia]) > 0:
            media = sum(self.__voti[materia]) / len(self.__voti[materia])
            return f"{materia}: media {media:.2f}"
        else:
            return f"Nessun voto disponibile per {materia}"


def ins_voti():
    voti = {}
    while True:
        materia = input("Inserisci materia (X per terminare): ").lower()
        if materia == "x":
            break
        voti[materia] = []
        while True:
            voto = input(f"Inserisci voto per {materia} (X per terminare): ").lower()
            if voto == "x":
                break
            try:
                voto = int(voto)
                if 0 <= voto <= 10:
                    voti[materia].append(voto)
                else:
                    print("Il voto deve essere tra 0 e 10")
            except ValueError:
                print("Inserisci un numero valido")
    return voti