# Cartão de Identidade Acadêmica

Backend em Django para o cadastro de "cartões de identidade acadêmica" dos alunos: um perfil simples com **Nome**, **Curso** e **Bio**, exibido em formato de cartão.

## Tecnologias

- Python 3.11+
- Django 5.2
- SQLite (banco padrão de desenvolvimento)
- python-decouple (configuração via `.env`)

## Instalação e execução

```bash
# 1. Clonar o repositório
git clone https://github.com/ljborgess/crud-facul-django.git
cd crud-facul-django

# 2. Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Criar o arquivo de variáveis de ambiente (e gerar uma SECRET_KEY nova)
copy .env.example .env       # Windows
# cp .env.example .env       # Linux/Mac
python -c "from django.core.management.utils import get_random_secret_key as g; print(g())"
# cole o valor gerado em SECRET_KEY dentro do .env

# 5. Aplicar as migrações do banco de dados
python manage.py migrate

# 6. (Opcional) Criar um superusuário para acessar o admin
python manage.py createsuperuser

# 7. Rodar o servidor de desenvolvimento
python manage.py runserver
```

O projeto ficará disponível em **http://127.0.0.1:8000/**.

## Endpoints disponíveis

| Método | URL              | Descrição                              |
|--------|------------------|-----------------------------------------|
| GET    | `/`              | Lista todos os cartões de aluno         |
| GET    | `/novo/`         | Formulário para criar um novo cartão    |
| POST   | `/novo/`         | Cria um novo aluno                      |
| GET    | `/<id>/editar/`  | Formulário para editar um cartão        |
| POST   | `/<id>/editar/`  | Atualiza os dados do aluno              |
| GET    | `/<id>/excluir/` | Página de confirmação de exclusão       |
| POST   | `/<id>/excluir/` | Exclui o aluno                          |
| GET    | `/admin/`        | Django Admin (gerenciamento dos alunos) |

## Modelo de dados

**Aluno**
- `nome` — CharField, obrigatório
- `curso` — CharField, obrigatório
- `bio` — TextField, obrigatório, limite de 280 caracteres

## Demonstração

<!-- Adicione aqui prints ou um GIF mostrando o cadastro, edição e exclusão de um cartão -->
