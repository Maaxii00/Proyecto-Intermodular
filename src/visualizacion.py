import gymnasium as gym
import time
import torch
from src.agente import Agente

def mirar_agente_jugar():
    env = gym.make("CartPole-v1", render_mode="human")

    input_dim = env.observation_space.shape[0] 
    n_actions = env.action_space.n              
    
    jugador = Agente(input_dim, n_actions)
    
    # ¡AQUÍ ESTÁ LA CLAVE! 
    # Le inyectamos los conocimientos matemáticos que el entrenador guardó en el archivo .pth
    jugador.cerebro.load_state_dict(torch.load("cerebro_cartpole.pth", weights_only=True))
    
    # Le decimos al agente que NO explore haciendo cosas al azar, que use 100% lo que sabe
    jugador.probabilidad_aleatoria = 0.0 
    jugador.cerebro.eval() 

    episodios = 5  
    
    for episodio in range(episodios):
        state, info = env.reset()
        terminado = False
        puntos = 0
        
        print(f"Preparando episodio {episodio + 1}")
        time.sleep(2) 
        
        while not terminado:
            state_tensor = torch.FloatTensor(state).unsqueeze(0)
            action = jugador.elegir_accion(state_tensor)
            
            next_state, reward, terminated, truncated, info = env.step(action)
            state = next_state
            puntos += 1
            terminado = terminated or truncated

            time.sleep(0.05) # Un poquito más rápido para que veas cómo lo equilibra

        print(f"Episodio {episodio + 1}: El agente ha aguantado {puntos} pasos.")

    env.close() 

if __name__ == "__main__":
    mirar_agente_jugar()