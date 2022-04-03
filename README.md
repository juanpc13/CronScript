# CronScript
THIS IS TRIGGER BY A CRON TIMMER BY FOLLOWING EXPRESSION AND ENV VARIABLE "run this: $crontab -e"
```
# m h  dom mon dow   command
# * * * * * /usr/bin/python3 /home/jcpleitez/CronScript/generate-data.py

# EJECUTAR LOS PRIMEROS 10 MINUTOS DE CADA HORA
scriptPath=/home/jcpleitez/CronScript
0-9 * * * * docker run --rm -v ${scriptPath}:/usr/src/app python-cron python generate-data.py

# EJECUTAR AL MINUTO 10 CADA HORA
scriptPath=/home/jcpleitez/CronScript
10 * * * * docker run --rm -v ${scriptPath}:/usr/src/app python-cron python save-best-pendientes.py >> ${scriptPath}/status.log
```

# Build Container
docker build -t python-cron .

# Run in container
scriptPath=/home/jcpleitez/CronScript
docker run --rm -v ${scriptPath}:/usr/src/app python-cron python generate-data.py >> ${scriptPath}/status.log