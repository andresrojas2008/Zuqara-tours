from entidad_bas_val import entidadbase 
from persona import persona

class usuario(entidadbase, persona):
    def __init__(self,nombre, correo, fecha_registro):
        super().__init__(nombre, correo)
        self.__fecha_registro= fecha_registro
        self.__itinerarios= []

    def validar(self):
        return True
    
    def describir(self):
        return f"usuarios: {self.get_nombre()} | {self.get_correo()}"
    
    def agregar_itinerario(self, itinerario):
        self.__itinerarios.append(itinerario)

    def get_itinerario(self):
        return self.__itinerarios