# Gestão de usuários

Esse projeto é o back-end do repositório **/react-good-practices**, ele proporciona os dados do usuário para o react usar e tem algumas rotas para testar o login de usuário.

## Principais tecnologias

- python==3.13.1
- Flask==3.1.0

As demais bibliotecas e suas versão estão no arquivo requirements.txt. Após instalar os requirimentos, como o projeto usa flask-migrate, você pode usar o comando **flask db init** seguido de **flask db upgrade**
para criar o banco de dados do projeto.

## Funcionamento do projeto

Estou usando o flask com as blueprints para separar as rotas, o arquivo run.py serve apenas para iniciar o servidor, o arquivo __init__.py dentro da pasta project é onde fica as configurações do flask.
Para o login, temos a pasta auth que armazena as configurações do login-manager, a view e o templante. Temos mais a pasta home e users seguindo a mesma estrutura para armazenar as rotas, templates, etc...

Quanto ao banco de dados, estou usando uma pasta storage dentro de database para armazenar os arquivos sql.py e sql.sql onde o arquivo .sql armazena apenas os comandos sql e o arquivo sql.py conecta com
banco e executa os comandos do arquivo .sql.
