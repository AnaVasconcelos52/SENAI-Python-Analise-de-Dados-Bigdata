n1 = float(input("Qual o valor da prova 1? R:"))
n2 = float(input("Qual o valor da prova 2? R:"))
n3 = float(input("Qual o valor da prova 3? R:"))

p1 = float(input("Qual o peso da prova 1? R:"))
p2 = float(input("Qual o peso da prova 2? R:"))
p3 = float(input("Qual o peso da prova 3? R:"))


media_ponderada = ((n1*p1)+(n2+p2)+(n3*p3))/(p1+p2+p3)

print(f"A média ponderada é: {media_ponderada}")