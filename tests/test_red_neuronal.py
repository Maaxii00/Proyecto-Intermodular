import unittest
import torch
from src.red_neuronal import DQN


class TestDQN(unittest.TestCase):

    def test_dimensiones_salida(self):
        red = DQN(input_shape=4, n_actions=2)
        estado_falso = torch.randn(1, 4)
        salida = red.forward(estado_falso)
        self.assertEqual(salida.shape, torch.Size([1, 2]), "La red neuronal no devuelve las dimensiones esperadas")