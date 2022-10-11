nome = input("Qual o seu nome? R:")

def EscreveValor(caracter,quantidade):

    variavel =  ""

    for n in quantidade:

        variavel+=caracter
        
    return variavel

print(EscreveValor("=",40))
print(f"|{nome}====================================")