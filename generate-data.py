import common.script as com
import postgres.script as pos

# Initial Configuration for Postgres
pos.iniConfigs("environment.ini")
pos.test()

# Dates
fechaInicio = com.getFechaInicio()
fechaFin = com.getFechaFin()
print("fechaInicio", fechaInicio.strftime('%Y-%m-%d_%H-%M-%S'))
print("fechaFin", fechaFin.strftime('%Y-%m-%d_%H-%M-%S'))

