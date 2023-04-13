import cmath
import numpy as np
import matplotlib.pyplot as plt
import cmath

def D_dipolo(c,f,b,resolucion_angular):
    """
    Funcion que calcula la funcion de directividad de dos fuentes puntuales que vibran en fase.
        Entradas:
        c (float): velocidad de propagación del sonido
        f (float): frecuencia a la que vibran las fuentes puntuales
        b (float): distancia entre fuentes puntuales
        resolucion_angular (float): minimo angulo de representacion

        Salida:
        theta (ndarray): vector de resolucion angular
        directivity_function (ndarray): directividad de la fuente
    """
    lambda_ = c/f #def de longitud de onda
    k = (2*np.pi)/lambda_ # def de numero de onda

    theta = np.arange(0,2*np.pi,resolucion_angular) #ndarray de angulos

    directivity_function = np.cos(((2*np.pi*b)/lambda_)*np.sin(theta)) #calculo de la funcion de diretividad D(theta)
    # el 2 dentro del argumento del coseno no deberia estar, pero si no lo pongo da la mitad de frecuencia que en el Beranek
    return theta,directivity_function

def D_linearray(c,f,d,resolucion_angular,N): 
    """
    Función que calcula la función de directividad para un arreglo lineal 
    de fuentes sonoras puntuales.
        Entradas:
        c (float): velocidad de propagación del sonido
        f (float): frecuencia a la que vibran las fuentes puntuales
        d (float): distancia entre fuentes puntuales
        resolucion_angular (float): minimo angulo de representacion
        N (int): cantidad de fuentes del array

        Salidas:
        theta (ndarray): vector de resolucion angular
        directivity_function (ndarray): directividad de la fuente
    """
    b = d/(N-1)
    lambda_= c/f
    k = (2*np.pi)/lambda_

    theta = np.arange(0,2*np.pi,resolucion_angular)

    num = np.sin(((N*np.pi*b)/lambda_)*np.sin(theta))
    den = N*np.sin(((np.pi*b)/lambda_)*np.sin(theta))
    directivity_function = num/den

    return theta,directivity_function

def D_linearray_continuo(c,f,d,resolucion_angular,N):
    """
    Función que calcula la función de directividad para un arreglo lineal
    formado por infinitas fuentes (N infinito) y con una distancia entre fuentes
    de 0 (b=0).
        Entradas:
        c (float): velocidad de propagación del sonido
        f (float): frecuencia a la que vibran las fuentes puntuales
        d (float): distancia entre fuentes puntuales
        resolucion_angular (float): minimo angulo de representacion
        N (int): cantidad de fuentes del array

        Salidas:
        theta (ndarray): vector de resolucion angular
        directivity_function (ndarray): directividad de la fuente
    """
    b = d/(N-1)
    lambda_= c/f
    k = (2*np.pi)/lambda_

    theta = np.arange(0,2*np.pi,resolucion_angular)

    num = np.sin(((np.pi*d)/lambda_)*np.sin(theta))
    den = ((np.pi*d)/lambda_)*np.sin(theta)
    directivity_function = num/den

    return theta,directivity_function

def D_beamforming(c,f,d,resolucion_angular,N,alfa):
    """
    Función que calcula la función de directividad para un arreglo lineal  
    un beamforming dirijido (steered beamforming) de fuentes sonoras puntuales
        Entradas:
        c (float): velocidad de propagación del sonido
        f (float): frecuencia a la que vibran las fuentes puntuales
        d (float): distancia entre fuentes puntuales
        resolucion_angular (float): minimo angulo de representacion
        N (int): cantidad de fuentes del array
        alfa (float): angulo de direccionamiento (steering angle)

        Salidas:
        theta (ndarray): vector de resolucion angular
        directivity_function (ndarray): directividad de la fuente
    """
    b = d/(N-1)
    lambda_= c/f
    k = (2*np.pi)/lambda_
    alfa = alfa*(np.pi/180)

    theta = np.arange(0,2*np.pi,resolucion_angular)
    
    num = np.sin(((N*np.pi*b)/lambda_)*(np.cos(theta)-np.cos(alfa)))
    den = N*np.sin(((np.pi*b)/lambda_)*(np.cos(theta)-np.cos(alfa)))
    
    directivity_function = num/den

    return theta,directivity_function

def D_beamforming_LeastMeanSquares(c,f,d,resolucion_angular,N,alfa,An):
    """
    Función que calcula la función de directividad para un arreglo lineal  
    un beamforming dirijido (steered beamforming) de fuentes sonoras puntuales
        Entradas:
        c (float): velocidad de propagación del sonido
        f (float): frecuencia a la que vibran las fuentes puntuales
        d (float): distancia entre fuentes puntuales
        resolucion_angular (float): minimo angulo de representacion
        N (int): cantidad de fuentes del array
        alfa (float): angulo de direccionamiento (steering angle)
        An (list): lista que atenua/amplifica la señal que emite cada fuente, esto permite optimizar la directividad de la fuente (metodo de least mean squares) 

        Salidas:
        theta (ndarray): vector de resolucion angular
        directivity_function (ndarray): directividad de la fuente
    """
    b = d/(N-1)
    lambda_= c/f
    k = (2*np.pi)/lambda_
    alfa = alfa*(np.pi/180)    

    theta = np.arange(0,2*np.pi,resolucion_angular)
    sum = 0
    for n in range(1,N//2+1,1):   
        sum += An[n-1]*np.cos((n-0.5)*k*b*(np.cos(theta)-np.cos(alfa)))
    directivity_function = (2/N)*sum

    return theta,directivity_function

def respuesta_presion(c,f,rho0,U,r,theta,directivity_function):
    lambda_ = c/f
    k = (2*np.pi)/lambda_
    A = complex(0,(k*rho0*c*U)/(4*np.pi))
    p = (2/r)*A*cmath.exp(0,-1*k*r)*directivity_function
    return theta,p

c=343
f=1000
# d=c/f
b = c/f
resolucion_angular=0.01
N=10
alfa=60
An = [1,2,1,2]

x = np.linspace(0,10,100)
x = np.delete(x,0)

for i in range(len(x)):
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection='polar')
    theta,directivity_function=D_beamforming_LeastMeanSquares(c,f,b*x[i],resolucion_angular,N,alfa,An)
    ax.plot(theta, directivity_function, label=f'{round(x[i],2)}$\lambda$')
    plt.title(r'Directividad de un $beamforming$ LMS ($N=10$,$\alpha=60^{\circ}$,$A_{n} = [1,2,1,2]$)', fontsize=12)
    ax.set_xticklabels(['0°','45°','90°','135°','180°','225°','270°','315°'],fontsize=15)
    legend = ax.legend(loc='upper right', shadow=True, fontsize='xx-large')
    plt.savefig(f'C:/Users/Asus/Desktop/programitas/SimuladorLineArray/GIFs/IMG_beamforming_lms/{i}.png')
    ax.legend([])