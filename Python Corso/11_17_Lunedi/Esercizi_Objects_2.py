# Esercizio 2: Classe Libro
# Crea una classe chiamata Libro con:
# - Tre attributi: titolo, autore, pagine.
# - Un metodo descrizione(): restituisce una stringa del tipo:
#   "Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine."

class Libro:
    
    def __init__(self,titolo,autore,pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    
    def descrizione(self):
        return f"Il libro{self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine"
    
libro1 = Libro("Divina Commedia", "Dante", 350)
print(libro1.descrizione())
