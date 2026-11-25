class ControladorRestaurante:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        while True:
            opcion = self.vista.menu()

            if opcion == "1":
                nombre = self.vista.pedir_nombre()
                precio = self.vista.pedir_precio()
                porciones = self.vista.pedir_porciones()
                try:
                    plato = self.modelo.registrar_plato(nombre, precio, porciones)
                except ValueError as error:
                    clave = str(error)
                    if clave in self.vista.ERRORES:
                        self.vista.mostrar_error_caso(clave)
                    else:
                        self.vista.mostrar_error(clave)
                    continue
                self.vista.mostrar_plato_registrado(plato.codigo)

            elif opcion == "2":
                if not self.modelo.platos:
                    self.vista.mostrar_error_caso("sin platos")
                else:
                    self.vista.mostrar_platos(self.modelo.platos)

            elif opcion == "3":
                codigo = self.vista.pedir_codigo()
                try:
                    plato = self.modelo.buscar_plato(codigo)
                except ValueError as error:
                    clave = str(error)
                    if clave in self.vista.ERRORES:
                        self.vista.mostrar_error_caso(clave)
                    else:
                        self.vista.mostrar_error(clave)
                    continue

                cantidad = self.vista.pedir_cantidad()
                try:
                    plato = self.modelo.servir_plato(codigo, cantidad)
                except ValueError as error:
                    clave = str(error)
                    if clave in self.vista.ERRORES:
                        self.vista.mostrar_error_caso(clave)
                    else:
                        self.vista.mostrar_error(clave)
                    continue
                self.vista.mostrar_plato_servido(plato.porciones)

            elif opcion == "4":
                self.vista.mostrar_mensaje("programa acabadi.")
                break

            else:
                self.vista.mostrar_error_caso("opcion invalida")