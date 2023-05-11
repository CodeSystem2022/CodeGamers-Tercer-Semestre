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
