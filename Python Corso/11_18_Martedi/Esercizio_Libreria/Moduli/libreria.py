from Moduli.libro import Libro


class Libreria:
    def __init__(self):
        self.catalogo = []

    def aggiungi_libro(self, libro):
        # Se ISBN già usato, cerca il prossimo libero
        isbn_usati = {l.isbn for l in self.catalogo}

        # Se l'ISBN del libro è già occupato
        if libro.isbn in isbn_usati:
            nuovo_isbn = 1
            while str(nuovo_isbn) in isbn_usati:
                nuovo_isbn += 1
            libro.isbn = str(nuovo_isbn)   # assegna il primo libero

        # Aggiunge il libro con ISBN corretto
        self.catalogo.append(libro)
        print(f"Libro '{libro.titolo}' aggiunto con ISBN {libro.isbn}.")


    def rimuovi_libro(self, isbn):
        self.catalogo = [libro for libro in self.catalogo if libro.isbn != isbn]
        
    def cerca_per_titolo(self,titolo):
        risultati = []
        for libro in self.catalogo:
            if titolo.lower() in libro.titolo.lower():
                risultati.append(libro)
        return risultati

    def carica_da_file(self, percorso):
        with open(percorso, "r", encoding="utf-8") as f:
            for riga in f:
                libro = Libro.from_string(riga)
                self.aggiungi_libro(libro)




