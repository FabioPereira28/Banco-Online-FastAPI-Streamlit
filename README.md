# Banco Online – README
Este projecto consiste numa aplicação bancária simples composta por duas partes:
uma API FastAPI responsável pela lógica de autenticação e operações bancárias e
uma interface gráfica em Streamlit que permite ao utilizador interagir facilmente com o sistema.

# Requisitos
Para correr o projecto é necessário ter instalado:

- Python 3.9+
- Pip (gestor de pacotes)
- As seguintes bibliotecas Python:
  ``` bash
  fastapi
  uvicorn
  pandas
  requests
  streamlit

Podes instalar tudo de uma só vez com:
 ```bash
  pip install fastapi uvicorn pandas requests streamlit
 ```
# Como executar o projecto
1. Iniciar a API (backend)
```bash
uvicorn api:app
```
A API ficará disponível em: http://127.0.0.1:8000

2. Iniciar a interface streamlit(frontend)
``` bash
streamlit run interface.py
```
O navegador abrirá automaticamente com a interface do banco online.

# Funcionalidades
# API
A API expõe endpoints para:
  - Login
  - Criar conta
  - Consultar saldo
  - Depositar
  - Levantar
  - Transferir dinheiro
  - Obter lista de roles

A API comunica com ficheiros TXT para armazenar utilizadores e saldos.

# Interface Streamlit
  - A interface permite:
  - Fazer login
  - Criar conta (cliente ou admin)
  - Consultar saldo
  - Fazer depósitos
  - Fazer levantamentos
  - Realizar transferências
  - Administradores podem criar contas com qualquer role
  - Logout

Toda a comunicação com a API é feita via pedidos HTTP usando a biblioteca requests.

# Notas finais
- Este projecto utiliza ficheiros .txt como base de dados, por isso garante que a pasta /Banco existe e contém os ficheiros necessários.
- Certifica-te de que a API está a correr antes de abrir a interface.
