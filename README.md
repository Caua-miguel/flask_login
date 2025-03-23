# Gestão de usuários

Esse projeto é o back-end do repositório **/react-good-practices**, ele proporciona os dados do usuário para o react usar e tem algumas rotas para testar o login de usuário.

## Principais tecnologias

- python==3.13.1
- Flask==3.1.0

As demais bibliotecas e suas versão estão no arquivo requirements.txt. Após instalar os requirimentos, como o projeto usa flask-migrate, você pode usar o comando **flask db init** seguido de **flask db upgrade**
para criar o banco de dados do projeto.

## Funcionamento do projeto

Para rodar o projeto você precisa criar sua pasta .env para armazenar a chave secreta do flask e seguir os seguintes passos:

Instalação dos requisitos

`pip install -r requirements.txt`

Iniciar e ajustar o banco de dados sqlite, seguindo a própria documentação do flask-migrate

```
flask db init

flask db migrate

flask db upgrade
```
Em seguida, basta executar o arquivo app.py

`python app.py`


