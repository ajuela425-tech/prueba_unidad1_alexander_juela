class Plato:
    def __init__(self, codigo, nombre, precio, porciones):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.porciones = porciones
        self.validar()

    def validar(self):
        self.nombre = Restaurante.validar_nombre(self.nombre)
        self.precio = Restaurante.validar_precio(self.precio)
        self.porciones = Restaurante.validar_porciones(self.porciones)

    def servir(self, cantidad):
        if cantidad <= 0:
            raise ValueError("Error: la cantidad debe ser mayor que cero.")
        if cantidad > self.porciones:
            raise ValueError(f"Error: solo hay {self.porciones} porciones.")
        self.porciones -= cantidad
        return True

    def __str__(self):
        return f"{self.codigo:<8}{self.nombre:<24}{self.precio:<18.2f}{self.porciones:<14}"


class Restaurante:
    def __init__(self):
        self.platos = [
            Plato(1, "Mote pillo", 3.50, 30),
            Plato(2, "Hornado", 6.00, 20),
        ] 

    @staticmethod
    def validar_nombre(nombre):
        if not nombre.strip():
            raise ValueError("Error: el campo no puede estar vacio.")
        return nombre.strip()

    @staticmethod
    def validar_precio(precio):
        try:
            valor = float(precio)
        except (TypeError, ValueError):
            raise ValueError("Error: ingrese solo numero") from None
        if valor <= 0 or valor > 1000000:
            raise ValueError("Error: el valor debe ser mayor que cero.")
        return valor

    @staticmethod
    def validar_porciones(porciones):
        try:
            valor = int(porciones)
        except (TypeError, ValueError):
            raise ValueError("Error: ingrese solo numeros.") from None
        if valor < 0:
            raise ValueError("Error: el valor debe ser mayor o igual a 0.")
        return valor

    @staticmethod
    def validar_codigo(codigo):
        try:
            return int(codigo)
        except (TypeError, ValueError):
            raise ValueError("Error: ingrese solo numeros.") from None

    @staticmethod
    def validar_cantidad(cantidad):
        try:
            return int(cantidad)
        except (TypeError, ValueError):
            raise ValueError("Error: ingrese solo numeros.") from None

    def registrar_plato(self, nombre, precio, porciones):
        nombre = self.validar_nombre(nombre)
        precio = self.validar_precio(precio)
        porciones = self.validar_porciones(porciones)
        codigo = len(self.platos) + 1
        plato = Plato(codigo, nombre, precio, porciones)
        self.platos.append(plato)
        return plato

    def buscar_plato(self, codigo):
        codigo = self.validar_codigo(codigo)
        for plato in self.platos:
            if plato.codigo == codigo:
                return plato
        raise ValueError("Error: no existe ese codigo.")

    def servir_plato(self, codigo, cantidad):
        plato = self.buscar_plato(codigo)
        if plato is None:
            raise ValueError("Error: no existe ese codigo.")
        cantidad = self.validar_cantidad(cantidad)
        plato.servir(cantidad)
        return plato
