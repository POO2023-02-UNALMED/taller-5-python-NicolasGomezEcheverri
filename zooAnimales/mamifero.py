from .animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    def isPelaje(self):
        return self._pelaje
    
    def setPelaje(self, color):
        self._pelaje = color

    def getPatas(self):
        return self._patas
    
    def setPatas(self, color):
        self._patas = color

    @classmethod
    def getListado(cls):
        return Mamifero._listado
    
    @classmethod
    def setListado(cls, listado):
        Mamifero._listado = listado

    @classmethod
    def getCaballos(cls):
        return Mamifero.caballos
    
    @classmethod
    def setCaballos(cls, listado):
        Mamifero.caballos = listado

    @classmethod
    def getLeones(cls, listado):
        Mamifero.leones = listado

    @classmethod
    def setLeones(cls, listado):
        Mamifero.leones = listado
    
    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        Mamifero.caballos += 1
        return caballo
    
    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        Leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        Mamifero.leones += 1
        return Leon