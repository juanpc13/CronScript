# Time, Truncado la fecha de inicio y fin primeros 10 minutos de cada hora
from datetime import timedelta, datetime
import pytz
salvadorTz = pytz.timezone("America/El_Salvador") 
dt = datetime.now(salvadorTz)
fechaInicio = dt.replace(minute=0, second=0, microsecond=0)
fechaFin = fechaInicio + timedelta(minutes=59, seconds=59)

##REMOVE THIS WHEN YOUR SURE "PLEITEZ"
#PROCESS OLD
fechaInicio = fechaInicio - timedelta(hours=1)
fechaFin = fechaFin - timedelta(hours=1)
######################################

def getFechaInicio():
    return fechaInicio
def getFechaFin():
    return fechaFin
def getCurrentMinute():
    return dt.replace(second=0, microsecond=0)

# PRINT FOR LOGS
print("LOG----------" + dt.strftime('%Y-%m-%d %H:%M:%S') + "----------")