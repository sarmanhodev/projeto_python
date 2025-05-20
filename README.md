
# 🐍 projeto_python – Projeto Básico com Flask + pyodbc

Este é um projeto básico usando **Python + Flask** que realiza a listagem de assuntos armazenados em um banco de dados SQL Server, utilizando **conexão via pyodbc**.

---

## 📁 Estrutura do Projeto

```
projeto_python/
├── app.py                  # Aplicação principal Flask
├── conexoes.py             # Função de conexão e consulta ao banco de dados
├── venv/                   # Ambiente virtual (não enviar para o GitHub)
└── templates/
    └── assuntos.html       # Template HTML para exibir os assuntos
```

---

## ▶️ Como Executar o Projeto

### 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/projeto_python.git
cd projeto_python
```

### 2. Ative o ambiente virtual existente:

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **Linux/macOS:**
  ```bash
  source venv/bin/activate
  ```

 ## 📦 Dependências

Instale o Flask e o pyodbc (caso ainda não tenha):

```bash
pip install flask pyodbc
```

A instalaçãodas dependências também poderá ser feita através do arquivo requirements.txt, executando o comando: pip install -r requirements.txt

### 3. Execute a aplicação:

```bash
python app.py
```

---

## 🌐 Acesse no navegador

```
http://127.0.0.1:5000/carregar_assunto
```
---

## ❗ Observação

É recomendado **usar um ambiente virtual (venv)** para evitar conflitos de dependências entre projetos.

---

## 🧑‍💻 Autor

- Diego Sarmanho - https://github.com/sarmanhodev
