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
  result = cur.fetchone()
  cur.close()
  return result