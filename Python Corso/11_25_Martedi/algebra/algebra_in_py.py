#NumPy include un modulo per algebra lineare numpy.linalg

#Prodotto Matriciale = np.dot(), np.matmul().
#Determinante: np.linalg.det().
#Autovalori e Autovettori: np.linalg.eig()
#Risoluzione di sistemi lineari: np.linalg.solve()

import numpy as np

#CREAZIONE DI UNA MATRICE QUADRATA
A = np.array([[1,2],[3,4]])
A = np.array([[3,4],[5,6]])
#Calcolo dell'inversa della matrice
A_inv = np.linalg.inv(A)
print("Inversa di A: ", A_inv)

#Calcolo della norma del vettore
v = np.array([3,4])
norm_v = np.linalg.norm(v)
print("Norma di v:", norm_v)

np.linalg.solve

#Questa è una funzione utilizata per risolvere un sistema di equazioni della forma 
# Ax=BAx = BAx = B
#AAA è una matrice quadrata e BBB un vettore o una matrice

#Creazione della matrice A e del vettore B
A2= np.array([[3,1],[1,2]])
B2= np.array([9,8])

#RIsoluzione del sistema di equazioni Ax = B

x = np.linalg.solve(A2,B2)
print("Soluzione x: ", x) #output [2.3.]

#TRASFORMATA DI FOURIER DISCRETA (DFT) di un array.
np.fft.fft
#Creazione di un segnale
t = np.linspace(0,1,400)
sig = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)

#Calcolo della trasfomata di fourier
fft_sig = np.fft.fft(sig)
#Frequenze associate
freqs = np.fft.fftfreq(len(fft_sig))

print("Trasfomata di fourier:", fft_sig)
print("Freq associate:", freqs)