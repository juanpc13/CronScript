import common.script as com
import postgres.script as pos

# Initial Configuration for Postgres
pos.iniConfigs("environment.ini")#pos.test()

# Fechas
from datetime import timedelta
start_date  = com.getCurrentMinute()
end_date    = start_date + timedelta(minutes=1)
print("start_date\t", start_date, "\tTO\end_date\t", end_date)

pos.startQueue()
import random
while start_date < end_date:
    # Se genera 1 registro
    query = "INSERT INTO maindata(id_investigacion, id_dispositivo, fecha_registrada, humedad, dioxido_carbono, hidrogeno, acido_sulfhidrico, dioxido_azufre) "
    query += "VALUES (1, 1, '{}', {}, {}, {}, {}, {})".format(
        start_date.strftime('%Y-%m-%d %H:%M:%S'),
        random.randint(150000, 600000)/10.0,
        random.randint(4000, 7000)/10.0,
        random.randint(50, 150)/10.0,
        random.randint(100, 400)/10.0,
        random.randint(1, 20)/10.0
    )
    pos.addQueue(query)
    # Se continua al siguente segundo del datetime
    start_date += timedelta(seconds=1)
pos.endQueue()