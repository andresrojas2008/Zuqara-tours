from abc import ABC, abstractmethod
 
class entidadbase(ABC):
 
    @abstractmethod
    def validar(self):
        pass
 
    @abstractmethod
    def describir(self):
        pass