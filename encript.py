
class Encrypt:
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

