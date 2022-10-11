class Fruta:
    def __init__(self,tipo,cor):
        self.tipo = tipo
        self.cor = cor

    def MostrarPropriedades(self):
        print(f"Sou um(a) {self.tipo} e sou {self.cor}!")

NovaFruta =Fruta("Banana","amarela")


NovaFruta.MostrarPropriedades()


