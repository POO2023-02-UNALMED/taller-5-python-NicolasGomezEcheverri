from zooAnimales.mamifero import cantidadMamiferos
from zooAnimales.ave import cantidadAves
from zooAnimales.reptil import cantidadReptiles 
from zooAnimales.pez import cantidadPeces
from zooAnimales.anfibio import cantidadAnfibios

class Animal:
    _totalAnimales = 0
    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, zona=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
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
        return "Mamiferos: " + str(cantidadMamiferos()) + "\n" + "Aves: " + str(cantidadAves()) + "\n" + "Reptiles: " + str(cantidadReptiles()) + "\n" + "Peces: " + str(cantidadPeces()) + "\n" + "Anfibios: " + str(cantidadAnfibios())

    def toString(self):
        if self._zona != None:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad + ", habito en " + self._habitat + " y mi genero es " + self._genero + ", la zona en la que me ubico es " + self._zona.getNombre() + ", en el " + self._zona.getZoo().getNombre()
        else:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad + ", habito en " + self._habitat + " y mi genero es " + self._genero
