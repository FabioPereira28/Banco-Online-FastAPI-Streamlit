import streamlit as st
import requests
from Interface_services import funcs_login, funcs_operacoes

def pagina_principal():
    st.title(f"Banco online - Bem-vindo {st.session_state["user"]}💰")

    utilizador = st.session_state["user"]

    #####CONSULTAR SALDO#####
    st.subheader("Consultar saldo 💳")    
    if st.button("Ver saldo"):
        st.success(f"Saldo da conta: {funcs_operacoes.get_saldo(utilizador)}€")

    #####DEPÓSITOS#####
    st.subheader("Fazer Depósito 🪙")
    valor = st.number_input("Introduza o valor a depositar:", min_value=1.0, step=1.0)
    
    if st.button("Depositar dinheiro"):
        funcs_operacoes.deposito(utilizador,valor)

    #####LEVANTAMENTOS#####
    st.subheader("Fazer Levantamento 🏧")
    valor = st.number_input("Introduza o valor a levantar:", min_value=1.0, step=1.0)
    
    if st.button("Levantar dinheiro"):
        funcs_operacoes.levantamento(utilizador,valor)

    #####TRANSFERENCIAS#####
    st.subheader("Fazer Transferência 💸")
    user_destino = st.text_input("Utilizador a enviar: ")
    valor = st.number_input("Introduza o valor a levantar: ", min_value=1.0, step=1.0)
    
    if st.button("Fazer transferência"):
        funcs_operacoes.transferencia(utilizador,user_destino,valor)

    #####CRIAR CONTA ADMIN#####
    funcs_login.pop_up_criar_conta_admin(st.session_state["role"])

    #####LOGOUT#####
    if st.button("Sair"):
        funcs_login.logout()
    


if "autenticado" in st.session_state and st.session_state["autenticado"]:
    pagina_principal()
else:
    funcs_login.login()