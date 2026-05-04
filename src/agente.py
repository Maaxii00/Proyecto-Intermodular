import torch
import random
from src.red_neuronal import DQN

class Agente:
    def __init__(self, input_dim, n_actions):
        self.n_actions = n_actions
        self.cerebro = DQN(input_dim, n_actions)
        self.probabilidad_aleatoria = 1.0  
        self.probabilidad_minima = 0.01    
        self.tasa_decaimiento = 0.985      

    def elegir_accion(self, estado_tensor):
        dado = random.random()
        if dado < self.probabilidad_aleatoria:
            return random.randrange(self.n_actions)
        else:
            with torch.no_grad():
                valores_q = self.cerebro(estado_tensor)
                return torch.argmax(valores_q).item()

    def actualizar_probabilidad_aleatoria(self):
        if self.probabilidad_aleatoria > self.probabilidad_minima:
            self.probabilidad_aleatoria *= self.tasa_decaimiento
            
    def guardar_modelo(self, ruta="modelo_entrenado.pth"):
        torch.save(self.cerebro.state_dict(), ruta)

    def cargar_modelo(self, ruta):
        self.cerebro.load_state_dict(torch.load(ruta))
        self.cerebro.eval()