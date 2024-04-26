class Transformador:
    def __init__(self):
        self.texto = texto
    def metodo_1(self):
        print("Este es el después")

class Transformador1(Transformador):
    def metodo_1(self):
        print("antes de la transformación")
        print(texto_usuario)
        super().metodo_1()
        self.texto_invertido = ''.join(palabra[::-1] for palabra in self.texto.split())
        print(self.texto_invertido)

    def metodo_2(self):
        print("antes de la transformación")
        print(texto_usuario)
        super().metodo_1()
        self.mayusculas = texto_usuario.upper()
        print(self.mayusculas)

    def metodo_3(self):
        print("antes de la transformación")
        print(texto_usuario)
        super().metodo_3()
        texto_nuevo = self.texto + '!'
        print(texto_nuevo)
