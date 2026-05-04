from src.agente import Agente
from src.red_neuronal import DQN
import unittest
import torch

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