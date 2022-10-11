from cProfile import label
import matplotlib.pyplot as plt
import seaborn as sns

#Definido os dados

data = [15,25,25,30,5]
labels = ['Grupo_01','Grupo_02','Grupo_03','Grupo_04','Grupo_05']

#Definido a paleta de de cores

#colors = sns.color_palette('pastel')[0:5]

#colors = sns.color_palette("tab10")

colors = sns.color_palette("husl", 8)


#Cria o Gráfico
plt.pie(data,labels = labels, colors = colors, autopct = '%.0f%%')

plt.show()