from logger_base import log


class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
           self._id_persona = id_persona
           self._nombre = nombre 
           self._apellido = apellido
           self._email = email
    
    def __str__(self):
           return f'''
                Id Persona: {self._id_persona},
                Nombre: {self._nombre},
                Apellido: {self._apellido},
                Email: {self._email}
                '''
    
    #Metodos getter and setters
    @property
    def id_persona(self):
           return self._id_persona