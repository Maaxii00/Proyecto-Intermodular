import torch
import random
from src.red_neuronal import DQN

class Agente:
    def __init__(self, input_dim, n_actions):
        self.n_actions = n_actions
        # Instanciamos la red neuronal que creamos en el hito anterior
        self.cerebro = DQN(input_dim, n_actions)
        
        # Parámetros para tomar decisiones (Exploración vs Explotación)
        self.probabilidad_aleatoria = 1.0  
        self.probabilidad_minima = 0.01    
        self.tasa_decaimiento = 0.995      

    def elegir_accion(self, estado_tensor):

        # Tiramos un dado imaginario del 0 al 1
        dado = random.random()
        
        if dado < self.probabilidad_aleatoria:
            # Elige un movimiento totalmente al azar
            return random.randrange(self.n_actions)
        else:
            # Usa la red neuronal para elegir el mejor movimiento
            # No calculamos gradientes porque aquí solo estamos jugando, no entrenando
            with torch.no_grad():
                valores_q = self.cerebro(estado_tensor)
                return torch.argmax(valores_q).item()

    def actualizar_probabilidad_aleatoria(self):

        if self.probabilidad_aleatoria > self.probabilidad_minima:
            self.probabilidad_aleatoria *= self.tasa_decaimiento
            
    def guardar_modelo(self, ruta="modelo_entrenado.pth"):
        torch.save(self.cerebro.state_dict(), ruta)