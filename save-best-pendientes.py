import common.script as com
import postgres.script as pos
import mathematics.script as mat

# Initial Configuration for Postgres
pos.iniConfigs("environment.ini")#pos.test()

# Generalidades Globales
fecha_inicio = com.getFechaInicio().strftime('%Y-%m-%d %H:%M:%S')
fecha_fin = com.getFechaFin().strftime('%Y-%m-%d %H:%M:%S')

# Rutuna contiene todas las DATA A GENERAR, POR CADA UNO OBTEBER SU MEJOR PENDIENTE Y GUARDARLA EN LA BD
query = pos.getQueryRutinas()
rutinas = pos.queryFetchAll(query)

for rutina in rutinas:
    ########GENERALIDADES DE LA RUTINA A GENERAR########
    # Id Rutina
    id_rutina = rutina[0]
    # Id Investigacion
    id_investigacion = rutina[1]
    # Id Dispositivo
    id_dispositivo = rutina[2]
    # Se setea el nombre del grafico
    nombre = rutina[3]

    # Se genera la QUERY para obtener la maindata a procesar
    query = pos.getQueryMainData(id_investigacion, id_dispositivo, fecha_inicio, fecha_fin)
    maindata = pos.getDataFrameQuery(query)

    # EJE X data que corresponde a la columna
    index = rutina[4]
    ejeX = maindata.iloc[:, index]
    # EJE Y data que corresponde a la columna
    index = rutina[5]
    ejeY = maindata.iloc[:, index]

    # FALTA IMPLEMENTAR LOS MULTIPLICADORES

    # Se calcula todo lo necesario para la regresion
    pendiente, intercepto, coeficiente_correlacion, p, stderr = mat.regresionLineal(ejeX, ejeY)
    descripcion = f'Regresion Lineal: Y = {intercepto:.3f} + {pendiente:.3f}X, R={coeficiente_correlacion:.3f}'

    # Creacion de la Query por cada uno de los graficos
    constante = intercepto
    query = pos.getQueryHistorico(id_rutina, nombre, fecha_inicio, fecha_fin, pendiente, constante, coeficiente_correlacion, descripcion)
    pos.runQuery(query)
    print(query)