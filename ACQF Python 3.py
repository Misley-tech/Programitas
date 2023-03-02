# "Autocorrelación de secuencias difusoras" 
# Adaptacion de Emmanuel Misley y Pablo Rodriguez del codigo de Alejandro Bidondo realizado en Matlab, 
# para la materia "Instrumentos y Mediciones Acusticas" de ingenieria de sonido UNTREF.   
import numpy as np
import pandas as pd

def ACQF(a):    
    """
    Esta función calcula la autocorrelación de una lista de python
        Entradas:
            a (list): lista o array a la que se le quiere calcular la autocorrelación
        
        Salidas:
            ACQF (float): entrega el valor de la autocorrelación
    """
    mean = np.mean(a) #calculo de la media
    var = np.var(a) #calculo de la varianza
    normdata = a-mean #aplicacion de biasado a la lista
    acorr = np.correlate(normdata,normdata,mode='full')[len(normdata)-1:] #calculo de la autocorrelacion
    acorr = acorr / var / len(normdata) #normalizacion de la correlacion
    ACQF = 10*np.log10(np.sqrt(sum(acorr**2))) #calculo de valor rms
    return ACQF

def busqueda(t,min,max,cant_celdas,prof_max,ndif):
    """
    Funcion que genera listas de enteros hasta encontrar la primer secuencia que cumpla con el umbral elegido.
        Entradas:
            t (float): umbral de buscado para la autocorrelación (0<t<1).
            min (int): minimo valor de profundidad. Valor recomendado min=1 (no poner 0 porque sino la regla de tres simple no funciona)
            max (int): maximo valor de profundidad. Valor recomendado min=10
            cant_celdas (int): cantidad de celdas que tiene el difusor
            prof_max (int): profundidad maxima que tiene el difusor en metros (ej.: prof_max=0.6)
            ndif (int) : cantidad de niveles de profundidad del difusor (ej.: ndif=5). Observación: para valores de ndif<=3 puede tardar varios segundos.
        Salidas:
            mensaje (str): texto que indica el valor de ACQF, la profundidad de cada celda en cm y la cantidad de niveles de profundidad.
    """
    S=1 #condicion inicial del peor difusor posible (ACQF=1)
    niveles = 1e100 # difusor con la mayor cantidad de niveles de profundidad posible
    while ndif<=niveles:
        S=1
        while S>t:
            secuencia=np.random.randint(min,max,size=cant_celdas,dtype=int) #generacion de lista de enteros
            S = ACQF(secuencia) #calculo de la autocorrelacion
        secuencia = pd.Series(secuencia) #se convierte a la secuencia en un panda series
        niveles = secuencia.nunique() # se cuenta la cantidad de elementos iguales que tiene la secuencia
        if ndif>niveles: #pido que la cantidad de niveles de profundidad sea menor a ndif
            secuencia_cm=min*(prof_max/max)*secuencia*100 #se aplica la regla de tres simple para pasar de unidades a cm
            secuencia = pd.Series.tolist(secuencia)  # se castea la variable de un panda series a una lista
            secuencia_cm = pd.Series.tolist(secuencia_cm) # idem
            salida = f"El valor de ACQF es {str(round(S,4))} y la secuencia es {secuencia}, en centimetros es {secuencia_cm} y la cantidad de niveles de profundidad es de {niveles}."
            return salida

#Ejemplo:
#print(busqueda(0.4,1,10,15,0.6,5))
