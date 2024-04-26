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

                self.seleccionar_metodo()
                self.seleccionar_tipo()
                opcion_tipo = input("seleccione una opción: ")
                string_transformado = self.objeto.transformar(string, opcion_tipo)
                print("Resultado: ", string_transformado)



            if opcion == "2":
                print("Hasta pronto")
                print("Saliendo.....")
                break


    def seleccionar_metodo(self):
        print("---metodos para transformar---\n")
        print("1. metodo 1")
        print("2. metodo 2")
        print("3. metodo 3")
        print("4. metodo 4")

        usuario_input = input("Seleccione un método para transformar: ")

        self.obtener_transformador(usuario_input)


    def seleccionar_tipo(self):
        print("---Tipos de transformación---\n")
        print("1. Tipo 1")
        print("2. Tipo 2")
        print("3. Tipo 3")


    def obtener_transformador(self, method_transformer: int) -> Transformador:
        pass

