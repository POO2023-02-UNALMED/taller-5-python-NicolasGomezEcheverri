from .animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas=None, largoCola=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, largoCola):
        self._largoCola = largoCola
    
    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)
    
    def movimiento(self):
        return "reptar"
