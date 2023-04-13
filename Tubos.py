import numpy as np
import matplotlib.pyplot as plt

def TuboCerrado_PosicionFija(Um,rho0,l,x,c):
    """
    Funcion que calcula la magnitud de:
        1) velocidad de las particulas (u) medido en m/s
        2) la presion efectiva (P) [Pa] 
        3) la impedancia acustica especifica (Ze) [ohm_a]=[Pa*s/m3]
    para todo el espectro audible (20 a 20 kHz) en una posición especifica (x) dentro del tubo.
        Entradas:
            Um (float): velocidad que impone el piston
            rho0 (float): densidad del aire
            l (float): largo del tubo cerrado
            x (float): ubicación dentro del tubo
            c (float): velocidad de propagación dentro del tubo       
        Salidas:
            u (list): velocidad de las particulas por frecuencia
            p (list): presion efectiva por frecuencia
            Z (list): impedancia acustica especifica por frecuencia
    """
    f = np.arange(20,20e3,0.1) #array de frecuenias de 20 a 20 kHz
    lambda_ = c/f #longitud de onda de todas las frecuencias de 20 a 20 kHz
    k = 2*np.pi/lambda_ #numero de onda para todas las frecuencias

    #se crea una serie de listas de ceros para luego ser sobrescribirlos
    u = [0]*len(f)
    p = [0]*len(f)
    Z = [0]*len(f)
    for i in range(len(f)):
        u[i] = Um*((np.cos(k[i]*(l-x)))/(np.cos(k[i]*l))) # calculo de vel de las particulas (u)
        p[i] = rho0*c*Um*((np.sin(k[i]*(l-x)))/(np.cos(k[i]*l))) # calculo de presion efectiva (P)
        Z[i] = rho0*c*((np.sin(k[i]*(l-x)))/(np.cos(k[i]*(l-x)))) # calculo de impedancia caracteristica (Ze)
    return u,p,Z

def TuboCerrado_FrecuenciaFija(Um,rho0,l,f,c):
    """
    Funcion que calcula la magnitud de:
        1) velocidad de las particulas (u) medido en m/s
        2) la presion efectiva (P) [Pa] 
        3) la impedancia acustica especifica (Ze) [ohm_a]=[Pa*s/m3]
    para todas las posiciones dentro del tubo para una frecuencia especifica (f).
        Entradas:
            Um (float): velocidad que impone el piston
            rho0 (float): densidad del aire
            l (float): largo del tubo cerrado
            x (float): ubicación dentro del tubo
            c (float): velocidad de propagación dentro del tubo       
        Salidas:
            u (list): velocidad de las particulas por frecuencia
            p (list): presion efectiva por frecuencia
            Z (list): impedancia acustica especifica por frecuencia
    """
    lambda_ = c/f #longitud de onda de todas las frecuencias de 20 a 20 kHz
    k = 2*np.pi/lambda_ #numero de onda para todas las frecuencias

    x = np.arange(0,l,0.0001) #posiciones consideradas dentro del tubo

    #se crea una serie de listas de ceros para luego ser sobrescribirlos
    u = [0]*len(x)
    p = [0]*len(x)
    Z = [0]*len(x)
    for i in range(len(x)):
        u[i] = Um*((np.cos(k*(l-x[i])))/(np.cos(k*l))) # calculo de vel de las particulas (u)
        p[i] = rho0*c*Um*((np.sin(k*(l-x[i])))/(np.cos(k*l))) # calculo de presion efectiva (P)
        Z[i] = rho0*c*((np.sin(k*(l-x[i])))/(np.cos(k*(l-x[i])))) # calculo de impedancia caracteristica (Ze)
    return u,p,Z

# Valores de entrada
Um = 1 
rho0 = 1.18
l = 1
x = 0.5
f = 1000
c = 343 

u_pf,p_pf,Z_pf = TuboCerrado_PosicionFija(Um,rho0,l,x,c)
u_ff,p_ff,Z_ff = TuboCerrado_FrecuenciaFija(Um,rho0,l,f,c)

################## Ploteo posicion fija ##################
fig, axs = plt.subplots(3,2)
axs[0,0].semilogx(u_pf)
axs[0,0].grid()
axs[0,0].set_ylabel('Vel. de particulas [$m/s$]',size=13)
axs[0,0].set_title('Posición fija en x='+str(x)+'m',size=14)
axs[0,0].set_xlim([20,20000])
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)

axs[1,0].semilogx(p_pf)
axs[1,0].grid()
axs[1,0].set_ylabel('Presion [$Pa$]',size=13)
axs[1,0].set_ylim([-8000,8000])
axs[1,0].set_xlim([20,20000])
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)

axs[2,0].semilogx(Z_pf)
axs[2,0].grid()
axs[2,0].set_ylabel('Impedancia específica [$\Omega_a$]',size=13)
axs[2,0].set_xlabel('Frecuencia [$Hz$]',size=13)
axs[2,0].set_ylim([-8000,8000])
axs[2,0].set_xlim([20,20000])
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)

################# Ploteo frecuencia fija #################

axs[0,1].semilogx(u_ff)
axs[0,1].grid()
axs[0,1].set_title('Frecuencia fija en f='+str(f)+' Hz',size=14)
axs[0,1].set_ylim([min(u_ff),max(u_ff)])
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)

axs[1,1].semilogx(p_ff)
axs[1,1].grid()
axs[1,1].set_ylim([min(p_ff),max(p_ff)])
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)

axs[2,1].semilogx(Z_ff)
axs[2,1].grid()
axs[2,1].set_ylim([-8000,8000])
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

