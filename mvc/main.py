from modelo import Restaurante
from vista import VistaOperaciones
from controlador import ControladorRestaurante

modelo = Restaurante()
vista = VistaOperaciones()
controlador = ControladorRestaurante(modelo, vista)
controlador.ejecutar() 