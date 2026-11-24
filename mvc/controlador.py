if __package__:
    from .modelo import Restaurante
    from .vista import VistaOperaciones
else:
    from modelo import Restaurante
    from vista import VistaOperaciones


class ControladorRestaurante:
    def __init__(self, modelo=None, vista=None):
        self.modelo = modelo if modelo is not None else Restaurante()
        self.vista = vista if vista is not None else VistaOperaciones()

    def ejecutar(self):
        while True:
            opcion = self.vista.menu()

            if opcion == "1":
                self.registrar_plato()
            elif opcion == "2":
                self.vista.mostrar_platos(self.modelo.platos)
            elif opcion == "3":
                self.servir_plato()
            elif opcion == "4":
                self.vista.mostrar_mensaje("programa finalizado.")
                break
            else:
                self.vista.mostrar_mensaje("opcion invalida.")

    def _pedir_valor(self, pedir, validar):
        while True:
            valor = pedir()
            try:
                return validar(valor)
            except ValueError as error:
                self.vista.mostrar_error(str(error))

    def registrar_plato(self):
        nombre = self._pedir_valor(
            self.vista.pedir_nombre, self.modelo.validar_nombre
        )
        precio = self._pedir_valor(
            self.vista.pedir_precio, self.modelo.validar_precio
        )
        porciones = self._pedir_valor(
            self.vista.pedir_porciones, self.modelo.validar_porciones
        )
        try:
            plato = self.modelo.registrar_plato(nombre, precio, porciones)
        except ValueError as error:
            self.vista.mostrar_error(str(error))
            return
        self.vista.mostrar_plato_registrado(plato.codigo)

    def servir_plato(self):
        codigo = self._pedir_valor(
            self.vista.pedir_codigo, self.modelo.validar_codigo
        )
        try:
            plato = self.modelo.buscar_plato(codigo)
        except ValueError as error:
            self.vista.mostrar_error(str(error))
            return

        cantidad = self._pedir_valor(
            self.vista.pedir_cantidad, self.modelo.validar_cantidad
        )
        try:
            plato = self.modelo.servir_plato(codigo, cantidad)
        except ValueError as error:
            self.vista.mostrar_error(str(error))
            return
        self.vista.mostrar_plato_servido(plato.porciones)
