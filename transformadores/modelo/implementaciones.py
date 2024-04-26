from transformadores.modelo.abstracciones import Transformador


class Encrypt(Transformador):
    def to_morse(self, string) -> str:
        morse_code = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
        }

        morse_text = ''
        for char in string.upper():
            if char in morse_code:
                morse_text += morse_code[char] + ' '
            else:
                morse_text += char

        return morse_text.strip()

    def to_binary(self, string: str) -> str:

        bytes_string: bytes = string.encode('utf-8')
        binario: str = ' '.join(format(byte, '08b') for byte in bytes_string)
        return binario

    def to_cesar(self, string: str, desplazamiento=5) -> str:
        resultado = ""
        for char in string:
            if char.isalpha():  # Verificar si el carácter es una letra
                # Obtener el código ASCII del carácter y ajustar el desplazamiento
                codigo = ord(char) + desplazamiento
                if char.islower():
                    if codigo > ord('z'):
                        codigo -= 26
                    elif codigo < ord('a'):
                        codigo += 26
                elif char.isupper():
                    if codigo > ord('Z'):
                        codigo -= 26
                    elif codigo < ord('A'):
                        codigo += 26
                resultado += chr(codigo)
            else:
                resultado += char  # Conservar caracteres que no son letras
        return resultado

    def transformar(self, string: str, type: int) -> str:
        if type == 1:
            return self.to_binary(string)
        elif type == 2:
            return self.to_morse(string)
        elif type == 3:
            return self.to_cesar(string)
        else:
            return string.capitalize()


class TransformText(Transformador):
    def transformar(self, text: str, tipo: int) -> str:
        if tipo == 1:
            morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                          'H': '....',
                          'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                          'P': '.--.',
                          'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
                          'X': '-..-',
                          'Y': '-.--', 'Z': '--..'}
            morse_text = []
            for i in text.upper():
                if i in morse_code:
                    morse_text.append(morse_code[i])
                elif i == ' ':
                    morse_text.append(' ')
            return ' '.join(morse_text)

        elif tipo == 2:
            binary_text = ' '.join(format(ord(i), '08b') for i in text)
            return binary_text

        elif tipo == 3:
            numbers_text = []
            for i in text:
                if i.isalpha():
                    numbers_text.append(str(ord(i) - 64))
                else:
                    numbers_text.append(i)
            return ' '.join(numbers_text)


class CambiosTxt(Transformador):

    def texto_invertido(self, string: str):
        texto_invertido = ''.join(palabra[::-1] for palabra in string.split())
        return texto_invertido

    def texto_mayusculas(self, string: str):
        mayusculas = string.upper()
        return mayusculas

    def admiracion(self, string: str):
        texto_nuevo = string + '!'
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
