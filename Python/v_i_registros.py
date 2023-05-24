#INSERTAR VARIOS REGISTROS

import psycopg2 # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(user='postgres', password='3875622315', host='127.0.0.1', port='5432', database='test bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido, email)VALUES (%s, %s, %s)' #creando parámetros
            valores = (
                ('Carlos', 'Lara', 'clara@mail.com'),
                ('Marcos', 'Canto', 'mcanto@mail.com'),
                ('Marcelo', 'Cuenca', 'cuencam@mail.com')
            ) # Es una tupla de tuplas
            cursor.executemany(sentencia, valores) # De esta manera ejecutamos la sentencia
            # conexion.commit() esto se utiliza para guardar los cambios en la base de datos
            registros_insertados = cursor.rowcount #ingresar valores a las columnas
            print(f'Los registros insertados son: {registros_insertados}')


except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
