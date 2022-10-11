import numpy as np

minha_lista_1 = np.array (([30,60,270],[3,43,7],[1,2,3]))


#calcula a inversa da matriz quadrada
x= np.linalg.inv(minha_lista_1)

print(x)