import soundfile as sf
import numpy as np
import scipy as sc

A,fs=sf.read('C:/Users/Asus/Desktop/programitas/SVD/Audio/Hola/Hola_8khz.wav')
A=np.array([A])
A_t=np.transpose(A)
C=A_t@A

eigenvalues, V = np.linalg.eig(C)
singular_values = np.sqrt(eigenvalues)
sigma = np.diag(singular_values)
sigma_inv = sc.linalg.pinvh(sigma)
U=A@V@sigma_inv

F=U@sigma@np.transpose(V)
F=np.real(F)
print(F[0])
print(A[0])
sf.write('HolaSVD.wav',F[0],fs)