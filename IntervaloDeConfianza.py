import numpy as np
from scipy.stats import norm, t, chi2
import matplotlib.pyplot as plt

def IEsperanzaPoblacionNormalVarianzaConocida(data,sigma,nivel):
    X_prom = np.mean(data)
    alfa=1-nivel
    z_alfa2 = -norm.ppf(alfa/2)
    n = len(data)
    error = z_alfa2*(sigma/n**0.5)
    minimo = X_prom-error
    maximo = X_prom+error
    return [minimo,maximo]

def IEsperanzaPoblacionNormalVarianzaDesconocida(data,nivel):
    X_prom = np.mean(data)
    s = np.std(data,ddof=1)
    alfa=1-nivel
    n = len(data)
    t_alfa2 = -t.ppf(alfa/2,df=n-1)
    error = t_alfa2*(s/n**0.5)
    minimo = X_prom-error
    maximo = X_prom+error
    return [minimo,maximo]

def IVarianzaPoblacionNormal(data,nivel):
    n = len(data)
    s = np.std(data,ddof=1)
    alfa=1-nivel
    a = chi2.ppf(alfa/2, df=n-1)
    b = chi2.ppf(1 - alfa/2, df=n-1)
    minimo = ((n-1)*s**2)/b
    maximo = ((n-1)*s**2)/a
    print([minimo,maximo])

def IMedia(data,nivel):
    X_prom = np.mean(data)
    n = len(data)
    alfa=1-nivel
    s = np.std(data,ddof=1)
    z_alfa2 = norm.ppf(alfa/2)
    error = z_alfa2*(s/n**0.5)
    minimo = X_prom-error
    maximo = X_prom+error    
    return [minimo,maximo]

def IProporciones(data,nivel):
    X_prom = np.mean(data)
    n = len(data)
    alfa=1-nivel
    z_alfa2 = -norm.ppf(alfa/2)    
    error = z_alfa2*((X_prom*(1-X_prom))**0.5/(n**0.5))
    minimo = X_prom-error
    maximo = X_prom+error
    return [minimo,maximo]

# def PlotPNG():
#     a = r'\int_{-\infty}^{\infty} e^{-x^{2}} \ dx'
#     b = r'\sum_{i=1}^{\infty}'

#     ax = plt.axes([0.3,0,0,1]) #left,bottom,width,height
#     ax.set_xticks([])
#     ax.set_yticks([])
#     ax.axis('off')
#     plt.text(0,0.5,'$%s$' %a,size=20)
#     plt.text(0,0.2,'$%s$' %b,size=20)
#     plt.savefig('foo.png',dpi=199)

# PlotPNG()