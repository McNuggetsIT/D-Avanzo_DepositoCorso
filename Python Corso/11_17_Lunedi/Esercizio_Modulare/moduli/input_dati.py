import re
def leggi_dati_vendita():
    
    while True:    
        
        dati = input("Inserisci gli importi separati da spazi: ")
        if re.match(r'^\d+(\s+\d+)*$', dati):
            vendite = [int(x) for x in dati.split()]
            return vendite 
        else :
            print("error inserisci un numero")
            
def leggi_dati_da_file(percorso = "Python Corso/11_17_Lunedi/Esercizio_Modulare/dati_test.txt"):
    with open(percorso, "r") as f:
        dati = f.readline().strip()   # legge la prima riga
        vendite = [int(x) for x in dati.split()]
        return vendite
