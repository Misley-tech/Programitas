import numpy as np
import matplotlib.pyplot as plt
pi = np.pi 

f = np.arange(0,50e3,step=0.01)
print(f)
w = 2*pi*f

R = 0.01
L = 10**(-3)
C = 10**(-3)

fs = 1/(2*np.pi*np.sqrt(L*C))
print(2*np.pi*fs)

Z = [0]*len(w)
abs_Z = [0]*len(w)
for i in range(len(w)):
    Z[i] = complex(R,w[i]*L-(1/(w[i]*C)))
    abs_Z[i] = abs(Z[i])

plt.semilogx(f,abs_Z)
plt.ylim([0,100])
plt.ylabel('hola')
plt.xlim([0,20000])
plt.show()