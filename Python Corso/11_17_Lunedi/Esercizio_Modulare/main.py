from moduli.input_dati import leggi_dati_vendita, leggi_dati_da_file
from moduli.analisi_dati import calcolo_del_totale_e_media, vendite_sopra_media
from moduli.visualizza_risultati import mostra_risultati

def main():
    print("=== Analizzatore di Dati di Vendita ===")
    print("Vuoi inserire i dati a mano (1) o leggerli dal file (2)?")
    scelta = input("Digita 1 o 2: ")

    # Lettura dei dati
    if scelta == "1":
        vendite = leggi_dati_vendita()
    elif scelta == "2":
        vendite = leggi_dati_da_file()
    else:
        print("Scelta non valida.")
        return

    # Analisi dei dati
    totale, media = calcolo_del_totale_e_media(vendite)
    sopra_media = vendite_sopra_media(vendite, media)

    # Visualizzazione dei risultati
    mostra_risultati(totale, media, sopra_media)


if __name__ == "__main__":
    main()
