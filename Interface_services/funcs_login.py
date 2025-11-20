import streamlit as st
import requests

def criar_conta(utilizador,pw,saldo,role=2):
    """
    Esta função serve para criar uma conta através da API
    params : 
        utilizador : nome de utilizador a ficar associado á conta
        pw : password a ficar associada á conta
        saldo : saldo que a conta irá ter ao ser criada
        role : 1 - admin | 2 - cliente
    """
    url = "http://127.0.0.1:8000/criar_conta"
    params = {"utilizador": utilizador, "password": pw, "saldo":saldo,"role":role}
    response = requests.post(url, params=params)

    if response.status_code == 200:
         st.success(response.text)  
    else:
        st.error("Erro ao comunicar com o servidor.")

def pop_up_criar_conta_cliente():
    """
    Esta função serve para criar um pop-up para criar conta 
    
    """
    st.subheader("Criar conta 🔑")
    with st.popover("Criar Conta"):
        utilizador = st.text_input("Utilizador", key="novo_utilizador")
        senha = st.text_input("Password", type="password",key="nova_senha")
        saldo = st.number_input("Saldo",key="novo_Saldo")

        if st.button("Criar conta"):
            criar_conta(utilizador,senha,saldo)

def login():
    """
    Esta funçao serve para construir o layout do login e atribuir os valores da sessão ás variaveis session_state
     -Pede utilizador e senha ao user e envia os dados á api
     -A api vai verificar os dados recebidos e retornar se o login é valido e a role do utilizador que fez login
    """
    st.title("Banco online - Login 💰")
    utilizador = st.text_input("Utilizador",key="login_utilizador")
    senha = st.text_input("Password", type="password",key="login_senha")

    if st.button("Entrar"):

        url = "http://127.0.0.1:8000/login"
        params = {"utilizador": utilizador, "password": senha}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            dados=response.json()
            if dados.get("valido") == True:
                st.session_state["autenticado"]=True
                st.session_state["user"]=utilizador
                st.session_state["role"]=dados.get("role")
                #print("Role:", st.session_state["role"])
                st.success(f"Bem-vindo, {utilizador}!")
                st.rerun()
            else:
                st.error("Credenciais inválidas")
        else:
            st.error("Erro ao comunicar com a api")
    pop_up_criar_conta_cliente()

def logout():
    """
    Esta funçao serve para dar clear aos dados da variavel session_state e atualizar a página 
    """
    st.session_state.clear()
    st.rerun()

def get_roles():
    url = "http://127.0.0.1:8000/get_roles"
    response = requests.post(url)

    dados = response.json()

    return dados

def pop_up_criar_conta_admin(session_role):
    """
    Esta função serve para criar um pop-up para criar conta caso o user logado seja um admin
    params : 
        session_role: é a role do user que está logado (1-Admin,2-Cliente)
    """
    if session_role==1 or session_role==3:
        st.subheader("Criar conta 🔑")
        with st.popover("Criar Conta"):
            utilizador = st.text_input("Utilizador")
            senha = st.text_input("Password", type="password")
            saldo = st.number_input("Saldo")

            roles=get_roles()
            opcoes = {f"{id_role} - {nome_role}" for id_role, nome_role in roles.items()}

            role_str = st.selectbox(
                "Selecione o tipo de conta", opcoes)
            role = int(role_str.split(" - ")[0])

            if st.button("Criar conta"):
                criar_conta(utilizador,senha,saldo,role)
