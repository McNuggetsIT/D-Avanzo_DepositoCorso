 
def calcolo_del_totale_e_media(vendite):
    if not vendite:
        return 0,0
    else:
        totale = sum(vendite)
        media = totale/len(vendite)
        return totale,media
    
def vendite_sopra_media(vendite,media):
    sopra_media = []
    for vendite in vendite:
        if vendite > media:
            sopra_media.append(vendite)
    return sopra_media