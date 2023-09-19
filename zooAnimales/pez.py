from .animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, color):
        self._cantidadAletas = color

    @classmethod
    def getListado(cls):
        return Pez._listado
    
    @classmethod
    def setListado(cls, listado):
        Pez._listado = listado

    @classmethod
    def getSalmones(cls):
        return Pez.salmones
    
    @classmethod
    def setSalmomnes(cls, listado):
        Pez.salmones = listado

    @classmethod
    def getBacalaos(cls, listado):
        Pez.bacalaos = listado

    @classmethod
    def setBacalaos(cls, listado):
        Pez.bacalaos = listado

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        Salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        Pez.salmones += 1
        return Salmon
    
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        Bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        Pez.bacalaos += 1
        return Bacalao