from multiprocessing import connection
import sqlite3

# Inicializa a conexão com o banco de dados
conn = sqlite3.connect("db.db")

# Inicializa o cursor onde sera feito as Querys
c = conn.cursor()


#Lista com os dados dos novos usuários

lista = [
        ('Felipe','felipe123@gmail.com','senha123','30/04/2001'),
        ('Adriana','adrianacosta3@gmail.com','harrypotter','31/08/2001'),
        ('Pedro','pedropedicru@gmail.com','avada','28/05/2000'),

]

#EXECUTA O COMANDO SQL
c.executemany(""" INSERT INTO usuarios(Nome,Email,Senha,data_nascimento) VALUES(?,?,?,?)
""",lista)

# Mostra mensagem para o usuarios
print("Adicionado novos usuarios na tabela 'usuarios'")

# Grava as informações no Banco de Dados
conn.commit()

# Fecha a conexao com o Banco de Dados
conn.close()