# COMO ACTUALIZAR VARIOS REGISTROSS

import psycopg2 # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(user='postgres', password='3875622315', host='127.0.0.1', port='5432', database='test bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s' #actualizar registros en una DB
            valores = (
                ('Juan Domingo', 'Farfan', 'fdomingo@mail.com', 4),
                ('Rocio', 'Aymar', 'ayro@mail.com', 5),
                ('Laura', 'Tolaba', 'lauto@mail.com', 6),
                ('Veronica', 'Quispe', 'qvero@mail.com', 7),
                ('Jorge', 'Garay', 'geray@mail.com', 8),
                ('Fabiola', 'Gimenez', 'gila@mail.com', 9),
                ('Viviana', 'Gerez', 'virez@mail.com', 10)
            ) # Es una tupla de tuplas
            cursor.executemany(sentencia, valores) # De esta manera ejecutamos la sentencia
            registros_actualizados = cursor.rowcount #ingresar valores a las columnas
            print(f'Los registros actualizados son: {registros_actualizados}')


except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
