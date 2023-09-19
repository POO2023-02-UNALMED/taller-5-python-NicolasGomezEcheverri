from .animal import Animal

class Ave(Animal):

    _listado = []
    halcones = 0
    aguilas = 0
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, color):
        self._colorPlumas = color

    @classmethod
    def getListado(cls):
        return Ave._listado
    
    @classmethod
    def setListado(cls, listado):
        Ave._listado = listado

    @classmethod
    def getHalcones(cls):
        return Ave.halcones
    
    @classmethod
    def setHalcones(cls, listado):
        Ave.halcones = listado

    @classmethod
    def getAguilas(cls, listado):
        Ave.aguilas = listado

    @classmethod
    def setRanas(cls, listado):
        Ave.aguilas = listado

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        Halcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        Ave.halcones += 1
        return Halcon
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        Aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        Ave.aguilas += 1
        return Aguila