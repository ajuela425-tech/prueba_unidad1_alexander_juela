class ControladorCine:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        while True:
            opcion = self.vista.menu()

            if opcion == "1":
                pelicula = self.vista.pedir_nombre()
                precio = self.vista.pedir_precio()
                asientos = self.vista.pedir_asientos()
                try:
                    funcion = self.modelo.registrar(pelicula, precio, asientos)
                except ValueError as error:
                    self.vista.mostrar_error(str(error))
                else:
                    self.vista.mostrar_mensaje(
                        f"Funcion registrada con el codigo {funcion.codigo}."
                    )

            elif opcion == "2":
                self.vista.mostrar_funciones(self.modelo.funciones)

            elif opcion == "8":
                self.vista.mostrar_mensaje("Programa finalizado.")
                break
            elif opcion in ("3", "4", "5", "6", "7"):
                continue
            else:
                self.vista.mostrar_error("opcion invalida; seleccione del 1 al 8.")
