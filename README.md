# CronScript
THIS IS TRIGGER BY A CRON TIMMER BY FOLLOWING EXPRESSION
```
m h  dom mon dow   command
* * * * * /usr/bin/python3 /home/jcpleitez/CronScript/generate-data.py
```

# Build Container
docker build -t python:cronscript .

# Run in container
docker run --rm -v ${PWD}:/usr/src/app python:cronscript python generate-data.py