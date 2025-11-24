# ESERCIZIO:
# Creare un filtro che controlli, per ogni elemento x della lista,
# se elem[x] e elem[x+1] sono entrambi maggiori di elem[x+2].
# Per gli ultimi elementi della lista, usare due volte quelli presenti (tranne l’ultimo)
# per evitare errori di indice e completare il controllo.

numbers = [1,2,3,4,5,6,7,8,9,10]

def adds(i):
    for j in [i]:
        tot = numbers[j] + numbers[j+1]
        if tot > numbers[j+2]:
            return True
    return False

tots = list(filter(adds, range(len(numbers)-2)))

risultati = [numbers[i] + numbers[i+1] for i in tots]
print(risultati)