if __package__:
    from .controlador import ControladorRestaurante
    from .modelo import Restaurante
    from .vista import VistaOperaciones
else:
    from controlador import ControladorRestaurante
    from modelo import Restaurante
    from vista import VistaOperaciones


def main():
    modelo = Restaurante()
    vista = VistaOperaciones()
    controlador = ControladorRestaurante(modelo, vista)
    controlador.ejecutar()


if __name__ == "__main__":
    main()
