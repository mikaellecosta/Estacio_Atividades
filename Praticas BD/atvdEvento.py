import sqlite3

def conectarBD(bd):
    conexao = sqlite3.connect(bd)
    return conexao

def criarTab(conexao):
    cursor = conexao.cursor()

    cursor.execute( '''CREATE TABLE IF NOT EXISTS Local (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        endereco TEXT NOT NULL
                    );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Participante (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT NOT NULL,
                        evento_id INTEGER NOT NULL,
                        FOREIGN KEY (evento_id) REFERENCES Evento(id) 
                   );''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Evento (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        data DATE NOT NULL,
                        local TEXT NOT NULL,
                        participantes TEXT NOT NULL,
                        FOREIGN KEY (local) REFERENCES Local(nome),
                        FOREIGN KEY (participantes) REFERENCES Participantes(nome) 
                   );''')
    
    conexao.commit()

if __name__ == '__main__':
    conexao = conectarBD('bd_Eventos.db')
    criarTab(conexao)
    conexao.close