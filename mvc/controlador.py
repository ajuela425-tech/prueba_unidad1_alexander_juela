class ControladorRestaurante:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def _parsear_nombre(self, texto):
        limpio = texto.strip()
        if not limpio:
            raise ValueError("nombre_vacio")
        return limpio

    def _parsear_precio(self, texto):
        try:
            valor = float(texto)
        except (TypeError, ValueError):
            raise ValueError("precio_invalido") from None
        if valor <= 0 or valor > 1000000:
            raise ValueError("precio_invalido")
        return valor

    def _parsear_entero_positivo(self, texto, clave_error, permitir_cero=False):
        try:
            valor = int(texto)
        except (TypeError, ValueError):
            raise ValueError(clave_error) from None
        if permitir_cero:
            if valor < 0:
                raise ValueError(clave_error)
        else:
            if valor <= 0:
                raise ValueError(clave_error)
        return valor

    def _mostrar_error(self, clave_o_mensaje):
        if hasattr(self.vista, "ERRORES") and clave_o_mensaje in self.vista.ERRORES:
            self.vista.mostrar_error_caso(clave_o_mensaje)
        else:
            self.vista.mostrar_error(clave_o_mensaje)

    def ejecutar(self):
        while True:
            opcion = self.vista.menu()

            if opcion == "1":
                nombre_raw = self.vista.pedir_nombre()
                try:
                    nombre = self._parsear_nombre(nombre_raw)
                except ValueError as error:
                    self._mostrar_error(str(error))
                    continue

                precio_raw = self.vista.pedir_precio()
                try:
                    precio = self._parsear_precio(precio_raw)
                except ValueError as error:
                    self._mostrar_error(str(error))
                    continue

                porciones_raw = self.vista.pedir_porciones()
                try:
                    porciones = self._parsear_entero_positivo(
                        porciones_raw, "porciones_invalidas", permitir_cero=True
                    )
                except ValueError as error:
                    self._mostrar_error(str(error))
                    continue

                try:
                    plato = self.modelo.registrar_plato(nombre, precio, porciones)
                except ValueError as error:
                    self._mostrar_error(str(error))
                    continue

                self.vista.mostrar_plato_registrado(plato.codigo)

            elif opcion == "2":
                if not self.modelo.platos:
                    self._mostrar_error("sin platos")
                else:
                    self.vista.mostrar_platos(self.modelo.platos)

            elif opcion == "3":
                codigo_raw = self.vista.pedir_codigo()
                try:
                    codigo = self._parsear_entero_positivo(
                        codigo_raw, "codigo no encontrado", permitir_cero=False
                    )
                except ValueError as error:
                    self._mostrar_error(str(error))
                    continue

                plato = self.modelo.buscar_plato(codigo)
                if plato is None:
                    self._mostrar_error("codigo no encontrado")
                    continue

                cantidad_raw = self.vista.pedir_cantidad()
                try:
                    cantidad = self._parsear_entero_positivo(
                        cantidad_raw, "cantidad invalida", permitir_cero=False
                    )
                except ValueError as error:
                    self._mostrar_error(str(error))
                    continue

                if not plato.puede_servir(cantidad):
                    self._mostrar_error("porciones insuficientes")
                    continue

                try:
                    servido = self.modelo.servir_plato(plato, cantidad)
                except ValueError as error:
                    self._mostrar_error(str(error))
                    continue

                if servido is None:
                    self._mostrar_error("porciones_insuficientes")
                    continue

                self.vista.mostrar_plato_servido(servido.porciones)

            elif opcion == "4":
                self.vista.mostrar_mensaje("programa finalizado.")
                break

            else:
                self._mostrar_error("opcion_invalida")