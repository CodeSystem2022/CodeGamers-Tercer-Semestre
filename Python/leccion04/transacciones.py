# EJECUCION DE QUERYS EXITOSA

import psycopg2 as bd # Esto es para poder conectarnos a Postgre

conexion = bd.connect(user='postgres', password='3875622315', host='127.0.0.1', port='5432', database='test bd')
try:
    #conexion.autocommit = False (no usar estos comandos) # Usar True no es una buena práctica de un buen programador
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email)VALUES(%s, %s, %s)'
    valores = ('Maria', 'Esparza', 'mesparza@email.com')
    cursor.execute(sentencia, valores)
    conexion.commit()  #Hacemos el commit manual
    print('Termina la transacción')

except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo un rollback: {e}')
finally:
    conexion.close()
