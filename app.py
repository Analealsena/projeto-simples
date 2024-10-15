from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def connect_db():
    return sqlite3.connect('inventario_simples.db')

# Página inicial: exibe os registros
@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Consulta todos os registros
    cursor.execute("SELECT * FROM registros")
    registros = cursor.fetchall()
    
    conn.close()
    return render_template('index.html', registros=registros)

# Rota para registrar entrada ou saída
@app.route('/registrar', methods=['POST'])
def registrar():
    nome = request.form['nome']
    acao = request.form['acao']
    
    conn = connect_db()
    cursor = conn.cursor()
    
    # Inserir o registro no banco de dados
    cursor.execute("INSERT INTO registros (nome, acao) VALUES (?, ?)", (nome, acao))
    
    conn.commit()
    conn.close()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
    
