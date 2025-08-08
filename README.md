<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=E6F4E9&height=120&section=header"/>

[![Typing SVG](https://readme-typing-svg.herokuapp.com/?color=25434B&size=35&center=true&vCenter=true&width=1000&lines=Welcome+to+ExBookChange+API!;Manage+Books,+Users,+Transactions,+and+Notifications)]()

---

# 📚 ExBookChange API - Backend Django Modular

> A ExBookChange API é uma aplicação backend construída com Django e Django REST Framework (DRF) que oferece uma arquitetura modular, organizada e escalável para o gerenciamento eficiente de livros, usuários, transações financeiras e notificações. Seu design focado em modularidade facilita a manutenção e a expansão conforme o projeto cresce.

---

## 🚀 Estrutura do Projeto

A estrutura do backend segue o padrão Django, mas com organização modular, onde cada funcionalidade fica isolada dentro de apps específicas para facilitar a escalabilidade e reutilização.

```plaintext
backend/
├── apps/                       # Apps Django com funcionalidades específicas
│   ├── books/                  # 📖 Gerenciamento de livros (catálogo, empréstimos, etc)
│   ├── complaints/             # 🛠 Gestão de reclamações e feedbacks
│   ├── notifications/          # 🔔 Sistema de notificações para usuários
│   ├── transactions/           # 💰 Controle de transações financeiras e empréstimos
│   └── users/                  # 👤 Gestão de usuários e autenticação
│
├── core/                       # Configurações globais do Django (settings, urls, deploy)
├── utils/                      # Código utilitário (helpers, validações)
├── manage.py                   # Script para gerenciamento do projeto Django
├── db.sqlite3                  # Banco de dados SQLite local (ideal para desenvolvimento)
├── .env                       # Variáveis de ambiente (configurações sensíveis)
└── README.md                   # Documentação do projeto (este arquivo)
```

---

## 📂 Principais Arquivos por App

Cada app contém arquivos que isolam responsabilidades, facilitando o desenvolvimento e manutenção:

```plaintext
models.py	Define os modelos ORM, ou seja, as tabelas do banco de dados relacionadas ao app
serializers.py	Serializadores do DRF para converter objetos Python para JSON e vice-versa
views.py	Views que implementam a lógica dos endpoints REST (API)
urls.py	Arquivo de rotas (URLs) específicas daquele app, para modularizar a navegação
services.py	Contém lógica de negócio separada para evitar views e models poluídos
__init__.py	Arquivo para marcar o diretório como pacote Python, permitindo importações corretas
```

---

## ⚙️ Configurações Importantes (core/settings.py)
INSTALLED_APPS: Certifique-se de incluir todos os apps criados, como 'apps.books', 'apps.users' etc.

STATIC_URL: URL base para arquivos estáticos, normalmente '/static/'.

ROOT_URLCONF: Aponta para o módulo principal de URLs, geralmente 'core.urls'.

Configurações extras: banco de dados, autenticação, middlewares e variáveis de ambiente são configuradas aqui.

---

## 🗝️ Arquivo .env (exemplo)

Para separar variáveis sensíveis e facilitar a configuração em diferentes ambientes, utilize o arquivo .env:

```plaintext
DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui
DATABASE_URL=sqlite:///db.sqlite3
```

---

## ▶️ Como rodar o servidor localmente

```plaintext
Clone o repositório e entre na pasta do projeto:
▶️ Rode as migrações para criar o banco:
python manage.py migrate

▶️ Inicie o servidor de desenvolvimento:
python manage.py runserver

▶️ Acesse a API no navegador em: http://localhost:8000/ 
```

## 💻 Tecnologias utilizadas
<p> <img height="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" /> <img height="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-plain.svg" alt="Django REST Framework" /> <img height="40"

<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=E6F4E9&height=120&section=footer"/>