#Crea una classe biblioteca che permetta di creare un libro e stamparlo

#Creazioen della classe
# Creazione della classe
class Libro:
    # costruttore: inizializza gli attributi dell'oggetto
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        
    def descrizione(self):
        return f"Il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine."
    
    #istanzio metodo per creare libri
def create_book():
    lista_libri = []
    scelta =  int(input("Quanti libri vuoi creare?"))
    cont = 0
    
    # il ciclo while serve a creare tanti oggetti Libro quanti indicati dall'utente
    while cont <= scelta - 1 :
        titolo = input("Titolo: ")
        autore = input("Autore: ")
        pagine = input("Pagine: ")
        libro = Libro(titolo, autore, pagine)  # istanziazione di un nuovo oggetto Libro
        lista_libri.append(libro)
        cont = cont + 1
    return lista_libri

# qui stampiamo la descrizione di ogni libro creato
libri = create_book()

for libro in libri:
    print(libro.descrizione())
