import statistics

lista_de_dados  = [35, 37, 36, 34, 38, 35, 37, 37, 33, 36, 38, 37, 35, 36, 33, 31, 39, 37, 38, 33, 32, 33, 34, 35, 36, 37, 39, 38, 35, 36, 31, 30, 31, 32, 32, 33, 35, 37, 36]

moda = statistics.mode(lista_de_dados)

print(f"Moda -> {moda}")