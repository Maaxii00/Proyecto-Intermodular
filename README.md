# Título del proyecto
Aprendizaje por Refuerzo aplicado a la Automatización de Pruebas en Videojuegos (Prototipo DQN)

# Descripción breve
Este proyecto es un prototipo funcional de un Agente de Inteligencia Artificial basado en Aprendizaje por Refuerzo (Deep Q-Network). El sistema inicializa un entorno de simulación (CartPole) y conecta una red neuronal para la toma de decisiones visuales en tiempo real.

# Tecnologías utilizadas
* **Lenguaje:** Python 3.x
* **Framework de IA:** PyTorch
* **Entorno de Simulación:** Gymnasium (Farama Foundation)

# Requisitos previos
Para ejecutar este proyecto necesitas tener instalado en tu sistema:
* Python 3.12 o inferior (recomendado para compatibilidad de librerías).
* Gestor de paquetes `pip`.

# Instrucciones de instalación
Abre tu terminal y ejecuta los siguientes comandos para instalar las dependencias necesarias:

```bash
pip install torch
pip install gymnasium[classic_control]
pip install pygame-ce
```

# Instrucciones de ejecución
El prototipo consta de dos scripts principales operativos:

Para probar la arquitectura de la red neuronal por consola:

Bash
python prueba.py
Para visualizar al agente interactuando gráficamente con el entorno:

Bash
python visualizacion.py

# Funcionalidades implementadas
✅ Creación de la arquitectura de la Red Neuronal (DQN) con capas lineales.

✅ Inicialización del entorno gráfico CartPole-v1 mediante Gymnasium.

✅ Captura del estado del entorno y conversión a tensores de PyTorch.

✅ Bucle de juego funcional donde el agente toma decisiones (pesos aleatorios).

✅ Documentación técnica en el código fuente.

# Funcionalidades pendientes

⏳ Implementar el algoritmo de entrenamiento (cálculo de recompensas, función de pérdida y optimizador).

⏳ Crear el "Replay Buffer" para almacenar el aprendizaje.

⏳ Guardar y cargar modelos entrenados (.pth).

⏳ Realizar pruebas unitarias.

# Autor
Maximiliano González Segura - 2º DAM
