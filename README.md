# Agente Inteligente CartPole (DQN) - Proyecto Intermodular

Este proyecto es el módulo de Inteligencia Artificial (IA) del Proyecto Intermodular. Consiste en el desarrollo de un agente basado en Aprendizaje por Refuerzo (Reinforcement Learning) utilizando una arquitectura Deep Q-Network (DQN). El sistema permite al agente aprender de forma autónoma a balancear un péndulo invertido sobre un carro móvil dentro del entorno de simulación CartPole (Gymnasium).

## Tecnologías utilizadas
* **Lenguaje:** Python 3.12.x
* **Framework IA:** PyTorch 2.2+
* **Simulación de Entorno:** Gymnasium (Farama Foundation) 0.29.1
* **Motor Gráfico:** pygame-ce
* **Análisis y Métricas:** Matplotlib 3.8+
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

3. Instala las dependencias necesarias:
> `pip install torch gymnasium[classic_control] pygame-ce matplotlib`

## Instrucciones de ejecución
El proyecto cuenta con varios scripts según lo que se desee probar. Recuerda ejecutarlos desde la carpeta raíz.

**A) Iniciar el Entrenamiento de la IA:**
Inicia el bucle de aprendizaje. Al finalizar, genera un archivo de pesos y una gráfica.
> `python src/entrenador.py`

**B) Visualizar al Agente en el entorno:**
Abre la interfaz gráfica para ver cómo la IA toma decisiones en tiempo real usando el motor Pygame.
> `python src/visualizacion.py`

**C) Ejecutar las Pruebas Unitarias:**
Ejecuta la batería de tests para comprobar la integridad de las clases POO.
> `python -m unittest tests/tests.py`

## Configuración necesaria
* **Variables de entorno:** No se requieren `.env` para la simulación local.
* **Credenciales de prueba:** El sistema de simulación no requiere login, autenticación JWT ni base de datos externa por el momento.
* **Hiperparámetros:** Variables como `learning_rate`, `batch_size` o `episodios` se pueden configurar directamente en los constructores de las clases dentro del código fuente.

## Funcionalidades implementadas (80% Operativo)
* ✅ **Arquitectura DQN:** Red neuronal multicapa programada con PyTorch.
* ✅ **Programación Orientada a Objetos (POO):** Clases estructuradas (`Agente`, `Memoria`, `Entrenador`) siguiendo el diagrama UML del proyecto.
* ✅ **Gestión de Memoria (Replay Buffer):** Almacenamiento circular de experiencias pasadas para entrenar en lotes aleatorios.
* ✅ **Bucle de Entrenamiento:** Lógica matemática de recompensa/castigo, cálculo de pérdida (MSE) y optimización de pesos (Adam).
* ✅ **Métricas:** Generación automática de gráficas de la curva de aprendizaje.
* ✅ **Testing:** Pruebas unitarias de las clases core del sistema.

## Funcionalidades pendientes
* ⏳ **Carga dinámica de modelos:** Lograr que `visualizacion.py` lea automáticamente el archivo de pesos entrenado para que el agente juegue como un experto, en lugar de instanciar una red vacía.
* ⏳ **Integración Intermodular:** Posible conexión de los resultados y métricas del agente con el módulo de Sistemas de Gestión Empresarial.

## Problemas conocidos
* 🐛 En entornos WSL (Windows Subsystem for Linux) o servidores sin interfaz gráfica, la librería `pygame-ce` puede lanzar un error "Headless" al no poder abrir la ventana de visualización. Se soluciona ejecutando el código desde CMD/PowerShell en Windows nativo.

## Capturas de pantalla

* **Ejecución del Entrenamiento:** <img width="1290" height="263" alt="Captura de pantalla 2026-04-26 174701" src="https://github.com/user-attachments/assets/65258eae-4a2f-41e5-9213-5052c26ea33f" />
* **Entorno Gráfico CartPole:** <img width="620" height="437" alt="Captura de pantalla 2026-04-26 174731" src="https://github.com/user-attachments/assets/446cfd5d-db04-40dc-a483-87ebebed75c0" />
* **Gráfica de Aprendizaje:** <img width="637" height="480" alt="Captura de pantalla 2026-04-26 174757" src="https://github.com/user-attachments/assets/9449a967-493b-4cc5-9135-dde16f33d831" />
* **Pruebas Unitarias:** <img width="569" height="145" alt="Captura de pantalla 2026-04-26 174858" src="https://github.com/user-attachments/assets/23dd026d-a27a-4dc9-935e-913148862e75" />
* **Estructura del Proyecto:** <img width="257" height="472" alt="Captura de pantalla 2026-04-26 175628" src="https://github.com/user-attachments/assets/7eb976c4-6f88-45fc-9048-f937e75e8ec9" />

## Autor y Contacto
* **Desarrollador:** Maximiliano González Segura - 2º DAM
* **GitHub:** [Maaxii00](https://github.com/Maaxii00)
