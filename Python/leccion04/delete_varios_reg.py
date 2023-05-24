# COMO ELIMINAR VARIOS REGISTROS DE UNA SOLA VEZ

import psycopg2 # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(user='postgres', password='3875622315', host='127.0.0.1', port='5432', database='test bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Digite el número de registro a eliminar: ')
            valores = (tuple(entrada.split(',')),) # tuplas de tuplas
            cursor.execute(sentencia, valores) # De esta manera ejecutamos la sentencia
            registros_eliminados = cursor.rowcount #ingresar valores a las columnas
            print(f'Los registros eliminados son: {registros_eliminados}')


except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
