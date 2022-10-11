
# funcao input recebe um dado do usuario
nota1 = int(input("Qual o valor da nota 1? "))

nota2 = int(input("Qual o valor da nota 2? "))

nota3 = int(input("Qual o valor da nota 3? "))

nota4 = int(input("Qual o valor da nota 4? "))

lista_de_dados = [nota1,nota2,nota3,nota4]



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

if media(lista_de_dados) >= 7:
    print("APROVADO")
    
elif media(lista_de_dados) < 5:
    print("REPROVADO")


elif media(lista_de_dados) >= 5:
    print("RECUPERAÇÃO")


