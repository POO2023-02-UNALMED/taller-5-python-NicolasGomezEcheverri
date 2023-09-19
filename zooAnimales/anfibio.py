from .animal import Animal

class Anfibio(Animal):
    _listado = []
    salamandras = 0
    ranas = 0
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self, color):
        self._colorPiel = color

    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, valor):
        self._venenoso = valor

    @classmethod
    def getListado(cls):
        return Anfibio._listado
    
    @classmethod
    def setListado(cls, listado):
        Anfibio._listado = listado

    @classmethod
    def getSalamandras(cls):
        return Anfibio.salamandras
    
    @classmethod
    def setSalamandras(cls, listado):
        Anfibio.salamandras = listado

    @classmethod
    def getRanas(cls, listado):
        Anfibio.ranas = listado

    @classmethod
    def setRanas(cls, listado):
        Anfibio.ranas = listado

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        Salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        Anfibio.salamandras += 1
        return Salamandra
    
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        Rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        Anfibio.ranas += 1
        return Rana