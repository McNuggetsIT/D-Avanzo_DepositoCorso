#INPUT ED OUTPUT SU UN FILE
# si apre usando il metodo open() e possono avere altri metodi tipo letture scrittura aggiunga ecc

#ESEMPIO

file = open("Python Corso/11_21_Venerdi/INPUT_OUTPUT_ESEMPI/nome_file.txt", "r")

#il metodo read() legge tutto il contenuto
#il metodo readline() legge solo una singola riga

contenuto = file.read()
print(contenuto)
file.close()

#Scrittura del file :
#è possibile scrivere dati su un file utilizzando il metodo write() "w" (SOPRASCRITTURA)
# "a" per aggiungere (append)

file = open("Python Corso/11_21_Venerdi/INPUT_OUTPUT_ESEMPI/nome_file.txt", "w")
file.write("Meow meow meow meow")
file.close()

file = open("Python Corso/11_21_Venerdi/INPUT_OUTPUT_ESEMPI/nome_file.txt", "r")
nuovo_contenuto = file.read()
print(nuovo_contenuto)
file.close()

#Bisogna ricordare CHE BISOGNA CHIUDERE SEMPRE il file.close()

#Utilizzo di with si occupa della chiusura del file in automatico


with open("Python Corso/11_21_Venerdi/INPUT_OUTPUT_ESEMPI/nome_file.txt", "a") as file:
    file.write("Meow meow meow meow\nMeow meow meow meow22222222222222")


with open("Python Corso/11_21_Venerdi/INPUT_OUTPUT_ESEMPI/nome_file.txt", "r") as file:
    contenuto = file.read()
    print(contenuto)
