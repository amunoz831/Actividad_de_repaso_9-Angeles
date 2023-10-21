
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
