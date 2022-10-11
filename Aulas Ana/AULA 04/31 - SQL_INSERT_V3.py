from multiprocessing import connection
import sqlite3

# Inicializa a conexão com o banco de dados
conn = sqlite3.connect("db.db")

# Inicializa o cursor onde sera feito as Querys
c = conn.cursor()


#Carrega as informações do usuario
p_Nome = input("Nome: ")
p_Email = input("Email: ")
p_Senha = input("Senha: ")
p_data_nascimento = input("Data de nascimento (dd/mm/yyyy): ")



#EXECUTA O COMANDO SQL
c.execute(""" INSERT INTO usuarios(Nome,Email,Senha,data_nascimento) 
        VALUES(?,?,?,?)""",
(p_Nome, p_Email, p_Senha, p_data_nascimento)
)

# Mostra mensagem para o usuarios
print("Adicionado novos usuarios na tabela 'usuarios'")

# Grava as informações no Banco de Dados
conn.commit()

# Fecha a conexao com o Banco de Dados
conn.close()