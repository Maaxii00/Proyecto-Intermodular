import gymnasium as gym
import time
from agente import Agente

def mirar_agente_jugar():
    # Iniciamos el entorno gráfico
    env = gym.make("CartPole-v1", render_mode="human")

    # Sacamos las dimensiones dinámicamente
    input_dim = env.observation_space.shape[0] 
    n_actions = env.action_space.n              
    
    # Creamos a nuestro jugador (Agente). Él ya se encarga de crear su propio cerebro (DQN) por dentro.
    jugador = Agente(input_dim, n_actions)
    
    # Para la visualización, no queremos que explore haciendo locuras, 
    # queremos que use lo que sabe (aunque ahora mismo sepa poco).
    jugador.probabilidad_aleatoria = 0.0 
    jugador.cerebro.eval() # Modo evaluación

    episodios = 5  
    
    for episodio in range(episodios):
        state, info = env.reset()
        terminado = False
        puntos = 0
        
        print(f"Preparando episodio {episodio + 1}")
        time.sleep(2) 
        
        while not terminado:
            # Ahora es el Agente quien elige la acción, el código queda mucho más limpio
            import torch
            state_tensor = torch.FloatTensor(state).unsqueeze(0)
            
            # Le pedimos al agente que decida
            action = jugador.elegir_accion(state_tensor)
            
            # El entorno reacciona a la acción del agente
            next_state, reward, terminated, truncated, info = env.step(action)
            
            state = next_state
            puntos += 1
            terminado = terminated or truncated

            time.sleep(0.1)

        print(f"Episodio {episodio + 1}: El agente ha aguantado {puntos} pasos.")

    env.close() 

if __name__ == "__main__":
    mirar_agente_jugar()
