# COMO ACTUALIZAR UN SOLO REGISTRO

import psycopg2 # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(user='postgres', password='3875622315', host='127.0.0.1', port='5432', database='test bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s' #actualizar registros en una DB
            valores = ('Juan Carlos', 'Roldan', 'rcarlos@mail.com', 1) # Es una tupla
            cursor.execute(sentencia, valores) # De esta manera ejecutamos la sentencia
            registros_actualizados = cursor.rowcount #ingresar valores a las columnas
            print(f'Los registros actualizados son: {registros_actualizados}')


except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
