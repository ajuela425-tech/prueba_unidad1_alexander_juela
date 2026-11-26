#Alexander Juela y Andersson Bermejo
from controlador_cine import ControladorCine
from modelo_cine import Cine
from vista_cine import VistaCine


def main():
    modelo = Cine()
    vista = VistaCine()
    controlador = ControladorCine(modelo, vista)
    controlador.ejecutar()


if __name__ == "__main__":
    main()
