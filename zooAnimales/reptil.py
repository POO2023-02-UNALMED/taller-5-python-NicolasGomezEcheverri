from .animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, color):
        self._largoCola = color

    @classmethod
    def getListado(cls):
        return Reptil._listado
    
    @classmethod
    def setListado(cls, listado):
        Reptil._listado = listado

    @classmethod
    def getIguanas(cls):
        return Reptil.iguanas
    
    @classmethod
    def setIguanas(cls, listado):
        Reptil.iguanas = listado

    @classmethod
    def getSerpientes(cls, listado):
        Reptil.serpientes = listado

    @classmethod
    def setSerpientes(cls, listado):
        Reptil.serpientes = listado

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        Iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        Reptil.iguanas += 1
        return Iguana
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        Serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        Reptil.serpientes += 1
        return Serpiente
