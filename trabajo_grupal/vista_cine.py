class VistaCine:
    def menu(self):
        print("\n====== CINE CUENCA PLAZA ======")
        print("1. Registrar funcion")
        print("2. Mostrar funciones")
        print("3. Vender entradas")
        print("4. Buscar por nombre")
        print("5. Anular entrada")
        print("6. Mostrar entradas")
        print("7. Reporte general")
        print("8. Salir")
        return input("Seleccione una opcion: ")

    def pedir_nombre(self):
        return input("Nombre de la pelicula: ")

    def pedir_precio(self):
        return input("Precio: ")

    def pedir_asientos(self):
        return input("Cantidad de asientos: ")

    def mostrar_funciones(self, funciones):
        print(f"\n{'Codigo':<10}{'Pelicula':<28}{'Precio':<13}{'Asientos':<10}")
        print("-" * 61)
        for funcion in funciones:
            print(funcion)

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

    def mostrar_error(self, mensaje):
        print(f"Error: {mensaje}")
