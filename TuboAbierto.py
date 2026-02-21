from cmath import phase
from math import log10, pi, sin


def frecuencias_resonancia_tubo_abierto(longitud, c=343.0, modos=10):
    """Calcula las frecuencias de resonancia de un tubo abierto-abierto.

    fn = n*c/(2*L), con n = 1, 2, 3...
    """
    return [(n * c) / (2.0 * longitud) for n in range(1, modos + 1)]


def respuesta_presion_tubo_abierto(
    longitud,
    posicion,
    f_min=20.0,
    f_max=20000.0,
    paso_f=1.0,
    c=343.0,
    modos=20,
    amortiguamiento=0.01,
):
    """Calcula la respuesta de presión en frecuencia para un tubo abierto-abierto.

    Modelo modal 1D simplificado:
        H(f) = Σ phi_n(x)^2 / (fn^2 - f^2 + j*2*zeta*fn*f)

    donde:
        phi_n(x) = sin(n*pi*x/L)
        fn = n*c/(2*L)

    Retorna:
        - lista de frecuencias
        - magnitud normalizada en dB
        - fase en radianes
    """
    if not 0.0 <= posicion <= longitud:
        raise ValueError("La posición debe estar entre 0 y la longitud del tubo.")

    frecuencias = []
    f = f_min
    while f <= f_max:
        frecuencias.append(f)
        f += paso_f

    f_res = frecuencias_resonancia_tubo_abierto(longitud=longitud, c=c, modos=modos)

    respuesta = []
    for frecuencia in frecuencias:
        h = 0j
        for n, fn in enumerate(f_res, start=1):
            phi_n = sin((n * pi * posicion) / longitud)
            denominador = complex(fn**2 - frecuencia**2, 2.0 * amortiguamiento * fn * frecuencia)
            h += (phi_n**2) / denominador
        respuesta.append(h)

    max_mag = max(abs(h) for h in respuesta)
    magnitud_db = [20.0 * log10(abs(h) / max_mag) for h in respuesta]
    fase_rad = [phase(h) for h in respuesta]
    return frecuencias, magnitud_db, fase_rad


def main():
    longitud = 1.0
    posicion = 0.35

    frecuencias, presion_db, fase = respuesta_presion_tubo_abierto(
        longitud=longitud,
        posicion=posicion,
        f_min=20,
        f_max=3000,
        paso_f=10,
        modos=20,
        amortiguamiento=0.01,
    )

    resonancias = frecuencias_resonancia_tubo_abierto(longitud=longitud, modos=8)
    print("Frecuencias de resonancia teóricas [Hz]:")
    for i, fr in enumerate(resonancias, start=1):
        print(f"  Modo {i}: {fr:.2f}")

    print("\nMuestra de respuesta de presión (frecuencia, magnitud dB, fase rad):")
    for i in range(0, len(frecuencias), max(1, len(frecuencias) // 10)):
        print(f"  {frecuencias[i]:7.1f} Hz -> {presion_db[i]:7.2f} dB, {fase[i]:7.3f} rad")


if __name__ == "__main__":
    main()
