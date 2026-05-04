import sys
import gymnasium as gym
import keyboard
import time
from src.entrenador import Entrenador
from src.visualizacion import visualizar_agente

def jugar_manualmente():
    print("Haz clic en la consola para asegurar que detecta las teclas.")
    print("Usa las flechas IZQUIERDA y DERECHA para mover el carro.")
    print("Mantén pulsada la tecla 'Q' para salir a mitad de partida.")
    
    try:
        env = gym.make("CartPole-v1", render_mode="human")
        env.reset()
        terminado = truncado = False
        puntos = 0
        
        time.sleep(1)
        accion = 0 
        while not (terminado or truncado):
            
            if keyboard.is_pressed('right'):
                accion = 1
            elif keyboard.is_pressed('left'):
                accion = 0
            
            if keyboard.is_pressed('q'):
                print("Partida abortada por el usuario.")
                break

            _, recompensa, terminado, truncado, _ = env.step(accion)
            puntos += recompensa
            time.sleep(0.05)
            
        print(f"Partida terminada. Tu puntuación ha sido: {puntos} puntos.")
    except Exception as e:
        print(f"Error al cargar el entorno manual: {e}")
    finally:
        env.close()

def mostrar_menu():
    print("CARTPOLE")
    print("1. Entrenar al Agente")
    print("2. Visualizar al Agente")
    print("3. Jugar Manualmente")
    print("4. Salir")
    print("="*40)

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            try:
                print("Iniciando módulo de entrenamiento...")
                entrenador = Entrenador()
                entrenador.entrenar()
            except Exception as e:
                print(f"Error crítico durante el entrenamiento: {e}")
                
        elif opcion == '2':
            try:
                print("Iniciando módulo de visualización")
                visualizar_agente()
            except Exception as e:
                print(f"Error al cargar la visualización: {e}")
                
        elif opcion == '3':
            jugar_manualmente()
                
        elif opcion == '4':
            print("¡Saliendo del programa! Hasta pronto.")
            sys.exit(0)
            
        else:
            print("Opción no válida. Por favor, elige 1, 2, 3 o 4.")

if __name__ == "__main__":
    main()