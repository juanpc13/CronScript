import pandas as pd
from datetime import datetime, timedelta
import common.script as com
import postgres.script as pos
import mathematics.script as mat

# Initial Configuration for Postgres
path = "/home/jcpleitez/ues/DataLogger-BestPendientes/"
pos.iniConfigs(path + "environment.ini")  # pos.test()

# Rutuna contiene todas las DATA A GENERAR, POR CADA UNO OBTEBER SU MEJOR PENDIENTE Y GUARDARLA EN LA BD
query = pos.getQueryRutinas()
rutinas = pos.queryFetchAll(query)
for rutina in rutinas:
    
    # ID de la investigacion 3 es la multigas
    idInvestigacion = str(rutina[1])
    id_dispositivo = str(rutina[2])
    index_x = rutina[6]
    index_y = rutina[7]
    label_x = rutina[10]
    label_y = rutina[11]
    # AUN NO IMPLEMENTADAS EN DB
    index_date = 3
    secondSteps = 60

    # Fechas a DateTime
    formatoFecha = '%Y-%m-%d %H:%M:%S'
    fecha1 = com.getFechaInicio()
    fecha2 = com.getFechaFin()
    #TEST
    #fecha1 = "2022-11-01 00:00:00"    #@param {type:"string"}
    #fecha2 = "2022-11-01 00:59:59"    #@param {type:"string"}
    #fecha1 = datetime.strptime(fecha1, formatoFecha)
    #fecha2 = datetime.strptime(fecha2, formatoFecha)

    # MAIN INVEST
    bestCorrelation = {"correlacion":None, "xArray":None, "yArray":None, "since":None, "to":None}

    # Iterar cada intervalo
    currentTime = fecha1
    while currentTime < fecha2:
        #Next Date
        nextDate = currentTime + timedelta(seconds=secondSteps)

        # Se obtiene Data
        ejeFecha, ejeX, ejeY = pos.buildData(idInvestigacion, id_dispositivo, index_date, index_x, index_y, currentTime.strftime(formatoFecha), nextDate.strftime(formatoFecha))

        # Se valida y se continua
        if len(ejeFecha) > 0:
            # Guardar en mainData si esta None
            if bestCorrelation["correlacion"] == None:
                bestCorrelation["correlacion"] = mat.getCoeficienteRelacion(ejeX, ejeY)
                bestCorrelation["xArray"] = ejeX
                bestCorrelation["yArray"] = ejeY
                bestCorrelation["since"] = ejeFecha.iloc[0]
                bestCorrelation["timeB"] = ejeFecha.iloc[-1]
            else:
                tempCorrelacion = mat.getCoeficienteRelacion(ejeX, ejeY)
                if tempCorrelacion > bestCorrelation["correlacion"]:
                    bestCorrelation["correlacion"] = tempCorrelacion
                    bestCorrelation["xArray"] = ejeX
                    bestCorrelation["yArray"] = ejeY
                    bestCorrelation["since"] = ejeFecha.iloc[0]
                    bestCorrelation["to"] = ejeFecha.iloc[-1]
        
        # Aumentar fecha con secondSteps
        currentTime = nextDate

    # Graficar Coeficiente de Relacion y Guardar
    fileName = path + "www/resultados/" + label_x + "-" + label_y + "-" + fecha1.strftime('%d-%m-%Y_%H') + ".png"
    if bestCorrelation["correlacion"] != None:
        tittle = "("+str(bestCorrelation["since"]) + "|" + str(bestCorrelation["to"])+")"
        mat.genGraf(fileName, tittle, label_x, label_y, bestCorrelation["xArray"], bestCorrelation["yArray"])
        # LOGS
        print("OK = ", fileName)
    else:
        # LOGS
        print("FAIL = ", fileName)