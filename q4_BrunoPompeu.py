import mysql.connector

# CONEXAO COM O BANCO DE DADOS
mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='1234',
    port='3306'
)

crs = mydb.cursor()

execsqlcmd = lambda cmd, crs : crs.execute(cmd)

# FUNCOES DE EXECUCAO DE COMANDOS SQL
execcreatetable = lambda table, attrs, crs : execsqlcmd ("CREATE TABLE IF NOT EXISTS " + table + "(" + attrs + ");\n", crs)
execcreatedatabase = lambda dbname, crs : execsqlcmd ("CREATE DATABASE IF NOT EXISTS " + dbname + ";\n", crs)
execdropdatabase = lambda dbname, crs : execsqlcmd ("DROP DATABASE " + dbname + ";\n", crs)
execdroptable = lambda dbname, crs : execsqlcmd ("DROP TABLE " + dbname + ";\n", crs)
execusedatabase = lambda dbname, crs : execsqlcmd ("USE " + dbname + ";\n", crs)
execselectfromwhere = lambda attrs, table, wherecond, crs : execsqlcmd ("SELECT " + attrs + " FROM " + table + " WHERE " + wherecond + ";\n", crs)
execinsertinto = lambda table, attrs, values, crs : execsqlcmd ("INSERT INTO " + table + "(" + attrs + ") VALUES (" + values + ");\n", crs)
execdeletefromwhere = lambda table, wherecond, crs : execsqlcmd ("DELETE FROM " + table + " WHERE " + wherecond + ";\n", crs)

# CRIANDO E USANDO O BANCO DE DADOS
execcreatedatabase("mydatabase", crs)
execusedatabase("mydatabase", crs)

# CRIACAO DAS TABELAS
execcreatetable("usuarios", "id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), console VARCHAR(255)", crs)
execcreatetable("jogos", "id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), data_lancamento DATE", crs)

# INSERT DOS DADOS #para inserir os dados basta informar os valores
# execinsertinto("usuarios", "nome, console", "\"Bruno\", \"PS4\"", crs)
# execinsertinto("jogos", "nome, data_lancamento", "'The Last of Us', '2013-06-14'", crs)

# REMOÇÃO DOS DADOS  #para deletar os dados basta informar o id
execdeletefromwhere("usuarios", "id = 14", crs)
# execdeletefromwhere("jogos", "id =1", crs)

# CONSULTA DOS DADOS
# execselectfromwhere("*", "usuarios", "true", crs)
# execselectfromwhere("*", "jogos", "true", crs)

res = crs.fetchall()
print_res = lambda res : [print(x) for x in res]
print_res(res)
mydb.commit();
