class Animal:
    _totalAnimales = 0
    def __init__(self, nombre=None, edad=None, habitat=None, genero=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = []
        Animal._totalAnimales += 1

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona

    def movimiento(self):
        return "desplazarse"

    @classmethod
    def totalPorTipo(cls):
        from .anfibio import Anfibio
        from .ave import Ave
        from .mamifero import Mamifero
        from .pez import Pez
        from .reptil import Reptil

        return "Mamiferos: " + str(Mamifero.cantidadMamiferos()) + "\n" + "Aves: " + str(Ave.cantidadAves()) + "\n" + "Reptiles: " + str(Reptil.cantidadReptiles()) + "\n" + "Peces: " + str(Pez.cantidadPeces()) + "\n" + "Anfibios: " + str(Anfibio.cantidadAnfibios())

    def toString(self):
        from gestion.zoologico import Zoologico
        from gestion.zona import Zona
        
        if len(self._zona) != 0:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad + ", habito en " + self._habitat + " y mi genero es " + self._genero + ", la zona en la que me ubico es " + self._zona.getNombre() + ", en el " + self._zona.getZoo().getNombre()
        else:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad + ", habito en " + self._habitat + " y mi genero es " + self._genero
