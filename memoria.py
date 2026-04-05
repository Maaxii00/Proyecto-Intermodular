import random

class Memoria:
    def __init__(self, capacidad_maxima):

        #Inicializa la memoria con un tamaño máximo.
        #Si la memoria se llena, los recuerdos más antiguos se borrarán.
        self.capacidad_maxima = capacidad_maxima
        self.lista_recuerdos = []
        self.posicion = 0

    def guardar_recuerdo(self, estado, accion, recompensa, siguiente_estado, terminado):
        
        #Guarda lo que acaba de pasar en el juego en la memoria.
        
        if len(self.lista_recuerdos) < self.capacidad_maxima:
            self.lista_recuerdos.append(None)
            
        self.lista_recuerdos[self.posicion] = (estado, accion, recompensa, siguiente_estado, terminado)
        self.posicion = (self.posicion + 1) % self.capacidad_maxima

    def sacar_recuerdos_aleatorios(self, cantidad):

        #Saca un puñado de recuerdos al azar para que la red neuronal entrene con ellos.

        return random.sample(self.lista_recuerdos, cantidad)

    def __len__(self):
        #Devuelve cuántos recuerdos hay guardados actualmente.
        return len(self.lista_recuerdos)
