class Plato:
    def __init__(self, codigo, nombre, precio, porciones):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.porciones = porciones

    def puede_servir(self, cantidad):
        return 0 < cantidad <= self.porciones

    def servir(self, cantidad):
        if not self.puede_servir(cantidad):
            return False
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

    def registrar_plato(self, nombre, precio, porciones):
        codigo = len(self.platos) + 1
        plato = Plato(codigo, nombre.strip(), float(precio), int(porciones))
        self.platos.append(plato)
        return plato

    def buscar_plato(self, codigo):
        for plato in self.platos:
            if plato.codigo == codigo:
                return plato
        return None

    def servir_plato(self, plato, cantidad):
        if plato.servir(cantidad):
            return plato
        return None