import unittest
import torch
from src.memoria import Memoria
from src.agente import Agente
from src.red_neuronal import DQN

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

class TestAgente(unittest.TestCase):

    def test_inicializacion_cerebro(self):
        jugador = Agente(input_dim=4, n_actions=2)
        self.assertIsInstance(jugador.cerebro, DQN, "El agente no ha instanciado la red neuronal correctamente")

    def test_eleccion_accion_exploracion(self):

        jugador = Agente(input_dim=4, n_actions=2)
        jugador.probabilidad_aleatoria = 1.0 
        estado_falso = torch.randn(1, 4)
        accion = jugador.elegir_accion(estado_falso)
        self.assertIn(accion, [0, 1], "El agente ha elegido una acción fuera de rango")

    def test_eleccion_accion_explotacion(self):
        jugador = Agente(input_dim=4, n_actions=2)
        jugador.probabilidad_aleatoria = 0.0 
        estado_falso = torch.randn(1, 4)
        accion = jugador.elegir_accion(estado_falso)
        self.assertIn(accion, [0, 1], "La red neuronal ha fallado al predecir la acción")

if __name__ == '__main__':
    unittest.main()