class Funcion:
    def __init__(self, codigo, pelicula, precio, asientos):
        self.codigo = codigo
        self.pelicula = pelicula
        self.precio = precio
        self.asientos = asientos

    def __str__(self):
        return (
            f"{self.codigo:<10}{self.pelicula:<28}"
            f"${self.precio:<12.2f}{self.asientos:<10}"
        )


class Cine:
    def __init__(self):
        self.funciones = [
            Funcion(1, "Coco", 4.50, 80),
            Funcion(2, "Intensamente 2", 4.50, 60),
            Funcion(3, "Moana 2", 5.00, 40),
        ]

    def registrar(self, pelicula, precio, asientos):
        pelicula = pelicula.strip()
        if not pelicula:
            raise ValueError("el nombre de la pelicula es obligatorio.")
        if "," in pelicula:
            raise ValueError("el nombre de la pelicula no puede contener comas.")

        try:
            precio = float(precio)
        except (TypeError, ValueError):
            raise ValueError("el precio debe ser mayor que 0.") from None
        if precio <= 0:
            raise ValueError("el precio debe ser mayor que 0.")

        try:
            asientos = int(asientos)
        except (TypeError, ValueError):
            raise ValueError("los asientos deben ser un numero entero mayor que 0.") from None
        if asientos <= 0:
            raise ValueError("los asientos deben ser mayor que 0.")

        codigo = max(funcion.codigo for funcion in self.funciones) + 1
        funcion = Funcion(codigo, pelicula, precio, asientos)
        self.funciones.append(funcion)
        return funcion
