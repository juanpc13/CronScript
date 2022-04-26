# load configuracions in VAR
from configparser import ConfigParser
configs = {}
def iniConfigs(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            configs[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

# Postgres
import psycopg2
conn = None

def getConnection():
  global conn, configs
  if conn == None:
    conn = psycopg2.connect(**configs)
    conn.autocommit = True
  return conn

def getCursor():
  try:
    cur = getConnection().cursor()
    return cur
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
    return None

def test():
  # Prueba de conexion
  cur = getCursor()
  cur.execute('SELECT version()')
  db_version = cur.fetchone()
  print(db_version)
  cur.close()

def runQuery(query):
  # Prueba de conexion
  cur = getCursor()
  cur.execute(query)
  cur.close()

def runQueryResult(query):
  # Prueba de conexion
  cur = getCursor()
  cur.execute(query)
  result = cur.fetchone()
  cur.close()
  return result

def queryFetchAll(query):
  # Prueba de conexion
  cur = getCursor()
  cur.execute(query)
  result = cur.fetchall()
  cur.close()
  return result

# Queue multiData
curQueue = None
def startQueue():
  # iniciar un cursor
  global curQueue
  curQueue = getCursor()
def addQueue(query):
  # Agregar a la cola
  global curQueue
  curQueue.execute(query)
def endQueue():
  # Enviar todo y cerrar cursor
  global curQueue
  conn.commit()
  curQueue.close()
  curQueue = None

###########
def getQueryRutinas():
  return "SELECT id_rutina, id_investigacion, id_dispositivo, nombre, index_x, index_y, multiplicador_x, multiplicador_y FROM rutina WHERE activa = TRUE;"

def getQueryMainData(idInvestigacion, idDispositivo, fechaInicio, fechaFin):
  columnas = f"fecha_registrada, humedad AS h2o, dioxido_carbono AS co2, hidrogeno AS h2, acido_sulfhidrico AS h2s, dioxido_azufre AS so2"
  where = f"id_investigacion = {idInvestigacion} AND id_dispositivo = {idDispositivo} AND fecha_registrada >= '{fechaInicio}' AND fecha_registrada < '{fechaFin}'"
  query = f"SELECT {columnas} FROM maindata WHERE {where} ORDER BY fecha_registrada ASC"
  return query

def getQueryHistorico(id_rutina, nombre, fecha_inicio, fecha_fin, pendiente, constante, coeficiente_correlacion, descripcion):
  query = "INSERT INTO historico(id_rutina, nombre, fecha_inicio, fecha_fin, pendiente, constante, coeficiente_correlacion, descripcion) "
  query += "VALUES ({}, '{}', '{}', '{}', {}, {}, {}, '{}')".format(
    id_rutina,
    nombre,
    fecha_inicio,
    fecha_fin,
    pendiente,
    constante,#LO MISMO QUE CONSTANTE o intercepto
    coeficiente_correlacion,
    descripcion
  )
  return query


import pandas as pd
def getDataFrameQuery(query):
  return pd.read_sql_query(query,con=getConnection())
