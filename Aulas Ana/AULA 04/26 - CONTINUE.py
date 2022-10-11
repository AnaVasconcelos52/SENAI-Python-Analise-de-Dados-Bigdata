
# Função "continue" retorna para o inicio do loop

var = 10

while var>0:
    var -= 1

    if(var == 5):
        continue

    print(f"Valor: {var}")

print("Tchau, tchau")