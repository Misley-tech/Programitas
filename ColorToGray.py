import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def ColorToGray(ubicacion,cantidad_imagenes):
    """
    Convierte un serie de imagenes de png a escala de grises     
        Entradas:
            ubicacion (str): path de los archivos png sin la dirección que indica el nombre del archivo y la extension. Ejemplo: ubicacion=C:/Users/Asus/Desktop/SegundoEdu/Segundo/ColorToGray
            cantidad_imagenes (int): cantidad de imagenes a convertir. Ejemplo: cantidad_imagenes=28
        Salida:
            imagenes en escala de grises
    """
    for i in range(1,cantidad_imagenes+1):
        img = Image.open(f'{ubicacion}/{i}.png')
        imggray = img.convert('LA')

        imgmat = np.array(list(imggray.getdata(band=0)), float)
        imgmat.shape = (imggray.size[1], imggray.size[0])
        imgmat = np.matrix(imgmat)
        plt.imshow(imgmat, cmap='gray')
        plt.axis('off')

        plt.savefig(f'C{i}.png')

#Ejemplo
# ubicacion = 'C:/Users/Asus/Desktop/SegundoEdu/Segundo/ColorToGray'
# cantidad_imagenes = 28
# ColorToGray(ubicacion,cantidad_imagenes)

