from abc import ABC, abstractmethod


class Transformador(ABC):
    @abstractmethod
    def transformador(self, s: str, tipo: int) -> int:
        pass


class Cambio(Transformador):
    def transformador(self, s: str, tipo: int) -> int:
        suma = 0
        for i in s:
            if "a" <= i <= "z" or "A" <= i <= "Z":
                valor_letra = ord(i.lower()) - ord("a") + 1
                suma += valor_letra
        return suma + tipo


class Inverso(Transformador):
    def transformador(self, s: str, tipo: int) -> int:
        if tipo > 0:
            tipo -= 2 * tipo
        else:
            tipo += 2 * tipo
        return tipo


class Multiplicado(Transformador):
    def transformador(self, s: str, tipo: int) -> int:
        caracteres = len(s)
        resultado = caracteres * tipo
        return resultado
