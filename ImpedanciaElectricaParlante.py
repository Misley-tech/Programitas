import numpy as np
import matplotlib.pyplot as plt

pi=np.pi 

f=np.arange(0,20000,1)
w = 2*pi*f

Rg = 0
Re = 5.4
Le = 0.93*(10**(-3))    
B=3
l=11
Mmd = 147.1
Rms = 12.6
Cms = 100*(10**(-6))
Zar = 1
Sd = 0.088
Zmr = (B*l**2)/(2*(Sd**2)*Zar)
# Bl = 33


# corchete = [0]*len(w)
# Z = [0]*len(w)
# absolute_Z=[0]*len(w)

# for i in range(len(w)):
#     termino1 = (Cms/Mmd)*((1/Rms)+(1/(2*Zmr)))
#     termino2 = (1/(2*Rms*Zmr))*(w[i]*Cms-(1/(w[i]*Mmd)))
#     corchete[i] = complex(termino1,termino2)
#     num =  (Bl**2)*Cms
#     den = 2*Rms*Mmd*Zmr*corchete[i]
#     paralelo = num/den
#     Z[i] = complex(Rg+Re,w[i]*Le) + paralelo
#     absolute_Z[i] = abs(Z[i])                               

# plt.plot(absolute_Z)
# # plt.xlim([20,100])
# plt.show()

termino2 = [0]*len(w)
termino3 = [0]*len(w)
Z = [0]*len(w)
absolute_Z=[0]*len(w)
paralelo = [0]*len(w)

for i in range(len(w)):
    termino1 = Rms
    termino2[i] = complex(0,w[i]*Mmd)
    termino3[i] = complex(0,-1/(w[i]*Cms)) 
    termino4 = 2*Zmr
    paralelo[i] = (Bl**2)/(termino1+termino2[i]+termino3[i]+termino4)
    Z[i] = complex(Rg+Re,w[i]*Le)+paralelo[i]
    absolute_Z[i] = abs(Z[i])

plt.plot(absolute_Z) 
# plt.xlim([20,100])
plt.show()