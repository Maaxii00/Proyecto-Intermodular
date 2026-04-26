import gymnasium as gym
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from agente import Agente
from memoria import Memoria

class Entrenador:
    def __init__(self, entorno_nombre="CartPole-v1", episodios=300, tamano_lote=64):
        self.env = gym.make(entorno_nombre)
        input_dim = self.env.observation_space.shape[0]
        n_actions = self.env.action_space.n
        self.episodios = episodios
        self.tamano_lote = tamano_lote
        self.agente = Agente(input_dim, n_actions)
        self.memoria = Memoria(capacidad_maxima=10000)
        self.optimizador = optim.Adam(self.agente.cerebro.parameters(), lr=0.001)
        self.funcion_perdida = nn.MSELoss()
        self.historial_puntos = []

    def entrenar(self):
        print("Iniciando el entrenamiento de la IA...")
        
        for episodio in range(self.episodios):
            estado, _ = self.env.reset()
            terminado = False
            puntos = 0
            
            while not terminado:
                estado_tensor = torch.FloatTensor(estado).unsqueeze(0)
                accion = self.agente.elegir_accion(estado_tensor)
                siguiente_estado, recompensa, terminated, truncated, _ = self.env.step(accion)
                terminado = terminated or truncated

                if terminado and puntos < 499:
                    recompensa = -10

                self.memoria.guardar_recuerdo(estado, accion, recompensa, siguiente_estado, terminado)

                self.aprender_de_memoria()
                
                estado = siguiente_estado
                puntos += 1

            self.agente.actualizar_probabilidad_aleatoria()
            self.historial_puntos.append(puntos)

            if (episodio + 1) % 10 == 0:
                print(f"Episodio {episodio + 1}/{self.episodios} | Puntos: {puntos} | Epsilon (Locura): {self.agente.probabilidad_aleatoria:.2f}")

        print("¡Entrenamiento finalizado!")
        self.agente.guardar_modelo("cerebro_cartpole.pth")
        self.dibujar_grafica()
        self.env.close()

    def aprender_de_memoria(self):
        if len(self.memoria) < self.tamano_lote:
            return 

        lote = self.memoria.sacar_recuerdos_aleatorios(self.tamano_lote)

        estados = torch.FloatTensor([experiencia[0] for experiencia in lote])
        acciones = torch.LongTensor([experiencia[1] for experiencia in lote]).unsqueeze(1)
        recompensas = torch.FloatTensor([experiencia[2] for experiencia in lote])
        siguientes_estados = torch.FloatTensor([experiencia[3] for experiencia in lote])
        terminados = torch.FloatTensor([experiencia[4] for experiencia in lote])

        q_valores_actuales = self.agente.cerebro(estados).gather(1, acciones).squeeze(1)
        q_valores_siguientes = self.agente.cerebro(siguientes_estados).max(1)[0]

        q_valores_objetivo = recompensas + (0.99 * q_valores_siguientes * (1 - terminados))

        error = self.funcion_perdida(q_valores_actuales, q_valores_objetivo.detach())
        
        self.optimizador.zero_grad()
        error.backward()
        self.optimizador.step()

    def dibujar_grafica(self):
        plt.plot(self.historial_puntos)
        plt.title('Curva de Aprendizaje de la IA')
        plt.xlabel('Episodios jugados')
        plt.ylabel('Puntos (Frames en pie)')
        plt.savefig('grafica_aprendizaje.png')
        print("Gráfica guardada como 'grafica_aprendizaje.png'")

if __name__ == "__main__":
    entrenador = Entrenador(episodios=100)
    entrenador.entrenar()