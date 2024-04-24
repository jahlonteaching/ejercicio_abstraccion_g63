class Transformador:
    def __init__(self, s: str, tipo: int):
        self.s: str = s
        self.tipo: int = tipo


class Transformador_1(Transformador):
    def metodo_morse(self):
        codigo_morse = {
            'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
            'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
            'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',
            'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'
        }

        morse = " ".join([codigo_morse.get(letra.lower(), " ") for letra in self.s])
        return morse


class Transformador_2(Transformador):
    pass


class Transformador_3(Transformador):
    pass