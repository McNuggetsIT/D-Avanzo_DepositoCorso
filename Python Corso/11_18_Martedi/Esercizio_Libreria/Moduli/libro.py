class Libro:
    _cont_isbn = 1
    
    def __init__(self,titolo,autore,isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn

    @staticmethod
    def _genera_isbn():
        isbn = Libro._cont_isbn
        Libro._cont_isbn += 1
        return str(isbn)
    
    def descrizione(self):
        return f"{self.titolo} di {self.autore} (ISBN: {self.isbn})"
    
    @staticmethod
    def from_string(riga):
        titolo, autore, isbn = riga.strip().split("|")
        return Libro(titolo, autore, isbn)