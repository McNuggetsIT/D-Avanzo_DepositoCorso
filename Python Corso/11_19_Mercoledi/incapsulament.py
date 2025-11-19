#Incapsulamento nasconde i dettagli dell'implementazione
#incapsulamento è divisa in 2 parti: Modificari e Operazioni pratiche

#Attributi privati (__attributo): inserendo due __ al nome di un attributo diventa privato e non può essere accesso direttamento
#dall'esterno della classe. Per accedere o modificare un attributo privato bisogna usare un getter e setter

#Attributi protetti (_attributo): insrendo UN _ al nome viene considerato proteto. si tratta di una convenzione che di una 
# funzionalità indicando che deve essere usato solo all'interno della classe e delle suo sottoclassi

#Metodi Getter e Setter: servono per OTTENERE (GET) e MODIFICARE(SET) questi metodi forniscono un controllo maggiore sull'accesso
#e modifica dei dati

class Computer:
    def __init__(self):
        self.__processore = "Intel i5" #ATTRIUTO PRIVATO
    def get_processore(self):
        return self.__processore
    def set_processore(self,processore):
        self.__processore = processore

pc = Computer()

print(pc.get_processore()) # Prende l'attributo tramite GET
pc.set_processore("Amd Ryzen 5") # MODIFICA l'ATTRIBUTO tramite SET
print(pc.get_processore())

#Incapsulamento

#In Python, i livelli di visibilità (o scope delle variabili) sono concetti importanti per gestire l'accesso
#e la visibilità delle variabili in differenti parti del codice.

#I principali livelli di visibilità sono: globale, locale e non-locale

#Globale: una variabile dichiarata fuori da tutte le funzioni è conosciuta come variabile globale.
#È accessibile da qualsiasi punto del codice dello stesso modulo, incluso dentro le funzioni,
#a meno che non venga oscurata da una variabile locale con lo stesso nome.

#Locale: le variabili locali sono quelle dichiarate all'interno di una funzione
#e sono accessibili solo all'interno di quella funzione.
#Non sono visibili né accessibili dall'esterno della funzione.

#Non-locale (utilizzato con nonlocal): questo livello di visibilità si applica nelle funzioni annidate,
#dove una variabile deve essere accessibile in più di una funzione interna ma non globalmente al modulo.
#La parola chiave nonlocal è utilizzata per indicare che una variabile si riferisce a una variabile
#di uno scope superiore (non globale) più vicino.

#Variabile globale

num = 10

def funzione_esterna():
    num = 5
    print("numero dentro funz esterna (locale): ", num)
    
    def funzione_interna():
    
        nonlocal num
        num = 3
        print("Numero dentro funzione_interna(non local): ", num)

    funzione_interna()

print("numero nel main globale: ", num)
funzione_esterna()
print("numero nel main dopo chiamata (globale non è cambiata): ", num)


#In py non esistono private o protected abbiamo solo il _ per protteto e _ _ per privata e possono esser chiamate solo tramite getter e setter

#ANChe le classi pososno essere privati
#PRIVATI

class MiaClasse:
    def __init__(self):
        self.__variabile_privata = "Sono privata"
        
    def __metodo_privato(self):
        return "questo è n metodo privato"
    def __cicciobello_saluta(self):
        return "ciccio bello napoletano ti saluta ciao!"

def uso_metodo_privato(self):
    return self.__cicciobello_saluta()
    
obj = MiaClasse()

print(obj.__variabile_privata) #ERRORE
print(obj._MiaClasse__variabile_privata) #FUNZIONA MA NON SI FA

print(obj.uso_metodo_privato())
#PROTETTI
#a differenza dei privati i metodi protetti vengono ereditati  e NON sono visibili all'esterno ma si possono usare

class ClasseBase:

    def __init__(self):
        self._variabile_protetta = "Sono protetta"


class SottoClasse(ClasseBase):
    def __init__(self):
        super().__init__()
        print(self._variabile_protetta)  # Accesso consentito

obj = SottoClasse()
# Accesso da fuori la classe (non consigliato, ma possibile)
print(obj._variabile_protetta)
