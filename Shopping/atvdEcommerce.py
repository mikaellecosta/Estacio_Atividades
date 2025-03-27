import sqlite3

def criarConexao(bd):
    conexao = sqlite3.connect(bd)
    return conexao

def criarTabelas(conexao):
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE Produto (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        preco REAL NOT NULL
                            );''')
    
    cursor.execute('''CREATE TABLE Comercio (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        cidade TEXT NOT NULL                
                        );''')
    
    cursor.execute('''CREATE TABLE Compra (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        data_compra DATE NOT NULL,
                        total REAL NOT NULL
                        );''')
    
    cursor.execute('''CREATE TABLE Itens_compra (
                        id_item INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_compra INTEGER NOT NULL,
                        nome_produto TEXT NOT NULL,
                        preco_und REAL NOT NULL,
                        subtotal REAL NOT NULL,
                        FOREIGN KEY(id_compra) REFERENCES Compra(id)
                   );''')
    
    conexao.commit()

def InsertProduto(conexao):
    cursor = conexao.cursor()
    

if __name__ == '__main__':
    conexao = criarConexao('bdEcommerce.db')
    # criarTabelas(conexao)
    conexao.close()
