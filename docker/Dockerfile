FROM python:3

# Agregando Zona Horario
ENV TZ="America/El_Salvador"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#COPY . .
#CMD [ "python", "./your-daemon-or-script.py" ]