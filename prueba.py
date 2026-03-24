import torch
import gymnasium as gym
from red_neuronal import DQN 

# Monto la configuración básica sacando los datos del propio juego
env = gym.make("CartPole-v1")
input_dim = env.observation_space.shape[0] # Pilla las 4 entradas
n_actions = env.action_space.n             # Pilla las 2 acciones posibles

# Instancio mi red neuronal con esos datos
mi_cerebro = DQN(input_dim, n_actions)

print("--- Estructura de mi Red Neuronal ---")
print(mi_cerebro)

# Meto datos random para probar si la red no peta antes de conectarla al juego real.
# torch.randn me genera un tensor con 4 valores aleatorios imitando lo que me daría el entorno.
estado_falso = torch.randn(1, input_dim) 

# Le paso el estado falso a la red a ver qué escupe
output = mi_cerebro(estado_falso)

print("Resultado de la predicción (sin entrenar)")
print(f"Estado de entrada: {estado_falso}")
print(f"Valores de salida: {output}")

# Saco el número más alto de la salida para saber qué acción elegiría
accion = torch.argmax(output).item()
accion_texto = "Izquierda" if accion == 0 else "Derecha"
print(f"Como la red no está entrenada todavía, elige hacer un movimiento aleatorio hacia la: {accion_texto}")