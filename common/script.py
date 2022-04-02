# Time, Truncado la fecha de inicio y fin primeros 10 minutos de cada hora
from datetime import timedelta, datetime
dt = datetime.now()
fechaInicio = dt.replace(minute=0, second=0, microsecond=0)
fechaFin = fechaInicio + timedelta(minutes=10)

def getFechaInicio():
    return fechaInicio
def getFechaFin():
    return fechaFin