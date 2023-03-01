import numpy as np
import matplotlib.pyplot as plt
from scipy.special import struve
from scipy.special import jv

def ImpedanciaParlante(Rg,Re,Le,Bl,Mms,Rms,Cms,a,c,rho0,resolucion):
    """
    Funcion que calcula el modulo de la impedancia electrica de un parlante.
        Entradas:
            Rg (float): impedancia del generador
            Re (float): resistencia electrico de la bobina [ohm]
            Le (float): inductancia de la bobina movil [mHy]
            Bl (float): motor magnetico [Tm]
            Mms (float): masa mecanica del sistema [kg]
            Rms (float): resistencia mecanica de la suspensión [kg/s]
            Cms (float): compliancia mecanica de la suspension [mm/N]
            a (float): radio efectivo del diafragma [mm]
            c (float): velocidad de propagación del sonido
            rho0 (float): densidad del aire
            resolucion (float): resolucion de la curva de impedancia
        Salidas:
            f (array): array con las frecuencias consideradas
            abs_z (array): modulo de la impedancia electrica del parlante
    """
    pi=np.pi 

    f=np.arange(0,20000,resolucion) #frecuencia 
    w = 2*pi*f #frecuencia angular

    lambda_ = c/f #longitud de onda
    k = 2*pi/lambda_ #numero de onda

    real = pi*(a**2)*rho0*c*(1-(jv(1,(2*k*a)/(k*a)))) #parte real de Zmr
    imag = pi*(a**2)*rho0*c*(struve(1,(2*k*a)/(k*a))) #parte imaginaria de Zmr
    Zmr = [0]*len(w) #impedancia mecanica de radiación
    Zmr = [complex(real[i],imag[i]) for i in range(len(imag))] #agrego valores de Zmr 
    
    #se crea una serie de listas de ceros para luego ser sobrescribirlos
    Z = [0]*len(w)
    abs_Z=[0]*len(w)
    for i in range(len(w)):
        real = (Rms/((Bl)**2))+((2*Zmr[i])/((Bl)**2)) #parte real de la Z electrica
        imag = w[i]*(Mms/((Bl)**2))-(1/(w[i]*Cms*((Bl)**2))) #parte imaginaria de la Z electrica
        Z[i] = complex(Rg+Re,w[i]*Le)+(((Bl)**2)/(complex(real,imag))) #impedancia electrica del parlante
        abs_Z[i] = abs(Z[i]) #magnitud de la impedancia electrica
    return f,abs_Z

rho0 = 1.18 
c = 343 

Rg = 0 
Re = 5.2 
Le = 0.5*(10**(-3)) 
Bl=6 
Mms = 0.189 
Rms = 1.0 
Cms = 0.149*(10**(-3)) 
Sd = 0.0154 #superficie efectiva del diafragma [cm2]
D = 140*(10**(-3)) 
a = D/2 
resolucion = 0.01 

f,abs_Z = ImpedanciaParlante(Rg,Re,Le,Bl,Mms,Rms,Cms,a,c,rho0,resolucion)

plt.semilogx(f,abs_Z)

plt.xlim([0.1,20000])
plt.ylabel('Modulo de impedancia electrica [$\Omega$]',size=15)
plt.xlabel('Frecuencia [$Hz$]',size=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.show()
