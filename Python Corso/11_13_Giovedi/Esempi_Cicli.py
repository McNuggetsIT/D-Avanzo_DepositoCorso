#Esistono due tipi di clicli While e For
#i while si usano quando non sai quante volte si devono far ripetere il ciclo
#i for quanto un definito di ripetizioni

#ciclo matematico
conteggio = 0
while conteggio <5:
    print(conteggio)
    conteggio += 1
    
#ciclo booleano
controller = True

while controller:
    scelta = input("Vuoi continuare?")
    if scelta.lower() == "no":
        controller= False
    else:
        print("Stai continuando")
        
#CICLI FOR

#for elemento in sequenza:
    #blocco di codice
#ESEMPIO
numeri = [1,2,3,4,5]

for numero in numeri:
    print(numero)
    
    
#range() è una funzione di py che restituisce una sequenza numeri interi che possono esser usati in  cicli for
#la sintassi è

#range([start]), stop, [step]

#i parametri di range sono:
#start() il valore di partenza se omesso = 0
#stop() il valore di sequenza di fine OBBLIGATORIO
#step() la differenza tra i valore successivi se omesso il valore è di 1 (quindi fa sempre un +1)

for i in range(5):
    print(i)
#1 PARTENZA #10 STOP #3 i salti di numeri a volta (quindi 1-3-5-7-9)
for i in range(1,10,2):
    print(i)
    


