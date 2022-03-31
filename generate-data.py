# Time
from datetime import datetime
from pytz import timezone

# Zona horario de El Salvador
tz = timezone('America/El_Salvador')
dt = datetime.now(tz)

# Truncado la fecha de inicio y fin primeros 10 minutos de cada hora
fechaInicio = dt.replace(minute=0, second=0, microsecond=0)
fechaFin = dt.replace(minute=10, second=0, microsecond=0)

print("fechaInicio", fechaInicio.strftime('%Y-%m-%d_%H-%M-%S'))
print("fechaFin", fechaFin.strftime('%Y-%m-%d_%H-%M-%S'))

# Postgres
import psycopg2
