<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=E6F4E9&height=120&section=header"/>

<div align="center">

# 📚 **ExBookChange API**

### Uma plataforma para troca e doação de livros entre estudantes

[![Typing SVG](https://readme-typing-svg.herokuapp.com/?color=25434B\&size=30\&center=true\&vCenter=true\&width=1000\&lines=Bem-vindo+à+ExBookChange+API!;Organize+Trocas+e+Doações+de+Livros;Gerencie+Usuários,+Livros+e+Transações)]()

</div>

---

# 📘 **Sobre o Projeto**

O **ExBookChange** é um sistema que facilita a **troca** e **doação** de livros entre estudantes, semelhante ao funcionamento da OLX:
📖 Você enjoou de um livro → anuncia → troca ou doa para outro estudante.

O projeto incentiva a **leitura**, promove **interação social** e cria um ecossistema simples para conectar pessoas com interesses literários.

O backend foi construído usando:

* **Django**
* **Django REST Framework**
* **MySQL / phpMyAdmin**
* **JWT para autenticação**
* Arquitetura modular baseada em **Models + Serializers + Views + Services**

---

# 🏗 **Arquitetura Geral**

A estrutura foi organizada para permitir fácil manutenção, escalabilidade e clareza no fluxo da API:

```
backend/
├── apps/
│   ├── books/          # 📚 Gestão de Anúncios de livros (troca/doação)
│   ├── users/          # 👤 Cadastro, login, autenticação
│   └── transactions/   # 🔄 Trocas e doações realizadas
│
├── core/               # Configurações globais (settings, urls)
├── utils/              # Funções auxiliares
├── manage.py
└── README.md
```

Cada app possui:

* `models.py` – Estrutura das tabelas
* `serializers.py` – Conversão Python <-> JSON
* `views.py` – Lógica das rotas
* `urls.py` – Rotas de cada módulo
* `services.py` – Regras de negócio

---

# 🛠 **Tecnologias Utilizadas**

<div style="display:flex; gap:20px;">
<img height="50" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"/>
<img height="50" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-plain.svg"/>
<img height="50" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original.svg"/>
</div>

* **Python 3.12**
* **Django 5+**
* **Django REST Framework**
* **MySQL**
* **JWT Authentication**
* **Arquitetura limpa baseada em Services**

---

# ▶️ **Como Rodar o Projeto**

### **1. Clone o repositório**

```
git clone https://github.com/seuusuario/exbookchange.git
cd exbookchange
```

### **2. Instale as dependências**

```
pip install -r requirements.txt
```

### **3. Configure o arquivo `.env`**

Exemplo:

```
DEBUG=True
SECRET_KEY=suachavesecreta
DATABASE_NAME=exbookchange
DATABASE_USER=root
DATABASE_PASSWORD=1234
DATABASE_HOST=localhost
DATABASE_PORT=3306
JWT_SECRET=segredoJWT
```

### **4. Execute as migrações**

```
python manage.py migrate
```

### **5. Rode o servidor**

```
python manage.py runserver
```

---

# 📌 **Principais Recursos da API**

✔ Cadastro e login de usuários
✔ Gerenciamento de livros
✔ Criação de anúncios de troca/doação
✔ Sistema de transações (conclusão de troca/doação)
✔ Retorno em JSON
✔ Segurança com JWT
✔ Estrutura modular escalável

---

# 📡 **Endpoints Principais**

> **A documentação completa está no arquivo `API.md`.**

* `/users/` → Criar, listar, editar e deletar usuários
* `/books/` → Criar, listar, editar e deletar Anúncios de livros
* `/transactions/` → Registrar trocas e doações

---

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=E6F4E9&height=140&section=footer"/>


</div>
