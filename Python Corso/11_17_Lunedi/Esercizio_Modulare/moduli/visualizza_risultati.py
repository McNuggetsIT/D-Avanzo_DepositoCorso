def mostra_risultati(totale, media, sopra_media):
    if totale == 0:
        print("Nessun dato di vendita disponibile")
    else:
        print(f"Totale vendite: €{totale}")
        print(f"Media vendite: €{media:.2f}")

        if sopra_media:
            print("Giorni con vendite sopra la media:", sopra_media)
        else:           
            print("Nessuna vendita sopra la media.")
