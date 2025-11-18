def mostra_catalogo(libreria):
    if not libreria.catalogo:
        print("il catalogo è vuoto")
    else:
        for libro in libreria.catalogo:
            print(libro.descrizione())
            
def mostra_risultati_ricerca(lista_libri):
    if not lista_libri:
        print("Nessun libro trovato.")
    else:
        print("Risultati trovati:")
        for libro in lista_libri:
            print(libro.descrizione())