class VistaOperaciones:
    def menu(self):
        print()
        print("======RESTAURANTE SABOR CUENCANO")
        print("MENU")
        print("1. Registrar plato")
        print("2. Mostrar platos")
        print("3. Servir platos") 
        print("4. Salir\n")
        return input("Seleccione una opcion: \n")

    def pedir_nombre(self):
        return input("Nombre: ")

    def pedir_precio(self):
        return input("Precio: ")

    def pedir_porciones(self):
        return input("Porciones: ")

    def pedir_codigo(self):
        return input("Codigo: ")

    def pedir_cantidad(self):
        return input("Cantidad: ")

    def mostrar_platos(self, platos):
        print("codigo---Nombre---Precio---Porciones")
        for plato in platos:
            print(plato)

    def mostrar_error(self, mensaje):
        print(mensaje)

    def mostrar_plato_registrado(self, codigo):
        print(f"Registrado con el codigo {codigo}.")

    def mostrar_plato_servido(self, porciones):
        print(f"Listo. Quedan {porciones} porciones.")

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
