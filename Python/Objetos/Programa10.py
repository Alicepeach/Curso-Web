class Palabra():
    sinVocales=""
    def __init__(self,palabra):
            vocales="aeiou"
            for letra in palabra:
                if letra in vocales:
                      continue
                self.sinVocales += letra