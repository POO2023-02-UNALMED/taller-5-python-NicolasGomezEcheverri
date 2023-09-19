from .animal import Animal

class Ave(Animal):
    _listado = []
    aguilas = 0
    halcones = 0

    def __init__(self, nombre=None, edad=None, genero=None, habitat=None, colorPlumas=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
    
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        halcones += 1
        return Ave(nombre, edad, genero, "montanas", "cafe glorioso")
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        aguilas += 1
        return Ave(nombre, edad, genero, "montanas", "blanco y amarillo")
    
    def movimiento(self):
        return "volar"
