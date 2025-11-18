# Classe base: Veicolo
class Veicolo:
    # Costruttore della classe Veicolo: inizializza marca e modello
    def __init__(self, marca, modello):
        self.marca = marca          # Salva la marca del veicolo (es. "Ferrari")
        self.modello = modello      # Salva il modello del veicolo (es. "F8 Spider")

    # Metodo per mostrare le informazioni del veicolo
    def mostra_informazioni(self):
        print(f"Veicolo marca {self.marca}, modello {self.modello}")  # Stampa marca e modello


# Seconda classe base: DotazioniSpeciali
class DotazioniSpeciali:
    # Costruttore della classe DotazioniSpeciali: riceve una lista di dotazioni
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni  # Salva le dotazioni (es. ["ABS", "ESP", "Launch Control"])

    # Metodo per mostrare le dotazioni speciali
    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")  # Unisce gli elementi con virgole

        
        
# Classe derivata: AutomobileSportiva eredita da Veicolo e DotazioniSpeciali
class AutomobileSportiva(Veicolo, DotazioniSpeciali):
    # Costruttore della classe AutomobileSportiva
    # Riceve marca, modello, dotazioni e cavalli come parametri
    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self, marca, modello)           # Inizializza la parte Veicolo
        DotazioniSpeciali.__init__(self, dotazioni)      # Inizializza la parte DotazioniSpeciali
        self.cavalli = cavalli                           # Salva la potenza in cavalli (es. 720)

def mostra_informazioni(self):
    # super().mostra_informazioni():
    # Qui usiamo super() per richiamare il metodo mostra_informazioni della superclasse.
    # In questo caso AutomobileSportiva eredita da Veicolo e DotazioniSpeciali.
    # L'ordine di ricerca dei metodi segue l'MRO (Method Resolution Order).
    # Quindi super() prende il primo mostra_informazioni che trova, cioè quello di Veicolo.
    # Risultato: stampa marca e modello del veicolo.
    
    #PRATICAMENTE TI VA A PRENDERE IL PRINT DI SOPRA (VEICOLO MARCA E MODELLO )
    super().mostra_informazioni()

    # Dopo aver stampato marca e modello, aggiungiamo un'informazione in più:
    # la potenza del motore in cavalli (CV).
    print(f"Potenza: {self.cavalli} CV")

    # Infine richiamiamo mostra_dotazioni(), che appartiene alla classe DotazioniSpeciali.
    # Questo metodo stampa tutte le dotazioni speciali dell'automobile.
    self.mostra_dotazioni()


auto_sportiva = AutomobileSportiva("Ferrari","F8", ["ABS", "Controllo trazione", "Airbag laterali"], 720)
auto_sportiva.mostra_informazioni()
auto_sportiva.mostra_dotazioni()
