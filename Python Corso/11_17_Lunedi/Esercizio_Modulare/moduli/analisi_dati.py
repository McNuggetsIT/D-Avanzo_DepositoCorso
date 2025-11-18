 
def calcolo_del_totale_e_media(vendite):
    if not vendite: #Se non ci son vendite ritorna 0
        return 0,0
    else:
        totale = sum(vendite)
        media = totale/len(vendite)
        return totale,media
    
def vendite_sopra_media(vendite,media):
    sopra_media = [] #creo una lista di vendite
    for vendite in vendite:
        if vendite > media: #se le vendite son maggiori della media
            sopra_media.append(vendite)
    return sopra_media