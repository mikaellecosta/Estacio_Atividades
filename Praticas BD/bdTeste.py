import sqlite3
try:
    conexao = sqlite3.connect('bdlite.db')
    cursor = conexao.cursor()

    tablePessoa = '''CREATE TABLE Pessoa (
                     cpf INTEGER NOT NULL,
                     nome TEXT NOT NULL,
                     nascimento DATE NOT NULL,
                     oculos BOOLEAN NOT NULL,
                     PRIMARY KEY (cpf)
                     )'''
    tableMarca = '''CREATE TABLE Marca (
                  id INTEGER NOT NULL,
                  nome TEXT NOT NULL,
                  sigla CHARACTER(2) NOT NULL,
                  PRIMARY KEY (id)
                  )'''
    tableVeiculo = '''CREATE TABLE Veiculo (
                    placa CHARACTER (7) NOT NULL,
                    marca TEXT NOT NULL,
                    cor TEXT NOT NULL,
                    ano TEXT NOT NULL,
                    proprietario INTEGER NOT NULL,
                    PRIMARY KEY (placa),
                    FOREIGN KEY (proprietario) REFERENCES Pessoa(cpf),
                    FOREIGN KEY (marca) REFERENCES Marca(nome)
                    )'''

    comando = ''' ALTER TABLE Veiculo
    ADD motor REAL;
    '''

    cursor.execute(comando) 
    conexao.commit()

except conexao.DatabaseError as err:
    print("Erro de banco de dados", err)
    
finally:   
     # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()
