class Posto:
    def __init__(self,numero,fila,occupato :bool):
        self._num = numero
        self._fila = fila
        self._ocp = occupato
        
    def get_numero(self):
        return self._num

    def set_numero(self, numero):
        self._num = numero

    def get_fila(self):
        return self._fila

    def set_fila(self, fila):
        self._fila = fila

    def get_occupato(self):
        return self._ocp

    def set_occupato(self, occupato: bool):
        if not isinstance(occupato, bool):
            raise ValueError("occupato deve essere un booleano")
        self._ocp = occupato
    
    def prenota(self):
        self._ocp = True
        
    def libera(self):
        self._ocp = False

    def is_occupato(self):
        return self._ocp

    def __str__(self):
        if self.ocp == True:
            stato = "Occupato"
        else:
            stato = "Libero"

        return f"Posto {self._fila}{self._num} - {stato}"