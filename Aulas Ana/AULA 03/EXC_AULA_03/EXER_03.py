class Quadrado:
    def __init__(self,tamanhoLado):
        self._tamanhoLado = tamanhoLado

    def trocarValor (self,novoLado):
        self._tamanhoLado = novoLado

    def mostrarLado (self):
        area = float(self._tamanhoLado**2)
        print(area)

quadrado = Quadrado (2)


quadrado.mostrarLado()
quadrado.trocarValor(3)
quadrado.mostrarLado()

