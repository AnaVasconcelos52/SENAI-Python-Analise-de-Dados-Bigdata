
from multiprocessing import connection
import sqlite3

# Inicializa a conexão com o banco de dados
conn = sqlite3.connect("db.db")

# Inicializa o cursor onde sera feito as Querys
c = conn.cursor()


#EXECUTA O COMANDO SQL
c.execute("""INSERT INTO usuarios(Nome,Email,Senha,data_nascimento) 
             VALUES('Maria','maria123@gmail.com','123mudar','01/10/1999')
             
""")

c.execute("""INSERT INTO usuarios(Nome,Email,Senha,data_nascimento) 
             VALUES('João','joao23@gmail.com','abcde','12/12/2000')
             
""")

c.execute("""INSERT INTO usuarios(Nome,Email,Senha,data_nascimento) 
             VALUES('Carla','carlacastra@gmail.com','sbc','08/08/1998')
             
""")

# Mostra mensagem para o usuarios
print("Adicionado novos usuarios na tabela 'usuarios'")

# Grava as informações no Banco de Dados
conn.commit()

# Fecha a conexao com o Banco de Dados
conn.close()