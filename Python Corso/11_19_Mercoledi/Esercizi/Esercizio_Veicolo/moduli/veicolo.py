class Veicolo:
    def __init__(self,marca,modello,anno,accensione):
        self._marca = marca
        self._modello = modello
        self._anno = anno
        self._accensione = accensione
    
    def get_marca(self):
        return self._marca

    def set_marca(self, nuova_marca):
        if nuova_marca:
            self._marca = nuova_marca


    def get_modello(self):
        return self._modello

    def set_modello(self, nuovo_modello):
        if nuovo_modello:
            self._modello = nuovo_modello
            
    def get_anno(self):
        return self._anno

    def set_anno(self, nuovo_anno):
        if nuovo_anno > 1900:
            self._anno = nuovo_anno

    def get_accensione(self):
        return self._accensione

    def set_accensione(self, stato):
        self._accensione = bool(stato)
      
    def accendi(self):
        if not self.get_accensione():
            self.set_accensione(True)
            print("Veicolo acceso.")
        else:
            print("Il veicolo è già acceso.")
            
    def spegni(self):
        if self.get_accensione():
            self.set_accensione(False)
            print("Veicolo spento")
        else:
            print("Veicolo è già spento")