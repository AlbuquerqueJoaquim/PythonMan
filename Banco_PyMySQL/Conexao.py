#importando o package pymysql para realizar a conexao com o banco de dados mysql

import  pymysql.cursors



conexao = pymysql.connect (

    host='localhost',
    user='admin',
    password='Jojo*21021990',
    db='DBI',
    cursorclass = pymysql.cursors.DictCursor

)

#cursor = conexao.cursor()
#criando uma tabela e suas colunas
#cursor.execute('create table pessoa(nome varchar(30), idade int, endereco varchar(100));')
#cursor.close()
#conexao.close()

#trabalhando de forma elegante

x = 'create table cidade(idcidade int,nome varchar(20));'

with conexao.cursor() as cursor:
    cursor.execute(x)

print('saiu do with')