import random

class Memoria:
    def __init__(self, capacidad_maxima):
        self.capacidad_maxima = capacidad_maxima
        self.lista_recuerdos = []
        self.posicion = 0

    def guardar_recuerdo(self, estado, accion, recompensa, siguiente_estado, terminado):
        if len(self.lista_recuerdos) < self.capacidad_maxima:
            self.lista_recuerdos.append(None)
        self.lista_recuerdos[self.posicion] = (estado, accion, recompensa, siguiente_estado, terminado)
        self.posicion = (self.posicion + 1) % self.capacidad_maxima

    def sacar_recuerdos_aleatorios(self, cantidad):
        return random.sample(self.lista_recuerdos, cantidad)

    def __len__(self):
        return len(self.lista_recuerdos)
