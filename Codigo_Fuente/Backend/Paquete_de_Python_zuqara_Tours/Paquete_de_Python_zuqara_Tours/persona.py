class persona:
    def __init__(self,nombre,correo):
        self.__nombre = None
        self.__correo = None
        self.set_nombre(nombre)
        self.set_correo(correo)

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        if nombre and len(nombre.strip())> 0:
            self.__nombre = nombre
        else:
            raise ValueError("El nombre no puede estar vacio")
        
    def get_correo(self):           
        return self.__correo
    
    def set_correo(self, correo):  
        if "@" in correo:
            self.__correo = correo
        else:
            raise ValueError("El correo debe contener @")



        