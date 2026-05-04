# Agente Inteligente CartPole (DQN) - Proyecto Intermodular

Este proyecto es el módulo de Inteligencia Artificial (IA) del Proyecto Intermodular. Consiste en el desarrollo de un agente basado en Aprendizaje por Refuerzo (Reinforcement Learning) utilizando una arquitectura Deep Q-Network (DQN). El sistema permite al agente aprender de forma autónoma a balancear un péndulo invertido sobre un carro móvil dentro del entorno de simulación CartPole (Gymnasium).

## Tecnologías utilizadas
* **Lenguaje:** Python 3.12.x
* **Framework IA:** PyTorch 2.2+
* **Simulación de Entorno:** Gymnasium (Farama Foundation) 0.29.1
* **Motor Gráfico:** pygame-ce
* **Análisis y Métricas:** Matplotlib 3.8+
* **Interacción manual:** `keyboard`
* **Testing:** `unittest` (Librería nativa de Python)

## Requisitos previos
Para ejecutar este proyecto en local, necesitas:
* Python 3.12 o inferior instalado en el sistema.
* Gestor de paquetes `pip` actualizado.
* (Opcional) Entorno virtual activo (`venv` o `conda`).
* Interfaz gráfica disponible (monitor o servidor X11) para el renderizado del juego.

## Instrucciones de instalación
Abre tu terminal y ejecuta los siguientes comandos paso a paso:

1. Clona el repositorio:
> `git clone https://github.com/Maaxii00/Proyecto-Intermodular.git`

2. Accede a la carpeta del proyecto:
> `cd Proyecto-Intermodular`

3. Instala todas las dependencias necesarias:
> `pip install torch gymnasium[classic_control] pygame-ce matplotlib keyboard`

## Instrucciones de ejecución
El proyecto se ha unificado bajo un único punto de entrada interactivo. Asegúrate de ejecutarlo desde el directorio raíz del proyecto.

**A) Iniciar la Aplicación Principal:**
> `python main.py`

Al ejecutar este comando, se desplegará un menú en consola con las siguientes opciones:
1. **Entrenar IA desde cero:** Inicia un nuevo bucle de aprendizaje.
2. **Entrenamiento Continuo (Fine-Tuning):** Carga un modelo guardado previamente (`.pth`) para perfeccionar su técnica sin perder la memoria.
3. **Visualizar Agente:** Abre el entorno gráfico de Pygame para ver a la IA jugar a velocidad normal usando el modelo entrenado.
4. **Jugar Manualmente:** Habilita el control humano mediante las flechas del teclado para comparar la dificultad del nivel frente a la IA.

**B) Ejecutar las Pruebas Unitarias:**
Ejecuta la batería completa de tests para comprobar la integridad de las clases del sistema.
> `python -m unittest discover tests -v`

## Funcionalidades implementadas (100% Operativo)
* ✅ **Arquitectura DQN:** Red neuronal multicapa (MLP) programada con PyTorch.
* ✅ **Sistema de Menú Interactivo:** CLI completa para gestionar los diferentes modos de ejecución sin tocar el código.
* ✅ **Carga y Guardado Dinámico:** El modelo se guarda automáticamente en disco (`models/cerebro_cartpole.pth`) al superar el nivel o terminar los episodios, y puede cargarse posteriormente.
* ✅ **Gestión de Memoria (Replay Buffer):** Almacenamiento circular de experiencias pasadas para entrenar en lotes aleatorios, evitando el olvido catastrófico.
* ✅ **Métricas y Análisis:** Generación automática de gráficas de la curva de aprendizaje (Puntos vs Episodios).
* ✅ **Testing y Modularidad:** Código 100% orientado a objetos y testeado mediante pruebas unitarias modulares.
* ✅ **Prevención de Sobreajuste (Early Stopping):** El entrenamiento se detiene automáticamente si la IA logra 10 partidas perfectas consecutivas.

## Problemas conocidos y Soluciones
* 🐛 **Error Headless (WSL/Servidores):** En entornos WSL (Windows Subsystem for Linux) o servidores sin interfaz gráfica, `pygame-ce` puede lanzar un error al no poder abrir la ventana de visualización. **Solución:** Ejecutar el código desde CMD/PowerShell en Windows nativo.
* 🐛 **El teclado no responde en Modo Manual:** La librería `keyboard` lee pulsaciones a nivel de sistema, lo que a veces requiere privilegios elevados. **Solución:** Ejecutar la terminal de VS Code (o PowerShell) como Administrador.

## Capturas de pantalla

* **Ejecución del Entrenamiento:** <img width="1290" height="263" alt="Captura de pantalla 2026-04-26 174701" src="https://github.com/user-attachments/assets/65258eae-4a2f-41e5-9213-5052c26ea33f" />
* **Entorno Gráfico CartPole:** <img width="620" height="437" alt="Captura de pantalla 2026-04-26 174731" src="https://github.com/user-attachments/assets/446cfd5d-db04-40dc-a483-87ebebed75c0" />
* **Gráfica de Aprendizaje:** <img width="637" height="480" alt="Captura de pantalla 2026-04-26 174757" src="https://github.com/user-attachments/assets/9449a967-493b-4cc5-9135-dde16f33d831" />
* **Pruebas Unitarias:** <img width="569" height="145" alt="Captura de pantalla 2026-04-26 174858" src="https://github.com/user-attachments/assets/23dd026d-a27a-4dc9-935e-913148862e75" />
* **Estructura del Proyecto:** <img width="257" height="472" alt="Captura de pantalla 2026-04-26 175628" src="https://github.com/user-attachments/assets/7eb976c4-6f88-45fc-9048-f937e75e8ec9" />

## Autor y Contacto
* **Desarrollador:** Maximiliano González Segura - 2º DAM
* **GitHub:** [Maaxii00](https://github.com/Maaxii00)