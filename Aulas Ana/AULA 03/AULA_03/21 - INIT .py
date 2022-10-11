#essa função serve para caractrizar 

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

NovaPessoa = Pessoa("João","16")

print(NovaPessoa.nome)
print(NovaPessoa.idade)