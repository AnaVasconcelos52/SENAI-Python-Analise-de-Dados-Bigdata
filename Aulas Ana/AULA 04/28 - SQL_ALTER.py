
from multiprocessing import connection
import sqlite3

# Inicializa a conexão com o banco de dados
conn = sqlite3.connect("db.db")

# Inicializa o cursor onde sera feito as Querys
c = conn.cursor()


#EXECUTA O COMANDO SQL
c.execute("""ALTER TABLE usuarios ADD data_nascimento VARCHAR(10)""")

# Mostra mensagem para o usuarios
print("Adicionado nova coluna 'data_nascimento' dentro da tabela de usuarios ")

# Grava as informações no Banco de Dados
conn.commit()

# Fecha a conexao com o Banco de Dados
conn.close()
