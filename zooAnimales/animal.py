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
        from .mamifero import Mamifero
        from .ave import Ave
        from .pez import Pez
        from .reptil import Reptil
        from .anfibio import Anfibio
        
        totalmamiferos = len(Mamifero.getListado())
        totalaves = len(Ave.getListado())
        totalreptiles = len(Reptil.getListado())
        totalpeces = len(Pez.getListado())
        totalanfibios = len(Anfibio.getListado())

        return (f"Mamiferos : {totalmamiferos}\nAves : {totalaves}\nReptiles : {totalreptiles}\nPeces : {totalpeces}\nAnfibios : {totalanfibios}")
    
    @classmethod
    def toString(self):
        from gestion.zona import Zona
        from gestion.zoologico import Zoologico
    
        if self._zona != None:
            return (f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero} la zona en la que me ubico es {self._zona[0]}, en el {self._zona[0].getZoo().getNombre()}")

        else:
            return (f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}")