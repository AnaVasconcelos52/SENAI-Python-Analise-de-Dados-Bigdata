from multiprocessing import connection
import sqlite3

# Inicializa a conexão com o banco de dados
conn = sqlite3.connect("db.db")

# Inicializa o cursor onde sera feito as Querys
c = conn.cursor()


#Carrega as informações do usuario
id_usuario = 1
p_Nome = "luiza"
p_Email = "luiza@gmail.com"
p_Senha = "Senha124"
p_data_nascimento = "15/04/2005"



#EXECUTA O COMANDO SQL
c.execute(""" UPDATE usuarios SET Nome=?, Email=?, Senha=?, data_nascimento=? WHERE id=?""",
(p_Nome, p_Email, p_Senha, p_data_nascimento,id_usuario)
)

# Mostra mensagem para o usuarios
print(f"Adicionado usuario: {id_usuario}'")

# Grava as informações no Banco de Dados
conn.commit()

# Fecha a conexao com o Banco de Dados
conn.close()