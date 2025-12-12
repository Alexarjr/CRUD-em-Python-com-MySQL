#CRUD em Python com MySQL

Um CRUD simples em Python conectado ao banco de dados MySQL, contendo
operações de:

-   Criar usuários
-   Listar usuários
-   Atualizar usuários
-   Excluir usuários

🚀 Tecnologias usadas

-   Python 3
-   MySQL
-   mysql-connector-python

📁 Estrutura do projeto

CRUD Python/
│ 
├── config.py # Credenciais do banco (não enviar ao GitHub) 
├── crud.py # Código do CRUD 
├── README.md 
├── .gitignore 
└── requirements.txt

⚙️ Como configurar

1.  Instale as dependências:

    pip install -r requirements.txt

2.  Crie um arquivo config.py:

    HOST = "seu_host"
    USER = "seu_usuario"
    PASSWORD = "sua_senha"
    DATABASE = "seu_banco"

3.  Execute o arquivo principal:

    python CRUD.py