def TuboCerrado_PosicionFija(Um,rho0,l,x,c):
    """
    Funcion que calcula la magnitud de:
        1) velocidad de las particulas (u) medido en m/s
        2) la presion efectiva (P) [Pa] 
        3) la impedancia acustica especifica (Ze) [ohm_a]=[Pa*s/m3]
    para todo el espectro audible (20 a 20 kHz) en una posición especifica (x) dentro del tubo.
        Entradas:
            Um (float): velocidad que impone el piston
            rho0 (float): densidad del aire
            l (float): largo del tubo cerrado
            x (float): ubicación dentro del tubo
            c (float): velocidad de propagación dentro del tubo       
        Salidas:
            u (list): velocidad de las particulas por frecuencia
            p (list): presion efectiva por frecuencia
            Z (list): impedancia acustica especifica por frecuencia
    """
    f = np.arange(20,20e3,1) #array de frecuenias de 20 a 20 kHz
    lambda_ = c/f #longitud de onda de todas las frecuencias de 20 a 20 kHz
    k = 2*np.pi/lambda_ #numero de onda para todas las frecuencias

    #se crea una serie de listas de ceros para luego ser sobrescribirlos
    u = [0]*len(f)
    p = [0]*len(f)
    Z = [0]*len(f)
    for i in range(len(f)):
        u[i] = Um*((np.sin(k[i]*(l-x)))/(np.sin(k[i]*l))) # calculo de vel de las particulas (u)
        p[i] = rho0*c*Um*((np.cos(k[i]*(l-x)))/(np.sin(k[i]*l))) # calculo de presion efectiva (P)
        Z[i] = rho0*c*((np.cos(k[i]*(l-x)))/(np.sin(k[i]*(l-x)))) # calculo de impedancia caracteristica (Ze)
    return u,p,Z

def TuboCerrado_FrecuenciaFija(Um,rho0,l,f,c):
    """
    Funcion que calcula la magnitud de:
        1) velocidad de las particulas (u) medido en m/s
        2) la presion efectiva (P) [Pa] 
        3) la impedancia acustica especifica (Ze) [ohm_a]=[Pa*s/m3]
    para todas las posiciones dentro del tubo para una frecuencia especifica (f).
        Entradas:
            Um (float): velocidad que impone el piston
            rho0 (float): densidad del aire
            l (float): largo del tubo cerrado
            x (float): ubicación dentro del tubo
            c (float): velocidad de propagación dentro del tubo       
        Salidas:
            u (list): velocidad de las particulas por frecuencia
            p (list): presion efectiva por frecuencia
            Z (list): impedancia acustica especifica por frecuencia
    """
    lambda_ = c/f #longitud de onda de todas las frecuencias de 20 a 20 kHz
    k = 2*np.pi/lambda_ #numero de onda para todas las frecuencias

    x = np.arange(0,l,0.0001) #posiciones consideradas dentro del tubo

    #se crea una serie de listas de ceros para luego ser sobrescribirlos
    u = [0]*len(x)
    p = [0]*len(x)
    Z = [0]*len(x)
    for i in range(len(x)):
        u[i] = Um*((np.sin(k*(l-x[i])))/(np.sin(k*l))) # calculo de vel de las particulas (u)
        p[i] = rho0*c*Um*((np.cos(k*(l-x[i])))/(np.sin(k*l))) # calculo de presion efectiva (P)
        Z[i] = rho0*c*((np.cos(k*(l-x[i])))/(np.sin(k*(l-x[i])))) # calculo de impedancia caracteristica (Ze)
    return u,p,Z

# Valores de entrada
Um = 1 
rho0 = 1.18
l = 1
x = 0.5
f = 1000
c = 343 

u_pf,p_pf,Z_pf = TuboCerrado_PosicionFija(Um,rho0,l,x,c)
u_ff,p_ff,Z_ff = TuboCerrado_FrecuenciaFija(Um,rho0,l,f,c)

################## Ploteo posicion fija ##################
fig, axs = plt.subplots(3,2)
axs[0,0].semilogx(u_pf)
axs[0,0].grid()
axs[0,0].set_ylabel('Vel. de particulas [$m/s$]',size=13)
axs[0,0].set_title('Posición fija en x='+str(x)+'m',size=14)
axs[0,0].set_xlim([20,20000])
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)

axs[1,0].semilogx(p_pf)
axs[1,0].grid()
axs[1,0].set_ylabel('Presion [$Pa$]',size=13)
axs[1,0].set_ylim([-8000,8000])
axs[1,0].set_xlim([20,20000])
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)

axs[2,0].semilogx(Z_pf)
axs[2,0].grid()
axs[2,0].set_ylabel('Impedancia específica [$\Omega_a$]',size=13)
axs[2,0].set_xlabel('Frecuencia [$Hz$]',size=13)
axs[2,0].set_ylim([-8000,8000])
axs[2,0].set_xlim([20,20000])
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)

################# Ploteo frecuencia fija #################

axs[0,1].semilogx(u_ff)
axs[0,1].grid()
axs[0,1].set_title('Frecuencia fija en f='+str(f)+' Hz',size=14)
axs[0,1].set_ylim([min(u_ff),max(u_ff)])
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)

axs[1,1].semilogx(p_ff)
axs[1,1].grid()
axs[1,1].set_ylim([min(p_ff),max(p_ff)])
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)

axs[2,1].semilogx(Z_ff)
axs[2,1].grid()
axs[2,1].set_ylim([-8000,8000])
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.show()