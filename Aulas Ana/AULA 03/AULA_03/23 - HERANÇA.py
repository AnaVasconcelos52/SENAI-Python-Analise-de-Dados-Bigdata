class Animal():
    def __init__(self,nome,cor,comida):
        self.__nome = nome
        self.__cor = cor
        self.__comida = comida


#função comer
    def comer(self):
        print(f"o {self.__nome} é {self.__cor} e está comendo {self.__comida}")

class Gato(Animal):
    def __init__(self,nome,cor,comida):
        super().__init__(nome,cor,comida)

class Cachorro(Animal):
    def __init__(self,nome,cor,comida):
        super().__init__(nome,cor,comida)

class Coelho(Animal):
    def __init__(self,nome,cor,comida):
        super().__init__(nome,cor,comida)

class Passaro(Animal):
    def __init__(self,nome,cor,comida):
        super().__init__(nome,cor,comida)

class Elefante(Animal):
    def __init__(self,nome,cor,comida):
        super().__init__(nome,cor,comida)


gato = Gato("Rabixo","azul","rato")
cachorro = Cachorro("Luke","preto","manga")
coelho = Coelho("Orelhudo", "rosa","cenoura")
passaro = Passaro("Piu Piu","amarelo","alpiste")
elefante =Elefante("Dumbo","cinza","amendoim")


#função de comer feita no def
gato.comer()
cachorro.comer()
coelho.comer()
passaro.comer()
elefante.comer()

