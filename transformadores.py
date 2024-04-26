class Transformador:
    def __init__(self, s: str, tipo: int) -> int:
        self.s: str = s
        self.tipo: int = tipo


class Mayusculas(Transformador):
    def transformar(self, cadena: str):
        return cadena.upper()


class Minusculas(Transformador):
    def transformar(self, cadena: str):
        return cadena.lower()


class Divisor(Transformador):
    def transformar(self, cadena: str):
        return cadena.split()
