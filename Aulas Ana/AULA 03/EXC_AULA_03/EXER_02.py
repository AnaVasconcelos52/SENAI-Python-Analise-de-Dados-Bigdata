class Bola:
    def __init__(self,cor,circunferencia,material):
        self._cor = cor
        self._circunferencia = circunferencia
        self._material = material
        

    def trocaCor(self,novaCor):
        self._cor = novaCor
    
    def mostrarCor(self):
        print(self._cor)

bola = Bola("Branca",20,"Elastico")

bola.mostrarCor()
bola.trocaCor("Azul")
bola.mostrarCor()


    