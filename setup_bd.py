import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('inventario_simples.db')
cursor = conn.cursor()

# Criar a tabela de registros (entrada e saída de ativos)
cursor.execute('''
CREATE TABLE IF NOT EXISTS registros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    acao TEXT NOT NULL,  -- entrada ou saída
    hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Salvar as mudanças e fechar a conexão
conn.commit()
conn.close()

print("Banco de dados criado com sucesso!")
