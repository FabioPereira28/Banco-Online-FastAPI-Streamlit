import streamlit as st
import requests

def get_saldo(utilizador):
    url = "http://127.0.0.1:8000/consultar_saldo"
    params = {"utilizador": utilizador}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.text  
    else:
        return -1

def deposito(utilizador,valor):
    url = "http://127.0.0.1:8000/deposito"
    params = {"utilizador": utilizador, "valor": valor}
    response = requests.post(url, params=params)

    if response.status_code == 200:
        st.success(f"{response.text} - Saldo atualizado: {get_saldo(utilizador)}€")  
    else:
        st.error("Erro ao comunicar com o servidor.")

def levantamento(utilizador,valor):
    url = "http://127.0.0.1:8000/levantamento"
    params = {"utilizador": utilizador, "valor": valor}
    response = requests.post(url, params=params)

    if response.status_code == 200:
         st.success(f"{response.text} - Saldo atualizado: {get_saldo(utilizador)}€")  
    else:
        st.error("Erro ao comunicar com o servidor.")

def transferencia(user_envio,user_destino,valor):
    url = "http://127.0.0.1:8000/transferencia"
    params = {"utilizador_envio":user_envio, "utilizador_destino":user_destino, "valor":valor}
    response=requests.post(url,params=params)

    if response.status_code == 200:
        st.success(f"{response.text} - Saldo atualizado {get_saldo(user_envio)}€")
    else:
        st.error("Erro ao comunicar com o servidor.")