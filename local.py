class Local:
    def __init__(self, numero, typeLocal):
        self.numero = numero
        self.typeLocal = typeLocal

    def __str__(self):
        return "[local numero:  " + str(self.numero) + " typeLocal: " + self.typeLocal + "]"