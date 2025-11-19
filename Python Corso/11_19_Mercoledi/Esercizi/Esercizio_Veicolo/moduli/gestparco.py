
class GestoreParcoVeicoli:
    def __init__(self):
        self._veicoli = []

    def aggiungi_veicolo(self, veicolo):
        self._veicoli.append(veicolo)

    def rimuovi_veicolo(self, modello,marca):
        for veicolo in self._veicoli:
            if veicolo.get_marca() == marca and veicolo.get_modello() == modello:
                self.veicoli.remove(veicolo)
                print("Rimosso")
            else:
                print("Non trovato")
            

    def lista_veicoli(self):
        return self._veicoli
