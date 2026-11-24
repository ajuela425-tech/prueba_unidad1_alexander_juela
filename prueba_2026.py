class Plato:
    def __init__(self, codigo, nombre, precio, porciones):
        self.codigo= codigo
        self.nombre= nombre
        self.precio= precio
        self.porciones= porciones

    def servir(self, cantidad):
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor que cero.")
            return False
        if cantidad > self.porciones:
            print(f"Error: solo hay {self.porciones} porciones.")
            return False
        self.porciones -= cantidad
        return True

    def __str__(self):
        return f"{self.codigo:<8}{self.nombre:<24}{self.precio:<18.2f}{self.porciones:<14}"


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Error: el campo no puede estar vacio.")


def leer_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Error: ingrese solo numeros.")
            continue
        if minimo is not None and valor < minimo:
            print(f"Error: el valor debe ser mayor o igual a {minimo}.")
            continue
        return valor

def leer_decimal(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
        except ValueError:
            print("Error: ingrese solo numero")
            continue
        if valor <= 0 or valor > 1000000:
            print("Error: el valor debe ser mayor que cero.")
            continue
        return valor

def buscar(lista, codigo):
    for elemento in lista:
        if elemento.codigo == codigo:
            return elemento
    return None


lista = [
    Plato(1, "Mote pillo", 3.50, 30),
    Plato(2, "Hornado", 6.00, 20),

]

while True:
    print()
    print("======RESTAURANTE SABOR CUENCANO")
    print("MENU")
    print("1. Registrar plato")
    print("2. Mostrar platos")
    print("3. Servir platos")
    print("4. Salir\n")
    opcion = input("Seleccione una opcion: \n")

    if opcion == "1":
        nombre = leer_texto("Nombre: ")
        precio = leer_decimal("Precio: ")
        porciones = leer_entero("Porciones: ", 0)
        codigo = len(lista) + 1
        lista.append(Plato(codigo, nombre, precio, porciones))
        print(f"Registrado con el codigo {codigo}.")
    elif opcion == "2":
        print("codigo---Nombre---Precio---Porciones")
        for elemento in lista:
            print(elemento)
    elif opcion == "3":
        codigo = leer_entero("Codigo: ")
        elemento = buscar(lista, codigo)
        if elemento is None:
            print("Error: no existe ese codigo.")
        else:
            cantidad = leer_entero("Cantidad: ")
            if elemento.servir(cantidad):
                print(f"Listo. Quedan {elemento.porciones} porciones.")
    elif opcion == "4":
        print("programa finalizado.")
        break
    else:
        print("opcion invalida.")