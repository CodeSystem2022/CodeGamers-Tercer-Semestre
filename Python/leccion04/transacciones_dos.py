# insertar un registro nuevo

import psycopg2 as bd # Esto es para poder conectarnos a Postgre

conexion = bd.connect(user='postgres', password='3875622315', host='127.0.0.1', port='5432', database='test bd')
try:
    conexion.autocommit = False # esto directamente no debería estar, inicia la transacción
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email)VALUES(%s, %s, %s)'
    valores = ('Jorge', 'Portal', 'jportal@email.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Juan Carlos', 'Perez', 'jcperez@email', 1)
    cursor.execute(sentencia, valores)

    conexion.commit()  #Hacemos el commit manual, se cierra la transacción
    print('Termina la transacción')

except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo un rollback: {e}')
finally:
    conexion.close()
