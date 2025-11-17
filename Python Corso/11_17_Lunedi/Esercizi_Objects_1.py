#  Esercizio 1: Classe Punto
# Crea una classe chiamata Punto con:
# - Due attributi: x e y, per rappresentare le coordinate nel piano.
# - Un metodo muovi(dx, dy): modifica le coordinate aggiungendo dx e dy.
# - Un metodo distanza_da_origine(): restituisce la distanza dal punto (0,0).

#crazione classe
class Punto:
    #creazione del costruttore
    def __init__(self, x, y):
        self.x= x
        self.y= y
    #istanziamento del metodo muovi
    def muovi(self):
       dx_sx = input("Dove vuoi spostarlo dx-sx?").lower()
       
       if dx_sx == "dx":
           qnt = int(input("di quante celle?"))
           self.x += qnt
       else:
           qnt = int(input("di quante celle?"))
           self.y += qnt
    #metodo stampa 
    def distanza_da_origine(self):
        return f"La distanza dal punto 0.0 è di:{self.x} sull'asse X e {self.y} sull'Asse Y"
    
#utilizzo della classe
p1 = Punto(0,0)
p1.muovi()
print(p1.distanza_da_origine())
           