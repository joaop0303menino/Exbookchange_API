# 📚 ExBookChange API - Backend Django Modular

> Bem-vindo ao backend da ExBookChange — uma API REST para gerenciamento de livros, usuários, transações e notificações, construída com Django e Django REST Framework (DRF) em uma arquitetura modular, organizada e escalável.

---

## 🚀 Estrutura do Projeto

```plaintext
backend/
├── apps/                       # Apps Django que implementam funcionalidades específicas
│   ├── books/                  # 📖 Gerenciamento de livros (catálogo, empréstimos, etc)
│   ├── complaints/             # 🛠 Gestão de reclamações e feedbacks
│   ├── notifications/          # 🔔 Sistema de notificações para usuários
│   ├── transactions/           # 💰 Controle de transações financeiras e empréstimos
│   └── users/                  # 👤 Gestão de usuários e autenticação
│
├── core/                       # Configurações globais do Django (settings, urls, deploy)
├── utils/                      # Código utilitário (helpers, validações)
├── manage.py                   # Script para gerenciamento do Django
├── db.sqlite3                  # Banco de dados SQLite local (para desenvolvimento)
├── .env                       # Variáveis de ambiente (configurações sensíveis)
└── README.md                   # Documentação do projeto


📂 Principais Arquivos por App
models.py	Define os modelos ORM (tabelas do banco de dados)
serializers.py	Serializadores DRF para converter dados entre JSON e Models
views.py	Views da API (REST endpoints)
urls.py	Rotas específicas do app
services.py	Lógica de negócio separada para manter o código organizado
__init__.py	Marca a pasta como módulo Python


⚙️ Configurações Importantes (core/settings.py)
INSTALLED_APPS: Registre todos os apps do projeto (ex: 'apps.books', 'apps.users').
STATIC_URL: Define a URL base para arquivos estáticos (ex: /static/).
ROOT_URLCONF: Aponta para o módulo raiz de rotas (ex: 'core.urls').


🛠️ Arquivo .env (exemplo)
DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui
DATABASE_URL=sqlite:///db.sqlite3

▶️ Como rodar o servidor localmente
Clone o repositório e entre na pasta do projeto:

▶️ Rode as migrações para criar o banco:
python manage.py migrate

▶️ Inicie o servidor de desenvolvimento:
python manage.py runserver

▶️ Acesse a API no navegador em: http://localhost:8000/