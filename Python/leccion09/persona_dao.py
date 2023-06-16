
    DAO significa: Data Access object
    CRUD significa:
                    Create > Insertar
                    Read > Seleccionar
                    Update > Actualizar
                    Delete > Eliminar

    SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%S, %S, %S)'
    ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'


    #definimos los métodos de clase
    @classmethod
    def seleccionar(cls):
           # with Conexion.obtenerConexion():
                    with Conexion.obtenerCursor() as cursor:
                            cursor.execute(cls._SELECCIONAR)
                            registros = cursor.fetchall()
                            personas = [] #creamos una lista
                            for registro in registros:
                                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                                personas.append(persona)
                            return personas

    @classmethod
    def insert(cls, persona):
            with Conexion.obtenerConexion():  
                with Conexion.obtenerCursor() as cursor:
                    valores = (persona.nombre, persona.apellido, persona.email)
                    cursor.execute(cls._INSERTAR, valores)
                    log.debug(f'Persona Insertada: {persona}')
                    return cursor.rowcount                    

    @classmethod
    def actualizar(cls, persona):
            with Conexion.obtenerConexion():
                with Conexion.obtenerCursor() as cursor:
                    valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                    cursor.execute(cls._ACTUALIZAR, valores)
                    log.debug(f'Persona actualizada: {persona}')
                    return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
           with Conexion.obtenerConexion():
                  with Conexion.obtenerCursor() as cursor:
                         valores = (persona.id_persona, )
                         cursor.execute(cls._ELIMINAR, valores)
                         log.debug(f'Los objetos eliminados son: {persona}')
                         return cursor.rowcount
                               

if __name__ == '__main__':
        #eliminar un registro
        persona1 = Persona(id_persona=13)

        #actualizar un registro
        #persona1 = Persona(1, 'Juan Jose', 'Pena', 'jjpena@algo')
        #personas_actualizadas = PersonaDAO.actualizar(persona1)
        #log.debug(f'Personas actualizadas: {personas_actualizadas}')
        
        #insertar un registro
        #persona1 = Persona(nombre='Omero', apellido='Ramos', emial='sdfso@mail.com')
        #personas_insertadas = PersonaDAO.insertar(persona1)
        #log.debug(f'Personas Insertadas: {personas_insertadas}')

        #seleccionar objetos
        personas = PersonaDAO.seleccionar()
        for persona in personas:
                log.debug(persona)
