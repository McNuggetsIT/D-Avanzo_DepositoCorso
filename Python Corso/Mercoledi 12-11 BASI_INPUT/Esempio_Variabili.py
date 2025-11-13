#Pre-Requisiti: 
    #1: Non possono avere spazi
    #2: Possono includere solo lettere,numeri ed underscore NO CARATTERI SPECIALI
    #3: non devono iniziare per numeri O underscore

#Come creare una variabile
    #Si crea con Nome = valore 



#Tipi di dati


#int (interi)
x = 10
y = -10
print("x = " + str(x) +  "\ny = " + str(y))

#float (floating-point numbers) numeri con la virgola
a = 3.14
b = -1.0

print(a,b)

#str (String)

z = 1
w = "mirko"

#Accedere ad un carattere specifico nella stringa
stringa = "Python"
print("lettera posizione 0 " + stringa[0]) #output: P
print("lettera posizione 1 " + stringa[1]) #output: t

#Concatenazione strings

saluto = "Ciao"
nome = input("Scrivi il tuo nome: ")
messaggio = saluto + " " + nome
print(messaggio)

#Metodi Stringhe
#len() ottieni lunghezza di una stringa
#upper() per convertire una stringa in maiuscola
#lower() per convertire una stringa in minuscola
#split() dividere la stringa in base ad un deliminatore (Esempio s.split(',') divide la stringa per ogni , che trova)
#replace() sostituisce parti di una stringa con un altri
#ESEMPI
s = "Hello,world"
print(len(s))
print(s.upper())
print(s.split(','))
print(s.replace('world', 'universe'))

#CHAR se string è un una seguenza di caratteri char si riferisce al SINGOLO simbolo.
carattere = 'A'

#Booleani TRUE & FALSE
#in python i booleani sono uno dei piu importanti per 2 motivi : 
# 1= Funzione logica applicativa che noi abbiamo 
# 2= 
#
print("x: " + str(x) , "\ny: " + str(y), "\nz: " + str(z))
print(x < y and y > z) # AND = Restituisce True se entrambe son vere
print(x <y or z > y) # OR = restituisce True se una delle due è vera
print(y <= x) # restituisce il valore booleno opposto a cio che segue
 
#Controlli di confronto
# == ugale a
# != diverso da
# < minore di
# > maggiore di
# <= minore o uguale a
# >= maggiore o uguale a

g = 5
k = 10
print(" UGUALE Output False:")
print(x == y)
print(" DIVERSO Output True:")
print(x != y)
print(" MINORE Output True:")
print(x < y) 