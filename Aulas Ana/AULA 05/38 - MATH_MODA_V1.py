
from ast import If
from itertools import count



lista_de_dados  = [35, 37, 36, 34, 38, 35, 37, 37, 33, 36, 38, 37, 35, 36, 33, 31, 39, 37, 38, 33, 32, 33, 34, 35, 36, 37, 39, 38, 35, 36, 31, 30, 31, 32, 32, 33, 35, 37, 36]

def EncontrarAmostragem(lista):
    amostragem = []

    for a in lista:
        if(a not in amostragem):
            amostragem.append(a)

    return amostragem

def ContarNumeroDeVezesQueAparece(lista):

    lista_de_contagem = []

    for n in lista:
        lista_de_contagem.append(0)


    count = 0

    for o in lista: 
        for n in lista_de_dados:
            if(o == n):
                lista_de_contagem[count] +=1

        count +=1

    return lista_de_contagem

def EncontraModa (lista1,lista2):
    valorInicial = lista2[0]
    indicoModa = 0
    count = 0

    for n in lista2:
        if(valorInicial <= n):
            valorInicial = n
            indicoModa = count


        count +=1

    return lista1[indicoModa]

lista_de_amostras = EncontrarAmostragem(lista_de_dados)

print(f"Lista de amostras -> {lista_de_amostras}")

lista_com_contagens = ContarNumeroDeVezesQueAparece(lista_de_amostras)

print(f"Lista de contagens -> {lista_com_contagens}")

moda = EncontraModa(lista_de_amostras, lista_com_contagens)

print(f"Moda -> {moda}")

