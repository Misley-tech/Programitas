import soundfile as sf
import numpy as np
def ang_2D(audio1,audio2,temperatura,distancia_fuentes):
    """
    Programa que determina el angulo de incidencia de una fuente 
    sobre dos micrófonos en 2D.
        Parameters:
            audio1 (string): audio de uno de los micrófonos
            audio2 (string): audio del otro micrófono
            temperatura (float): temperatura del ambiente
            distancia_fuentes (float): distancia entre micrófonos
        Returns:
            theta (float):  angulo de incidencia (en grados).
    """
    #Aproximación de la velocidad de propagacion del 
    #sonido a partir de la temperatura
    c = 331 + 0.607*temperatura

    #Adaptación del string del nombre de los archivos de audio
    audio1 = str(str(audio1)+str('.wav'))
    audio2 = str(str(audio2)+str('.wav'))

    #Letura de archivos de audio
    data1,fs = sf.read(audio1)
    data2,fs = sf.read(audio2)

    #Detecto el pico maximo de cada archivo
    max_data1=np.argmax(data1)
    max_data2=np.argmax(data2)  

    #Calculo de la diferencia de tiempo de arribo entre fuentes
    tau_muestras = max_data2 - max_data1
    tau = tau_muestras/fs

    #Calculo del angulo de incidencia de la fuente: theta = arcos(tau*c/d)
    arg = (tau*c)/distancia_fuentes
    theta = (180/np.pi)*np.arccos(arg)
    return theta