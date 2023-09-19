class Zona:
    def __init__(self, nombre=None, zoo=None, animales=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = animales

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getZoo(self):
        return self._zoo

    def setZoo(self, zoo):
        self._zoo = zoo

    def getAnimales(self):
        return self._animales

    def setAnimales(self, animales):
        self._animales = animales

    def agregarAnimales(self, animal):
        if self._animales == None:
            self._animales = []
        self._animales.append(animal)

    def cantidadAnimales(self):
        if self._animales == None:
            return 0
        return len(self._animales)
