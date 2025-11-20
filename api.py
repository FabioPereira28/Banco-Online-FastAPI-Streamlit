from fastapi import FastAPI
from Contas_api import funcs_login
from Operacoes_api import funcs_operacoes

app=FastAPI()

@app.get("/login", tags=["Login"])
def login(utilizador,password):
    valido, role = funcs_login.login(utilizador,password)
    return {"valido":valido,"role":role}
    
@app.post("/criar_conta", tags=["Login"])
def new_account(utilizador,password,saldo,role=2):
    return funcs_login.criar_conta(utilizador,password,role,saldo)

@app.get("/consultar_saldo", tags=["Operações nas contas"])
def get_saldo(utilizador):
    return funcs_operacoes.consultar_saldo(utilizador)

@app.post("/deposito", tags=["Operações nas contas"])
def depositar(utilizador,valor):
    return funcs_operacoes.deposito(utilizador,valor)

@app.post("/levantamento", tags=["Operações nas contas"])
def levantar(utilizador,valor):
    return funcs_operacoes.levantamento(utilizador,valor)

@app.post("/transferencia", tags=["Operações nas contas"])
def transferencia(utilizador_envio,utilizador_destino,valor):
    return funcs_operacoes.transferencia(utilizador_envio,utilizador_destino,valor)

@app.post("/get_roles", tags=["Operações base de dados"])
def get_roles():
    return funcs_operacoes.get_roles()