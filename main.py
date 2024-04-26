class Transformador:
    def __init__(self, s: str, tipo: int):
        self.s: str = s
        self.tipo: int = tipo


class MorseConverter(Transformador):
    def convert_to_morse(self):
        morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                      'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                      'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                      'Y': '-.--', 'Z': '--..'}
        morse_text = []
        for i in self.s.upper():
            if i in morse_code:
                morse_text.append(morse_code[i])
            elif i == ' ':
                morse_text.append(' ')
        return ' '.join(morse_text)


class BinaryConverter(Transformador):
    def convert_to_binary(self):
        binary_text = ' '.join(format(ord(i), '08b') for i in self.s)
        return binary_text


class LetterToNumberConverter(Transformador):
    def convert_to_numbers(self):
        numbers_text = []
        for i in self.s:
            if i.isalpha():
                numbers_text.append(str(ord(i) - 64))
            else:
                numbers_text.append(i)
        return ' '.join(numbers_text)
