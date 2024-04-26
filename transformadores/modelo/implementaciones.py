from transformadores.modelo.abstracciones import Transformador


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
            for i in self.s:
                if i.isalpha():
                    numbers_text.append(str(ord(i) - 64))
                else:
                    numbers_text.append(i)
            return ' '.join(numbers_text)