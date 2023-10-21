import csv

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        with open(self.nombre_archivo, "r") as archivo:
            reader = csv.reader(archivo, delimiter=",")
            next(reader, None)  # Salta la cabecera

            temperaturas = []
            humedades = []
            presiones = []
            velocidades_viento = []
            direcciones_viento = []

            for registro in reader:
                temperaturas.append(float(registro[5]))
                humedades.append(float(registro[6]))
                presiones.append(float(registro[7]))
                velocidades_viento.append(float(registro[8]))
                direcciones_viento.append(registro[9])

            temperatura_promedio = sum(temperaturas) / len(temperaturas)
            humedad_promedio = sum(humedades) / len(humedades)
            presion_promedio = sum(presiones) / len(presiones)
            velocidad_viento_promedio = sum(velocidades_viento) / len(velocidades_viento)

            direcciones_viento_grados = [angulo_a_grados(direccion) for direccion in direcciones_viento]
            direccion_promedio_grados = sum(direcciones_viento_grados) / len(direcciones_viento_grados)
            direccion_promedio = grados_a_direccion(direccion_promedio_grados)

            return temperatura_promedio, humedad_promedio, presion_promedio, velocidad_viento_promedio, direccion_promedio


def angulo_a_grados(direccion: str) -> float:
    if direccion == "N":
        return 0
    elif direccion == "NNE":
        return 22.5
    elif direccion == "NE":
        return 45
    elif direccion == "ENE":
        return 67.5
    elif direccion == "E":
        return 90
    elif direccion == "ESE":
        return 112.5
    elif direccion == "SE":
        return 135
    elif direccion == "SSE":
        return 157.5
    elif direccion == "S":
        return 180
    elif direccion == "SSW":
        return 202.5
    elif direccion == "SW":
        return 225
    elif direccion == "WSW":
        return 247.5
    elif direccion == "W":
        return 270
    elif direccion == "WNW":
        return 292.5
    elif direccion == "NW":
        return 315
    elif direccion == "NNW":
        return 337.5
    else:
        raise ValueError(f"La dirección del viento no es válida: {direccion}")


def grados_a_direccion(grados: float) -> str:
    if 0 <= grados < 22.5:
        return "N"
    elif 22.5 <= grados < 45:
        return "NNE"
    elif 45 <= grados < 67.5:
        return "NE"
    elif 67.5 <= grados < 90:
        return "ENE"
    elif 90 <= grados < 112.5:
        return "E"
    elif 112.5 <= grados < 135:
        return "ESE"
    elif 135 <= grados < 157.5:
        return "SE"
    elif 157.5 <= grados < 180:
        return "SSE"
    elif 180 <= grados < 202.5:
        return "S"
    elif 202.5 <= grados < 225:
        return "SSW"
    elif 225 <= grados < 247.5:
        return "SW"
