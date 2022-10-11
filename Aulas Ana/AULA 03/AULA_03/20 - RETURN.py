
# o *args da paa usar varios parametros, não precisa defirnir, o programa faz automatico

def MenorNumero(*args):
    oMenor = 9999999
    for x in args:
        if(oMenor >= x):
            oMenor = x

    return oMenor

print(MenorNumero(5,3,65,73,95,85,5551,5,4,9,11199))
