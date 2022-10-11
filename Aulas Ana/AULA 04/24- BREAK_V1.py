
#a função break serve para encerrar o loop e retornar a execução da proxima instrução

var = int(input("Digite um numero maior que 5:"))

while var > 0:
    print(f"var: {var}")

    #var = var -1
    var -= 1

    if(var == 5):
        print("Vou sairdo while")
        break

print("Tchau, tchau")


