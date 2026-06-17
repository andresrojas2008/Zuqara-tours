from entidad_bas_val import entidadbase
from persona import persona

class operadorturistico(persona, entidadbase):

    def __init__(self, nombre, correo, empresa):
        super().__init__(nombre, correo)
        self.__empresa = None
        self.set_empresa(empresa)

    def get_empresa(self):
        return self.__empresa

    def set_empresa(self, empresa):
        if empresa and len(empresa.strip()) > 0:
            self.__empresa = empresa
        else:
            raise ValueError("La empresa no puede estar vacia")

    def validar(self):
        if not self.__empresa or len(self.__empresa.strip()) == 0:
            raise ValueError("los datos del operador no son validos")
        return True


    def describir(self):
        return f"Operador: {self.__empresa} | Contacto: {self.get_correo()}"