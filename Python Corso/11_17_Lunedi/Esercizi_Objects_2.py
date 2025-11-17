# Esercizio 2: Classe Libro
# Crea una classe chiamata Libro con:
# - Tre attributi: titolo, autore, pagine.
# - Un metodo descrizione(): restituisce una stringa del tipo:
#   "Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine."

#creazione della classe
class Libro:
    #istanziamento del costruttore
    def __init__(self,titolo,autore,pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    #creazione metodo descrizione
    def descrizione(self):
        return f"Il libro{self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine"

#utilizzo della classe
libro1 = Libro("Divina Commedia", "Dante", 350)
print(libro1.descrizione())
