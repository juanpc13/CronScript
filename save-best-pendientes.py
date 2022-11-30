import pandas as pd
from datetime import datetime, timedelta
import common.script as com
import postgres.script as pos
import mathematics.script as mat

# Initial Configuration for Postgres
pos.iniConfigs("environment.ini")  # pos.test()

# ID de la investigacion 3 es la multigas
idInvestigacion = "1000"  # @param {type:"string"}
id_dispositivo = "1000"  # @param {type:"string"}
# fecha1 = "2022-11-01 00:00:00"    #@param {type:"string"}
# fecha2 = "2022-11-01 01:00:00"    #@param {type:"string"}
intervalo = 60  # @param {type:"number"}


formatoFecha = '%Y-%m-%d %H:%M:%S'
# Generalidades Globales
startDay = datetime.strptime('2022-11-01 00:00:00', formatoFecha)
endDay = datetime.strptime('2022-11-01 23:59:59', formatoFecha)
iteDay = startDay

# Loop dias
while iteDay <= endDay:
    # Loop horas
    starHour = iteDay
    endHour = starHour + timedelta(hours=23)
    iteHour = starHour
    # MAIN INVEST
    mainData = {"correlacion": None, "xArray": None,
                "yArray": None, "timeA": None, "timeB": None}
    while iteHour < endHour:
        # APP
        #print(iteHour, iteHour + timedelta(hours=1))

        # Generar query iterada
        mainQuery = pos.queryMainData(idInvestigacion, id_dispositivo, iteHour.strftime(
            formatoFecha), (iteHour + timedelta(seconds=intervalo)).strftime(formatoFecha))

        # Obtener el DataFrame iterado
        mainDataFrame = pd.read_sql_query(mainQuery, con=pos.getConnection())

        # Validar DataFrame
        if len(mainDataFrame) == 0:
            iteHour = iteHour + timedelta(hours=1)
            continue

        # Separar Ejes Fecha, X y Y
        ejeFecha = mainDataFrame.iloc[:, 3]
        ejeX = mainDataFrame.iloc[:, 12]
        ejeY = mainDataFrame.iloc[:, 14]

        # Obetener la mejor correlacion
        # Guardar en mainData si esta None
        if mainData["correlacion"] == None:
            mainData["correlacion"] = mat.getCoeficienteRelacion(ejeX, ejeY)
            mainData["xArray"] = ejeX
            mainData["yArray"] = ejeY
            mainData["timeA"] = ejeFecha.iloc[0]
            mainData["timeB"] = ejeFecha.iloc[-1]
        else:
            tempCorrelacion = mat.getCoeficienteRelacion(ejeX, ejeY)
            if tempCorrelacion > mainData["correlacion"]:
                mainData["correlacion"] = tempCorrelacion
                mainData["xArray"] = ejeX
                mainData["yArray"] = ejeY
                mainData["timeA"] = ejeFecha.iloc[0]
                mainData["timeB"] = ejeFecha.iloc[-1]

        # Generate and Save Image
        filename = iteHour.strftime('%Y-%m-%d-%H') + ".png"
        titulo = "H2O/CO2" + "("+str(mainData["timeA"]) + "|" + str(mainData["timeB"])+")"
        mat.genGraf(filename, titulo, "H2O", "CO2", mainData["xArray"], mainData["yArray"])

        # Avanazar en minutos
        iteHour = iteHour + timedelta(hours=1)
        
    # Avanzar en dias
    iteDay = iteDay + timedelta(days=1)
