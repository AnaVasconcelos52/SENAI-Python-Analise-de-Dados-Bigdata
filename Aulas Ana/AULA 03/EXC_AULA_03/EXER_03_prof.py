class Quadrado:
    def __init__(self,lado):
        self._tamanho_do_lado = lado

    def mudarValorDoLado(self,novo_lado):
        self._tamanho_do_lado = novo_lado

    def retornarValorDoLado(self):
        return self._tamanho_do_lado 

    def calcularArea(self):
        return (self._tamanho_do_lado * self._tamanho_do_lado)

NovoQuadrado = Quadrado (8)

print(NovoQuadrado.retornarValorDoLado())
NovoQuadrado.mudarValorDoLado(5)
print(NovoQuadrado.retornarValorDoLado())
print(NovoQuadrado.calcularArea())