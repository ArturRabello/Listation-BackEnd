# Listation API

![GitHub Repo Size](https://img.shields.io/github/repo-size/ArturRabello/Listation-BackEnd?style=for-the-badge)

![GitHub](https://img.shields.io/github/license/ArturRabello/Listation-BackEnd?style=for-the-badge)

![GitHub last commit](https://img.shields.io/github/last-commit/ArturRabello/Listation-BackEnd?style=for-the-badge)

![GitHub contributors](https://img.shields.io/github/contributors/ArturRabello/Listation-BackEnd?style=for-the-badge)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) ![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)

O Listation API é um serviço de API restful, deselvolvido para se comunicar com o front-end da aplicação Listation.O Listation é uma aplicação projetada para auxiliar pessoas na organização de atividades, tarefas e ideias de forma simples e fácil.

Ele realiza funções de CRUD (Create, Read, Update, Delete) em um banco de dados relacional.

**Link do Front-End:** [Listation](https://github.com/ArturRabello/Listation-FrontEnd)

# Propósito

Este projeto foi desenvolvido como parte do programa de **Pós-Graduação em Desenvolvimento Full Stack da PUC Rio**, tendo como objetivo principal a consolidação prática de conceitos teóricos estudados durante o curso.

O desenvolvimento dessa aplicação, me permitiu aprimorar as minhas habilidades no desenvolvimento do  back-end.

## 🚀 Tecnologias
* Python
* SQLite
* Flask
* SQLAlchemy

## 🛠️ Como utilizar 
- **Clone o repositório:**
```bash
git clone https://github.com/ArturRabello/Listation-BackEnd.git
```

- **Instale as dependências**:
```bash
(env)$ pip install -r requirements.txt
```

- **Execute a API atráves do flask:**
```bash
flask run --host 0.0.0.0 --port 5000
```
- **Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte. :**
```bash
flask run --host 0.0.0.0 --port 5000 --reload
```
## 🔍 funcionalidades

**Side Menu Cards**

* **Criar um novo card** - POST /side_menu_card/create.
* **Listar todos os cards** - GET /side_menu_card/list.
* **Deletar um card** - DELETE /side_menu_card/delete.

**Modals**
* **Criar um novo modal** - POST /modal/create.
* **Listar todos os modais** - GET /modal/list.
* **Deletar um modal** - DELETE /modal/delete.

**Modal Cards**
* **Criar um novo modal card** - POST /modal_card/create.
* **Listar todos os modal cards** - GET /modal_card/list.
* **Deletar um modal card** - DELETE /modal_card/delete.
* **Pegar um modal card** - GET /modal_card/get.
* **Editar um modal card** - PUT /modal_card/edit.

## 📂 Estrutura 

```bash
📦 Listation - Back-end
├── 📂 model/  → Modelos de dados
├── 📂 schemas/ → Esquemas de validação
├── 📜requirements.txt → dependencias
├── ⚙️app.py → Arquivo principal
└── 📌README.md → documentação geral
```

## Documentação da API

#### Criar um card no menu lateral

```bash
POST /side_menu_card/create
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id`| `string` | **Obrigatório**. Id card |
| `name`| `string` | Nome do card |
| `description`| `string` | Descrição do card |

**Respostas:**
| Código | Descrição | Resposta |
| :-------- | :------- | :------- |
| 200 | OK | Retorna o card criado |
| 404 | Conflit |Card de mesmo id já cadastrado|
| 400 | Not Found | Ocorreu um erro|

---------------------------------------------------------

#### Listar todos os card do menu lateral

```bash
GET /side_menu_cards/getAll
```

**Respostas:**
| Código | Descrição | Resposta |
| :-------- | :------- | :------- |
| 200 | OK | Retorna a lista de cards ou vazio|
| 400 | Bad Request | Ocorreu um erro|

---------------------------------------------------------

#### Deletar um card do menu lateral
```bash
DELETE /side_menu_card/delete
```
| Parâmetro | Tipo | Descrição |
| :-------- | :------- | :------- |
| `id`| `string` | **Obrigatório:** Id card |

**Respostas:**
| Código | Descrição | Resposta |
| :-------- | :------- | :------- |
| 200 | OK | Card deletado com sucesso |
| 404 | Not Found | Card não encontrado |
| 400 | Bad Request | Ocorreu um erro|

----------------------------------------------------------

#### Criar um modal

```bash
POST /modal/create
```

| Parâmetro | Tipo | Descrição |
| :-------- | :------- | :------- |
| `id`| `string` | **Obrigatório:** Id modal |
| `name`| `string` | Nome do modal |
| `description`| `string` | Descrição do modal |
| `side_menu_card_id`| `string` | Id do card do menu lateral |

**Respostas:**
| Código | Descrição | Resposta |
| :-------- | :------- | :------- |
| 200 | OK | Modal criado com sucesso |
| 404 | Not Found | Card não encontrado |
| 409 | Conflict | Modal de mesmo id já cadastrado|
| 400 | Bad Request | Ocorreu Um erro|

----------------------------------------------------------

#### Listar todos os modais
```bash
GET /modal/getAll
```


| Parâmetro | Tipo | Descrição |
| :-------- | :------- | :------- |
| `id`| `string` | **Obrigatório:** Side_menu_card_id |

**Respostas:**
| Código | Descrição | Resposta |
| :-------- | :------- | :------- |
| 200 | OK | Retorna a lista de modais ou vazio|
| 404 | Not Found | Card não encontrado ||

----------------------------------------------------------

#### Deletar um modal
```bash
DELETE /modal/delete
```

| Parâmetro | Tipo | Descrição |
| :-------- | :------- | :------- |
| `id`| `string` | **Obrigatório:** Id modal |

**Respostas:**
| Código | Descrição | Resposta |
| :-------- | :------- | :------- |
| 200 | OK | Modal deletado com sucesso |
| 404 | Not Found | Modal não encontrado |

----------------------------------------------------------
#### Criar um modal card
```bash
POST /modal_card/create
```

| Parâmetro | Tipo | Descrição |
| :-------- | :------- | :------- |
| `id`| `string` | **Obrigatório:** Id modal card |
| `name`| `string` | Nome do modal card |
| `description`| `string` | Descrição do modal card |
| `modal_id`| `string` | Id do modal |

**Respostas:**
| Código | Descrição | Resposta |
| :-------- | :------- | :------- |
| 200 | OK | Modal card criado com sucesso |
| 404 | Not Found | Modal não encontrado |
| 409 | conflict | Modal_Card de mesmo id já cadastrado|
| 400 | Bad Request | Ocorreu Um erro

----------------------------------------------------------

#### Pegar um modal card
```bash
GET /modal_card/get
```
| Parâmetro | Tipo | Descrição |
| :-------- | :------- | :------- |
| `id`| `string` | **Obrigatório:** Id modal card |

**Respostas:**

| Código | Descrição | Resposta |
| :-------- | :------- | :------- |
| 200 | OK | Retorna o modal card ou vazio|
| 404 | Not Found | Modal card não encontrado |

---------------------------------------------------------

#### Listar todos os modal cards

```bash
GET /modal_card/getAll
```

| Parâmetro | Tipo | Descrição |
| :-------- | :------- | :------- |
| `id`| `string` | **Obrigatório:** Id modal |

**Respostas:**
| Código | Descrição | Resposta |
| :-------- | :------- | :------- |
| 200 | OK | Retorna a lista de modal cards ou vazio|
| 404 | Not Found | Modal não encontrado |

----------------------------------------------------------

#### Atualizar um modal card
```bash
PUT /modal_card/update
```
| Parâmetro | Tipo | Descrição |
| :-------- | :------- | :------- |
| `id`| `string` | **Obrigatório:** Id modal card |

**Respostas:**
| Código | Descrição | Resposta |
| :-------- | :------- | :------- |
| 200 | OK | Modal card atualizado com sucesso |
| 404 | Not Found | Modal card não encontrado |

----------------------------------------------------------------

#### Deletar um modal card
```bash
DELETE /modal_card/delete
```
| Parâmetro | Tipo | Descrição |
| :-------- | :------- | :------- |
| `id`| `string` | **Obrigatório:** Id modal card |

**Respostas:**
| Código | Descrição | Resposta |
| :-------- | :------- | :------- |
| 200 | OK | Modal card deletado com sucesso |
| 404 | Not Found | Modal card não encontrado |

----------------------------------------------------------









