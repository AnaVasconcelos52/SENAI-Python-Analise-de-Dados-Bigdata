from multiprocessing import connection
import sqlite3

# Inicializa a conexão com o banco de dados
conn = sqlite3.connect("db.db")

# Inicializa o cursor onde sera feito as Querys
c = conn.cursor()


#EXECUTA O COMANDO SQL
c.execute("""SELECT * FROM usuarios"""
)

# Mostra mensagem para o usuarios
for linha in c.fetchall():
    print(linha)

# Grava as informações no Banco de Dados
conn.commit()

# Fecha a conexao com o Banco de Dados
conn.close()