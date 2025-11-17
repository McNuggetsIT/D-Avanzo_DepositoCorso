import re
#Sto usando il regex
def leggi_dati_vendita():
    
    while True:    
        
        dati = input("Inserisci gli importi separati da spazi: ")
        if re.match(r'^\d+(\s+\d+)*$', dati): #uso del regex per controllare il tipo di inserimento per evitare lettere o altro 
            vendite = [int(x) for x in dati.split()]
            return vendite 
        else :
            print("error inserisci un numero")
            #con questo mi prendo i dati dal file txt (mi son aiutato per farlo)
def leggi_dati_da_file(percorso = "Python Corso/11_17_Lunedi/Esercizio_Modulare/dati_test.txt"):
    with open(percorso, "r") as f:
        dati = f.readline().strip()
        vendite = [int(x) for x in dati.split()]
        return vendite
