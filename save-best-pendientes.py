import common.script as com
import postgres.script as pos

# Initial Configuration for Postgres
pos.iniConfigs("environment.ini")#pos.test()

# Generalidades
idInvestigacion = 1
idDispositivo = 1
fechaInicio = com.getFechaInicio().strftime('%Y-%m-%d %H:%M:%S')
fechaFin = com.getFechaFin().strftime('%Y-%m-%d %H:%M:%S')
print("fechaInicio\t", fechaInicio, "\nfechaFin\t", fechaFin)


# OBTENER LOS DATOS Y PROCESARLOS 
# columna 1 nombre de la grafica a generar (H2S-SO2)(H2-SO2)(CO2-SO2)(CO2-H2S)(H2O-SO2)
# columna 2 numero de columna de variable 1
# columna 3 numero de columna de variable 2
relacionGraficos = [
    ["CO2-H2O", 15, 14],
    ["H2S-SO2", 17, 18],
    ["H2-SO2",  16, 17],
    ["CO2-SO2", 15, 17],
    ["CO2-H2S", 15, 17],
    ["H2O-SO2", 14, 17]
]

for datosGrafico in range(relacionGraficos):
    # Se setea el nombre del grafico
    nombreGrafico = datosGrafico[0]
    # EJE X data que corresponde a la columna
    ejeX = maindata(datosGrafico[1])
    # EJE Y data que corresponde a la columna
    ejeY = maindata(datosGrafico[2])
    

    # Creacion de la Query por cada uno de los graficos
    query = "INSERT INTO historico(id_investigacion, id_dispositivo, fecha_inicio, fecha_fin, nombre, pendiente, constante, coeficiente_correlacion, descripcion) "
    query += "VALUES ({}, {}, '{}', '{}', {}, {}, {}, {}, {})".format(
        idInvestigacion,
        idDispositivo,
        fechaInicio.strftime('%Y-%m-%d %H:%M:%S'),
        fechaFin.strftime('%Y-%m-%d %H:%M:%S'),
        nombreGrafico,
        pendiente,
        constante,
        coeficiente_correlacion,
        descripcion
    )
    # Enviar la data y guardarla en logs
    pos.runQuery(query)
    print(query)