from modelo.abstraccion import Transformador

class Transformador1(Transformador):
    def __init__(self, texto):
        self.texto = texto

    def texto_invertido(self):
        print("antes de la transformación")
        print(self.texto)
        texto_invertido = ''.join(palabra[::-1] for palabra in self.texto.split())
        print(self.texto_invertido)

    def texto_mayusculas(self):
        print("antes de la transformación")
        print(self.texto)
        mayusculas = self.texto.upper()
        print(self.mayusculas)

    def admiracion(self):
        print("antes de la transformación")
        print(self.texto)
        texto_nuevo = self.texto + '!'
        print(texto_nuevo)

    def transformar(self, string: str, tipo: int) -> str:
        if tipo == 1:
            return self.texto_invertido(string)
        elif tipo == 2:
            return self.texto_mayusculas(string)
        elif tipo == 3:
            return self.admiracion(string)
        else:
            return string.capitalize()



