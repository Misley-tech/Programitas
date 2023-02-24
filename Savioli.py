import numpy as np
import matplotlib.pyplot as plt

def SavioliDoble(densidad1,densidad2,e1,e2,d,f,material,sup_divisoria):
    """
    Función que calcula el transmision loss de un panel doble con cavidad de aire.
        Entradas:
            densidad1(float): densidad del material 1 del panel
            densidad2(float): densidad del material 2 del panel
            e1(float): espesor del material 1
            e2(float): espesor del material 2
            d(float): profundidad de la cavidad de aire 
            f(list): banda de frecuencias
            material(string): tipo de material que componen al panel: 'no sonoro' y 'sonoro' (con minuscula). Si el material es sonoro se restan -5dB al TL final, si es no sonoro no se resta nada
            sup_divisoria(): superficie que divide la habitación A de la B 
        Salidas:
            TL_savioli(list): entrega el TL segun Savioli para cada frecuencia pedida
    """
    ms1 = densidad1 * e1 #calcula masa superficial del material 1
    ms2 = densidad2 * e2 #calcula masa superficial del material 2
    f0 = 60*((1/d)*(1/ms1 + 1/ms2))**(1/2) #calcula la frecuencia de resonancia del panel
    ms = ms1 + ms2 #masa superficial resultante para f0
    ######## Ajustes de Savioli ########
    if material == 'no sonoro':
        ajuste_material = 0
    elif material == 'sonoro':
        ajuste_material = -5
    else:
        return 'escribilo bien master'
    
    #Savioli provee tres valores de referencia para corregir por el el temaño de la superficie divisora
    #estos valores son 4m2 --> 0 dB, 8m2 --> 3 dB y 16m2 --> 6 dB. Estos valores son los que se utilizan
    #para trazar una regresión logaritmica
    [alfa,beta] = np.polyfit(np.log([4,8,16]),[0,3,6],1) #Calculo de regresion log
    ajuste_sup_divisoria = alfa*np.log(sup_divisoria)+beta #prediccion del ajuste para la sup divisoria ingresada
    ajuste_sup_divisoria = round(ajuste_sup_divisoria,1) #redondeado del ajuste
    ajuste_detalles_constructivos = -12 #ajuste debido a detalles constructivos 

    ######## Calculo de TL ########
    TL = 20*np.log10(ms*f0)-42 #Aplicación de la ley de masas para una incidencia normal, c=343 m/s, rho=1,18 kg/m3
    TL_savioli_f0 = TL+ajuste_detalles_constructivos+ajuste_material-ajuste_sup_divisoria #TL final segun savioli luego de aplicar las correcciones
    TL_savioli = [0]*len(f) #lista de ceros de largo igual a f
    frec = [0]*len(f) #lista de ceros de largo igual a f
    for i in range(len(f)):
        if i==0:
            TL_savioli[0] = TL_savioli_f0 
            frec[0] = f0 
        elif i==1:
            TL_savioli[1] = TL_savioli_f0 + 8 
            frec[1] = 2*f0 
        else:
            TL_savioli[i] = TL_savioli[i-1] + 8 
            frec[i] = 2*frec[i-1]
    #Como no se tienen los valores exactos de las frecuencias centrales de tercio y octava
    #se traza una regresion logaritmica para poder predicir el aislamiento para las frecuencias
    #que se necesiten
    [a,b] = np.polyfit(np.log(frec), TL_savioli,1) #coeficientes de la regresion log
    TL_savioli = a*np.log(f)+b #prediccion
    for i in range(len(TL_savioli)):
        TL_savioli[i] = round(TL_savioli[i],1) #redondeo de todos los valores de TL recibidos
    return TL_savioli

f=[31.5,63,125,250,500,1000,2000,4000]
densidad1=2300
densidad2=1600
e1=0.15
e2=0.3
d=0.1
material='no sonoro'
sup_divisoria=8
print(SavioliDoble(densidad1,densidad2,e1,e2,d,f,material,sup_divisoria))