import psycopg2 #esto es para poder conectarnos a postgre

conexion = psycopg2.connect(
user = 'postgres',
password = 'mara',
host = '127.0.0.1',
port = '5432',
database='test_bd',
)

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia) #de esta manera ejecutamos la sentencia
registros = cursor.fetchall() #recuperamos todos los registros que serán una lista
print (registros)

cursor.close()
conexion.close()
