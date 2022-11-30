# CronScript
THIS IS TRIGGER BY A CRON TIMMER BY FOLLOWING EXPRESSION AND ENV VARIABLE "run this: $crontab -e"
```
#GLOBAL ENVIROMENT
scriptPath=/home/jcpleitez/ues/DataLogger-BestPendientes
# EJECUTAR AL MINUTO 12 CADA HORA
# m h  dom mon dow   command
12 * * * * docker run --rm -v ${scriptPath}:/usr/src/app python-cron python save-best-pendientes.py >> ${scriptPath}/status.log
```
# Build Container
docker build -t python-cron .

# Run in container
scriptPath=/home/jcpleitez/CronScript
docker run --rm -v $(pwd):/usr/src/app python-cron python save-best-pendientes.py >> $(pwd)/status.log

# Liberias
pip install psycopg2-binary
pip install pandas
pip install scipy