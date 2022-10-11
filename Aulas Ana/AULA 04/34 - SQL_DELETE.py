from multiprocessing import connection
import sqlite3

# Inicializa a conexão com o banco de dados
conn = sqlite3.connect("db.db")

# Inicializa o cursor onde sera feito as Querys
c = conn.cursor()


#Carrega as informações do usuario
id_usuario = "1"


#EXECUTA O COMANDO SQL
c.execute(""" DELETE FROM usuarios WHERE id=?""",
(id_usuario)
)

# Mostra mensagem para o usuarios
print(f"USUARIO DELETADO: {id_usuario}'")

# Grava as informações no Banco de Dados
conn.commit()

# Fecha a conexao com o Banco de Dados
conn.close()