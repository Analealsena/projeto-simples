Controle de Entrada e Saída de Ativos
Este projeto é um sistema simples de controle de entrada e saída de ativos, como notebooks e outros equipamentos, desenvolvido usando Python com o Flask para o backend e SQLite como banco de dados. Ele permite registrar quando um ativo é retirado ou devolvido e exibir o histórico de movimentação.

Funcionalidades
Registro de entrada e saída de ativos: Permite registrar a retirada ou devolução de ativos pela equipe.
Listagem de ativos e histórico de movimentação: Exibe uma tabela com todos os ativos registrados e suas movimentações.
Banco de dados SQLite: Utilizado para armazenar as informações de ativos e registros de movimentação.
Interface Web: Simples, com formulários para registrar ações e uma tabela para exibir os dados.

Tecnologias Utilizadas

Python 3: Linguagem de programação principal do projeto.

Flask: Framework web leve para criar o backend.

SQLite: Banco de dados relacional usado para armazenar as informações.

HTML5, CSS3: Para construir a interface web.

VSCode: Editor de código recomendado para desenvolvimento.

Requisitos
Python 3.x
Flask
SQLite3

#Como Usar#

Acesse a interface web no navegador.
Utilize o formulário na página para registrar a entrada ou saída de um ativo.
Após o registro, os ativos e suas movimentações aparecerão na tabela abaixo do formulário.
Para adicionar novos ativos, utilize a funcionalidade de cadastro no formulário.

#Estrutura do Projeto#

/projeto-simples
    ├── app.py                 # Arquivo principal do servidor Flask
    ├── setup_db.py            # Script para criar o banco de dados SQLite
    ├── reset_db.py            # Script para resetar o banco de dados (se necessário)
    ├── inventario_simples.db   # Arquivo do banco de dados SQLite (criado após execução)
    ├── /templates/            # Pasta para os arquivos HTML
    │     └── index.html        # Página principal do sistema
    ├── /static/               # Pasta para arquivos estáticos (CSS)
    │     └── style.css         # Estilos personalizados da interface
    └── README.md              # Este arquivo de documentação
