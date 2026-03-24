import gymnasium as gym
import torch
import time
from red_neuronal import DQN

def mirar_agente_jugar():
    # Importante: el render_mode="human" es para que abra la ventanita con los gráficos
    env = gym.make("CartPole-v1", render_mode="human")

    # Saco los tamaños de las entradas y salidas dinámicamente
    input_dim = env.observation_space.shape[0] 
    n_actions = env.action_space.n              
    
    # Cargo la red neuronal vacía
    model = DQN(input_dim, n_actions)
    
    # Pongo la red en modo evaluación 
    model.eval()

    episodios = 5  # Vueltas que quiero ver
    
    for episodio in range(episodios):
        state, info = env.reset() # Reseteo el entorno para empezar limpio
        terminado = False
        puntos = 0
        
        print(f"Preparando episodio {episodio + 1}")
        time.sleep(2) # Pausa de 2 segundos al inicio de la partida con la pantalla congelada
        
        while not terminado:
            # Convierto el array de numpy que me da el juego a un Tensor
            state_tensor = torch.FloatTensor(state).unsqueeze(0)
            
            with torch.no_grad(): 
                q_values = model(state_tensor)
            
            # Cojo la acción que la red cree que es mejor
            action = torch.argmax(q_values).item()
            
            # Le paso la acción al juego
            next_state, reward, terminated, truncated, info = env.step(action)
            
            # Actualizo variables
            state = next_state
            puntos += 1
            terminado = terminated or truncated

            # Le metemos 0.1 o 0.2 segundos de delay para que los movimientos se aprecien
            time.sleep(0.1)

        print(f"Episodio {episodio + 1}: El agente ha aguantado {puntos} pasos.")

    env.close() 

if __name__ == "__main__":
    mirar_agente_jugar()