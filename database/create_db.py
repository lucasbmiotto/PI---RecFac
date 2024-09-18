import sqlite3

def create_database():
    conn = sqlite3.connect('login.db')
    cursor = conn.cursor()
    
    # Cria a tabela de usuários
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    
    # Adiciona um usuário de exemplo (não adicione isso em produção!)
    cursor.execute('''
    INSERT OR IGNORE INTO users (username, password)
    VALUES (?, ?)
    ''', ('admin', 'password'))
    
    conn.commit()
    conn.close()

create_database()
