# CronScript
THIS IS TRIGGER BY A CRON TIMMER BY FOLLOWING EXPRESSION AND ENV VARIABLE
```
# m h  dom mon dow   command
# * * * * * /usr/bin/python3 /home/jcpleitez/CronScript/generate-data.py

scriptPath=/home/jcpleitez/CronScript
* * * * * docker run --rm -v ${scriptPath}:/usr/src/app python-cron python generate-data.py
```

# Build Container
docker build -t python-cron .

# Run in container
scriptPath=/home/jcpleitez/CronScript
docker run --rm -v ${scriptPath}:/usr/src/app python-cron python generate-data.py