lista_de_dados = [28,32,85,97,41,57,98,82,65,88]

#Função que retorna o valor da media
def media(lista):


    #Inicializando as variaveis
    total_das_somatoria = 0
    n_de_dados = 0


    #Faz a somatoria e conta o numero de dados
    for n in lista:
        total_das_somatoria += n
        n_de_dados += 1

    #Retorna a somatoria dividida pelo numero de dados
    return total_das_somatoria/n_de_dados


# Mostra em tela o resultado
print(media(lista_de_dados))
