class App:
    def __init__(self, objeto: Transformador):
        self.objeto = objeto

    def mostrar_menu(self):
        print("\n--- Menú ---")
        print("1. Transformar string")
        print("2. Salir")

    def main(self):
        while True:
            string = input("\nIngrese un string: ")

            self.mostrar_menu()

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.obtener_transformador()

            if opcion == "2":
                print("Hasta pronto")
                print("Saliendo.....")
                break

    def obtener_transformador(self, tipo):
        pass