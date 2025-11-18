from Moduli.libro import Libro


def cerca_libro_da_input():
    titolo = input("Inserisci titolo del libro ")
    autore = input("Inserisci l'autore del libro ")
    return Libro(titolo, autore)

def crea_libro_da_input():
    titolo = input("Inserisci titolo del libro ")
    autore = input("Inserisci l'autore del libro ")
    isbn = Libro._genera_isbn()
    return Libro(titolo, autore,isbn)