from moduli.posto import Posto
class PostoVip(Posto):
    def __init__(self, numero, fila, occupato: bool = False, servizi_extra=None):
        super().__init__(numero, fila, occupato)
        if servizi_extra is None:
            servizi_extra = ["Accesso al lounge", "Servizio in posto"]
        self._servizi_extra = servizi_extra
        
    def prenota(self):
        if not self._ocp:   # uso _ocp, non ocp
            self._ocp = True
            print(f"Ti sei prenotato nel posto VIP {self._fila}{self._num}.")
            for servizio in self._servizi_extra:
                print(f" - {servizio}")
        else:
            print(f"Il posto VIP {self._fila}{self._num} è già occupato!")
            
    def __str__(self):
        stato = "Occupato" if self._ocp else "Libero"
        servizi = ", ".join(self._servizi_extra)
        return f"Posto VIP {self._fila}{self._num} - {stato} | Servizi: {servizi}"


class PostoStandard(Posto):
    def __init__(self, numero, fila, costo, occupato: bool = False):
        super().__init__(numero, fila, occupato)
        self._costo = costo
        
    def get_costo(self):
        return self._costo

    def set_costo(self, costo):
        self._costo = costo
        
    def prenota_in_sala(self):
        if not self._ocp:
            self._ocp = True
            print(f"Posto standard {self._fila}{self._num} prenotato in sala.")
            print(f"Costo prenotazione in sala: {self._costo}€")
        else:
            print(f"Il posto standard {self._fila}{self._num} è già occupato!")

    def prenota_online(self):
        if not self._ocp:
            self._ocp = True
            costo_finale = self._costo * 0.9
            print(f"Posto standard {self._fila}{self._num} prenotato online.")
            print(f"Costo prenotazione online (sconto 10%): {costo_finale}€")
        else:
            print(f"Il posto standard {self._fila}{self._num} è già occupato!")
            
    def __str__(self):
        stato = "Occupato" if self._ocp else "Libero"
        return f"Posto Standard {self._fila}{self._num} - {stato} | Costo: {self._costo}€"