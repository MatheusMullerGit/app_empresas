## 📚  Descrição 

API_REST com Django e Rest Framework para acesso à organizações e seus funcionários.
Esta API está disponível em https://app-empresas-heroku.herokuapp.com/

<img src="https://user-images.githubusercontent.com/64918635/95005136-88b49200-05ca-11eb-8a97-00b6057bcff8.png">

Para acessar basta utilizar os dados de login abaixo:
```
Usuário: usuario1
Senha: userpassword
```

## 📌Endpoints:

### [GET] /users

Retorna os usuários cadastrados no sistema conforme JSON abaixo:
```
  {
    "url": "https://app-empresas-heroku.herokuapp.com/users/5/",
    "username": "usuario5",
    "email": "",
    "groups": []
  }, ...
```

### [GET]/api/empresas

Retorna as empresas cadastradas no sistema conforme JSON abaixo:
```
  {
    "id": 1,
    "nome": "Empresa 01",
    "funcionario_set": [
      {
        "id": 1,
        "nome": "Funcionario 01",
        "departamentos": [
          1
        ],
        "empresa": 1,
        "user": 1
      }
    ]
  }, ...
```

### [GET]/api/funcionarios

Retorna os funcionarios cadastrados no sistema conforme JSON abaixo:
```
  {
    "id": 1,
    "nome": "Funcionario 01",
    "departamentos": [
      1
    ],
    "empresa": 1,
    "user": 1
  }, ...
```

### [GET]/api/departamentos

Retorna os departamentos cadastrados no sistema conforme JSON abaixo:
```
  {
    "nome": "RH-Empresa01",
    "empresa": 1,
    "funcionario_set": [
      {
        "id": 1,
        "nome": "Funcionario 01",
        "departamentos": [
          1
        ],
        "empresa": 1,
        "user": 1
      }
    ]
  }, ...
```

## 🚀 Tecnologias Usadas 

<img src="https://user-images.githubusercontent.com/18649504/66262823-725cd600-e7be-11e9-9cea-ea14305079db.png" width = "150">

<img src="https://user-images.githubusercontent.com/64918635/95004956-a84abb00-05c8-11eb-986f-bae23f1900e2.png" width = "150">

<img src="https://user-images.githubusercontent.com/64918635/95004978-d3cda580-05c8-11eb-86cb-c1546571054f.png" width = "150">

<img src="https://user-images.githubusercontent.com/64918635/95004996-1db68b80-05c9-11eb-8703-b42642372bd5.png" width = "150">

<img src="https://user-images.githubusercontent.com/64918635/95005030-7ab24180-05c9-11eb-8d99-93240ff27171.png" width = "150">

## 📢 Como executar

Requisitos:

Python 3.8.0<br>

Instalar todas as dependências do python usando o arquivo requirements.txt que está no projeto:  

```bash 
pip install  -r requirements.txt
 ```  
 Executar o manage.py runserver no cmd com o comando:

```bash 
python manage.py runserver
 ```  
Importar o arquivo collection.JSON utilizando um programa de requisições REST, como o <a href="https://insomnia.rest/download/">Insomnia</a> ou o <a href="https://www.postman.com/downloads/">Postman<a> e informar o IP: http://127.0.0.1:8000/+Endpoint , selecionando o Endpoint desejado.

Para visualizar o código em funcionamento, basta acessar diretamente a API em https://app-empresas-heroku.herokuapp.com/+Endpoint

## 🔓 Licença 
MIT © [Matheus Muller](https://www.linkedin.com/in/matheus-herrera-bezerra-muller/)
