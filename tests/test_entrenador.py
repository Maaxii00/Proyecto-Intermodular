import unittest
from src.memoria import Memoria
from src.agente import Agente
from src.entrenador import Entrenador

class TestEntrenador(unittest.TestCase):

    def test_inicializacion_componentes(self):
        entrenador_prueba = Entrenador(episodios=10) 
        
        self.assertIsNotNone(entrenador_prueba.env, "El entorno de Gymnasium no se ha inicializado")
        self.assertIsInstance(entrenador_prueba.agente, Agente, "El entrenador no ha creado a su Agente")
        self.assertIsInstance(entrenador_prueba.memoria, Memoria, "El entrenador no ha creado la Memoria")
        self.assertEqual(entrenador_prueba.episodios, 10, "La configuración de episodios no se ha guardado correctamente")

if __name__ == '__main__':
    unittest.main()