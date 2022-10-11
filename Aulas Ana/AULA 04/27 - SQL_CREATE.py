
from multiprocessing import connection
import sqlite3

# Inicializa a conexão com o banco de dados
conn = sqlite3.connect("db.db")

# Inicializa o cursor onde sera feito as Querys
c = conn.cursor()


#EXECUTA O COMANDO SQL
c.execute("""CREATE TABLE usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome VARCHAR(50),
    Email VARCHAR(100),
    Senha VARCHAR(50)

)""")

# Mostra mensagem para o usuarios
print("Tabela de usuarios criada com sucesso! ")

# Grava as informações no Banco de Dados
conn.commit()

# Fecha a conexao com o Banco de Dados
conn.close()