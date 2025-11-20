from moduli.tipi_elettro import Lavatrice, Frigorifero, Forno
from moduli.elettrodomestico import Elettrodomestico

class TicketRiparazione:
    def __init__(self, id_ticket, elettrodomestico : Elettrodomestico, stato="aperto", note=None):
        self.__it = id_ticket
        self.__ed = elettrodomestico
        self.__stato = stato
        self.__note = note if note is not None else []
        
    def get_id_ticket(self):
        return self.__it

    def get_elettrodomestico(self):
        return self.__ed

    def get_stato(self):
        return self.__stato

    def set_stato(self, stato):
        if stato not in ["aperto", "in lavorazione", "chiuso"]:
            raise ValueError("Stato non valido")
        self.__stato = stato

    def get_note(self):
        return self.__note
    
    def aggiungi_nota(self):
        n_nota = input("Scrivi nota: ")
        self.__note.append(n_nota)
        return n_nota

     
    def calcola_preventivo(self, *voci_extra):
        base = self.__ed.stima_costo_base()
        totale = base + sum(voci_extra)
        dettaglio = f"Costo base: {base} | Extra: {list(voci_extra)} | Totale: {totale}"
        return dettaglio

    
    def stampa_note(self):
        return "\n".join(self.__note) if self.__note else "Nessuna nota"
    def descrizione_ticket(self):
        
        return f"Ticket {self.__it} - Stato: {self.__stato} - Elettrodomestico: {type(self.__ed).__name__}"


