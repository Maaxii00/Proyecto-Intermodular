import unittest
from src.memoria import Memoria

class TestMemoria(unittest.TestCase):

    def test_limite_capacidad(self):
        memoria_prueba = Memoria(capacidad_maxima=3)
        for i in range(5):
            memoria_prueba.guardar_recuerdo(f"estado_{i}", 1, 10, f"estado_{i+1}", False)
        self.assertEqual(len(memoria_prueba), 3, "La memoria ha superado su capacidad máxima")

    def test_extraccion_aleatoria(self):
        memoria_prueba = Memoria(capacidad_maxima=10)
        for i in range(10):
            memoria_prueba.guardar_recuerdo(i, 0, 1, i+1, False)

        lote = memoria_prueba.sacar_recuerdos_aleatorios(4)
        self.assertEqual(len(lote), 4, "No ha devuelto la cantidad correcta de recuerdos")
