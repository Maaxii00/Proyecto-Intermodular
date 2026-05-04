import gymnasium as gym
import torch
import os
import time
from src.agente import Agente

def visualizar_agente():
    try:
        env = gym.make("CartPole-v1", render_mode="human")
    except Exception as e:
        print(f"Error al inicializar el entorno visual: {e}")
        return
    
    estados = env.observation_space.shape[0]
    acciones = env.action_space.n
    agente = Agente(estados, acciones)

    ruta_modelo = "models/cerebro_cartpole.pth"
    
    try:
        if os.path.exists(ruta_modelo):
            print(f"Modelo encontrado correctamente, cargandose desde: {ruta_modelo}")
            agente.cargar_modelo(ruta_modelo)
            agente.probabilidad_aleatoria = 0.0 
        else:
            print("No se encontró ningún modelo entrenado. El agente jugará de forma novata (De forma aleatoria).")
    except Exception as e:
         print(f"Error crítico al cargar los pesos del modelo: {e}")
         return

    try:
        estado, _ = env.reset()
        terminado = False
        truncado = False
        puntos = 0

        print("Iniciando simulación...")
        
        while not (terminado or truncado):
            estado_tensor = torch.FloatTensor(estado).unsqueeze(0)
            accion = agente.elegir_accion(estado_tensor)
            estado, recompensa, terminado, truncado, _ = env.step(accion)
            puntos += recompensa
            time.sleep(0.02) 

        print(f"Simulación terminada. Puntuación conseguida: {puntos}")
    except Exception as e:
        print(f"La simulación se interrumpió inesperadamente: {e}")
    finally:
        env.close()