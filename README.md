# todolist_server
Servidor e API para o projeto de ToDo List


## Requisito

- Python 3.6+


## Preparação de ambiente virtual

A partir da pasta do projeto, execute:
```
python -m venv venv
source venv/bin/activate
```

### Instalação de dependências
```
pip install -r requirements.txt
```

### Migração do banco de dados

```
./manage.py migrate
```

### Criação de super usuário

```
./manage.py createsuperuser
```

### Inicialização do servidor em modo de desenvolvimento

```
./manage.py runserver
```
