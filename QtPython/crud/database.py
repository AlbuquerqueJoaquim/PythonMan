from PyQt5 import  QtSql, QtCore


class DataBase():
    def conectar(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QPSQL')
        self.db.setHostName('127.0.0.1')
        self.db.setDatabaseName('cadastro')
        self.db.setUserName('root')
        self.db.setPassword('JJ*21021990')
        if not self.db.open():
            print("Erro ao conectar ao banco")

    def desconectar(self):
        self.db.close()
        QtSql.QSqlDatabase.removeDatabase('QPLSQ')

#listando as informação na grid

    def listarClientes(self):
        model = QtSql.QSqlQueryModel()
        model.setQuery('select idclientes, nome,telefone,celular, endereco from clientes'
                       'order by nome')
        model.setHeaderData(0, QtCore.Qt.Horizontal, "Código")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Nome")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Telefone")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "Celular")
        model.setHeaderData(4, QtCore.Qt.Horizontal, "Endereco")
        return model


#inserindo informações no banco
    def inserirClliente(self, cliente):
        query = QtSql.QSqlQuery()
        query.exec_(f"insert into clientes (nome, telefone, celular, endereco) values ('{cliente['nome']}','{cliente['nome']}','{cliente['telefone']}','{cliente['celular']}','{cliente['endereco']}')")


    def alterarCliente(self):
        query = QtSql.QSqlQuery()
        query.exec_("update clientes set nome='{cliente['nome']}','{cliente['telefone']}','{cliente['celular']}','{cliente['endereco']}' where idclientes={cliente['idclientes']}")


    def listarFornecedor(self):
        model = QtSql.QSqlQueryModel()
        model.setQuery('select idfornecedores, nome,telefone,celular, endereco from fornecedores'
                       'order by nome')
        model.setHeaderData(0, QtCore.Qt.Horizontal, "Código")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Nome")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Telefone")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "Celular")
        model.setHeaderData(4, QtCore.Qt.Horizontal, "Endereco")
        return model

    def inserirFornecedor(self):
        query = QtSql.QSqlQuery()
        query.exec_(f"insert into fornecedores (nome, telefone, celular, endereco) values('{fornecedor['nome']}', '{fornecedor['telefone']}', '{fornecedor['celular']}', '{fornecedor['endereco']}')")


    def alterarFornecedor(self):
        query = QtSql.QSqlQuery()
        query.exec_(f"update fornecedores set nome='{fornecedor['nome']}', telefone='{fornecedor['telefone']}', celular='{fornecedor['celular']}', endereco='{fornecedor['endereco']}' where idfornecedores={fornecedor['idfornecedores']}")