# 📦 Arquitetura da Biblioteca TikTok Automation

Esta biblioteca é organizada de forma modular para facilitar a automação e controle de interações com o TikTok, com foco em legibilidade, manutenção e expansão.

---

## 📁 Estrutura do diretório `service/`

```
service/
├── actions.py        # Curtir, seguir, comentar
├── auth.py           # Login e controle de autenticação
├── config.py         # Configurações globais
├── extraction.py     # Coleta de dados (vídeos, perfis, estatísticas)
├── posts.py          # Lógica de postagem e agendamento
├── sessions.py       # Gerenciamento de sessões e cookies
├── paths.py          # Gerenciamento das paths do selenium
├── monitor.py        # Coleta dados da sua conta e de outras pessoas 
└── upload.py         # Upload de vídeos
```

---

## 🧹 Módulos explicados

### 🔐 `auth.py`

Responsável por autenticação no TikTok:

* Login com credenciais
* Uso de cookies persistentes
* Armazenamento e carregamento de sessão (`storage_state.json` via Selenium)

---

### 📆 `config.py`

Em breve

---

### 📂 `sessions.py`

Gerencia múltiplas sessões:

* Salvar sessões por usuário
* Alternar entre contas
* Listar e limpar sessões existentes

---

### 🧐 `extraction.py`

Faz scraping de:

* Perfis de usuários
* Estatísticas de vídeos (Em teste)
* Hashtags, comentários, curtidas
* Frequência e histórico de postagens

Pode ser estendido para monitoramento de concorrentes.

---

### 🤖 `actions.py`

Automatiza ações sociais:

* Curtir vídeos
* Comentar
* Seguir usuários
* Postar
* Excluir vídeo

Essas funções usam comandos diretos no DOM da interface web (via Selenium).

---

### 🗓 `posts.py`

* ANALISAR
* Gerencia lógica de postagem:

* Validação de arquivos
* Registro de uploads
* Agendamento (cron ou biblioteca como `apscheduler`)

---


## 📀 Requisitos básicos

* Python 3.11+
* `pip install -r requirements.txt`
