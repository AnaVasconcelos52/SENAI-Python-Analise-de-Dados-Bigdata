
/*CREATE - Criar tabela de usuarios*/
CREATE TABLE usuarios (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome VARCHAR(50),
email VARCHAR(100),
senha VARCHAR(50)
);

/*ALTER - Altera a tabela de usuarios, adicionando a coluna data_nascimento*/
ALTER TABLE usuarios ADD data_nascimento VARCHAR(10);

/*INSERT - Insere um usuario na tabela*/
INSERT INTO usuarios(nome, email, senha, data_nascimento) VALUES ('Joao','joao_e_maria@gmail.com','Maria123','21/05/2001');
INSERT INTO usuarios(nome, email, senha, data_nascimento) VALUES ('Maria','maria_e_joao@gmail.com','Joao123','21/05/2001');
INSERT INTO usuarios(nome, email, senha, data_nascimento) VALUES ('Ana','aninha@gmail.com','Joao123','21/05/2001');

/*UPDATE - Altualizar um registro da tabela */ 
UPDATE usuarios SET senha="Ana123" WHERE nome="Joao"

/*DELETE - Deleta um usuario da tabela */ 
DELETE FROM usuarios WHERE email="joao_e_maria@gmail.com"

/*SELECT - Seleciona os registros da tabela*/ 
SELECT * FROM usuarios 
SELECT * FROM usuarios WHERE nome="Ana"
SELECT nome FROM usuarios WHERE senha="Joao123"
SELECT * FROM usuarios WHERE senha="Joao123" ORDER BY nome DESC

/*GRANT - Habilita as permissoes de utilizar os comando para o usuario "usuario_db_01" */ 
GRANT SELECT, INSERT, UPDATE ON usuarios TO usuario_db_01

/*REVOKE - Desabilita os comandos para o usuario "usuario_db_01" */ 
REVOKE SELECT ON usuarios FROM usuario_db_01

/*DENY - Nega todoas as permissõs para o usuario "usuario_db_01*/ 
DENY SELECT ON usuarios TO usuario_db_01

/*DROP - Exclui a tabela usuario/exclui o banco de dados */ 
DROP TABLE usuarios
DROP DATABASE db
