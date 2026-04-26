import torch
import torch.nn as nn
import torch.nn.functional as F

class DQN(nn.Module):
    def __init__(self, input_shape, n_actions):
        # Heredamos de nn.Module, que es lo que nos da PyTorch para poder crear redes neuronales
        super(DQN, self).__init__()
        
        # Primera capa (Capa de entrada)
        # Aquí entran los 4 datos que nos da el entorno del juego, utilizamos nn.Linear para conectar esos 4 datos iniciales con 128 neuronas.
        # Usamos Linea porque obliga a que cada dato de entrada se conecte con todas y cada una de las neuronas.
        self.fc1 = nn.Linear(input_shape, 128)
        
        # Segunda capa (Capa oculta)
        # Pasamos la información de las 128 neuronas anteriores a otro bloque de 128 neuronas. 
        # Añadir esta capa intermedia es lo que da profundidad a la red y le permite procesar patrones más complejos.
        self.fc2 = nn.Linear(128, 128)
        
        # Tercera capa (Capa de salida)
        # Cogemos las 128 neuronas de la capa anterior y las reducimos al número de acciones que podemos hacer (2: izquierda o derecha).
        # El resultado final serán dos valores numéricos.
        self.fc3 = nn.Linear(128, n_actions)

    def forward(self, x):
        
        # Pasamos los datos por la primera capa y al resultado le aplicamos la función matemática ReLU la cuál 
        # coge cualquier valor negativo y lo convierte en 0, lo necesitamos porque sino la red solo podría entender problemas muy simples
        x = F.relu(self.fc1(x))
        
        # Repetimos el mismo proceso para la segunda capa: pasamos los datos y volvemos a aplicar ReLU.
        x = F.relu(self.fc2(x))
        
        # Pasamos los datos por la capa de salida.
        # Hacemos esto porque queremos los valores puros de las acciones, y estos valores (que indican lo buena o mala que es una acción) sí que pueden ser negativos.
        actions_value = self.fc3(x)
        
        return actions_value