# filter() è una funzione integrata che consente di filtrare gli elementi di una sequenza 
# ( come una lista, tupla o insieme)

#Restituisce un iterazione che continee solo una sequenza che soddisfano la condizione:

#filter(funzione_di_filtro, sequenza)
# La funzione is_even(x) restituisce True se x è pari, False altrimenti.
# filter(is_even, numbers) applica is_even a ogni elemento della lista numbers.
# Restituisce solo i numeri pari sotto forma di iteratore.
# list() converte l'iteratore in una lista filtrata di numeri pari.

def is_even(x):
    return x % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = list(filter(is_even,numbers))
print(even_numbers)