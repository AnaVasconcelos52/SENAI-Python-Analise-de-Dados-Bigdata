def soma(*args):
    resultado = 0

    for x in args:
        resultado+= x
        # mesma coisa que isso: resultado = resultado + x

    print(resultado)

soma(1,5,6,2,4)
soma(1,3)

