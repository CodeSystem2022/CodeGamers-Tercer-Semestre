____________________________________________________________________________

# Leer_archivos.py

archivo = open('prueba.txt', 'r',
               encoding='utf8')
# print(archivo.read())
# w write = escribir
# r read = leer
# a append = anexar
# x crear = crear archivos
# print(archivo.read(16))
# print(archivo.read(10)) # Continuamos desde la lìnea anterior
# print(archivo.readline())
# print(archivo.readline())

# vamos a iterar el archivo, cada una de las lìneas
# for linea in archivo:
    # print(linea): iteramos todos los elementos del archivo
# print(archivo.readlines()[11]) #accedemos al archivo como si fuera una lista
# Anexamos informaciòn, copiamos a otro
archivo2 = open('copia.txt', 'w', encoding='utf8')
archivo2.write(archivo.read())
archivo.close() # cerramos el primer archivo
archivo2.close() # cerramos el segundo archivo

print('Se ha terminado el proceso de leer y copiar archivos')
