____________________________________________________________________________
# Archivos_con_whith.py

from ManejoArchivos import ManejoArchivos
# MANEJO DE CONTEXTO WITH: sintaxis simplificada, abre y cierra el archivo
# with open('prueba.txt', 'r', encoding='utf8') as archivo:
    # print(archivo.read())
# No hace falta ni el try, ni el finally
# en el contexto de with lo que se ejecuta de manera automática
# utiliza diferentes mètodos: __enter__ este es el que abre
# Ahora el siguiente mètodo es el que cierra: __exit__

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())
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

____________________________________________________________________________

# Manejo_de_archivos.py
# Declaramos una variable
try:
    archivo = open('prueba.txt', 'w', encoding='utf8') #La w es de write que significa escribir # crea archivos y abre archivos
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acciòn, ejecución y producción\n')
    archivo.write('las letras son:\nr read leer, \na append anexa, \nw write escribe, \nx crea un archivo')
    archivo.write('\nt especifica el archivo, texto, \nb binari binarios imagines, videos, pdf, etc. \nw+ para escribir y leer informaciòn, \nr+ son iguales\n')
    archivo.write('Saludos a todos los compañeros de la tecnicatura\n')
    archivo.write('Fin de las declaraciones con variables')
except Exception as e:
    print(e)
finally: # siempre se ejecuta
    archivo.close() # con esto se debe cerrar el archivo
# archivo.write('Todo quedó perfecto'): finally cerro el archivo, èste es un error, ya no podemos seguir trabajando con el archivo

____________________________________________________________________________

# ManejoArchivos.py

class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Obtenemos el recurso'.center(50, '-'))
        self.nombre = open(self.nombre, 'r', encoding='utf8') # Encapsulamos el còdigo del método
        return self.nombre

    def __exit__(self, tipo_exception, valor_exception, traza_error):
        print('cerramos el recurso'.center(50, '-'))
        if self.nombre:
            self.nombre.close() # cerramos el archivo

____________________________________________________________________________

prueba.txt

Programamos con diferentes tipos de archivos, ahora en txt.
Los acentos son importantes para las palabras
como por ejemplo: acciòn, ejecución y producción
las letras son:
r read leer, 
a append anexa, 
w write escribe, 
x crea un archivo
t especifica el archivo, texto, 
b binari binarios imagines, videos, pdf, etc. 
w+ para escribir y leer informaciòn, 
r+ son iguales
Saludos a todos los compañeros de la tecnicatura
Fin de las declaraciones con variables 

