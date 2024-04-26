from transformadores.modelo.abstracciones import Transformador
from transformadores.modelo.implementaciones import Encrypt, CambiosTxt, TransformText
from transformadores.ui.consola import App


def seleccionar_metodo():
    print("---metodos para transformar---\n")
    print("1. metodo 1")
    print("2. metodo 2")
    print("3. metodo 3")
    print("4. metodo 4")

    return int(input("Seleccione un método para transformar: "))


def obtener_transformador(method_transformer: int) -> Transformador:
        if method_transformer == 1:
            return Encrypt()
        if method_transformer == 2:
            return TransformText()
        if method_transformer == 3:
            return CambiosTxt()
        if method_transformer == 4:
            raise NotImplementedError


if __name__ == "__main__":
    metodo = seleccionar_metodo()
    transformador: Transformador = obtener_transformador(metodo)

    app = App(transformador)
    app.main()
