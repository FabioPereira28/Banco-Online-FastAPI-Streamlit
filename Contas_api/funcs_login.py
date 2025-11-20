import pandas as pd


def login(us,pw):
    """
    Esta função serve para verificar se o login está correto
    Se o utilizador e a password estiverem no ficheiro retorna True
    Se o utilizador e a password não estiverem no ficheiro retorna False
    """
    try:
        utilizadores = pd.read_csv("./Banco/logins.txt", sep = ",")
    except Exception as e:
        return False, None
    
    for indice, linha in utilizadores.iterrows():
        if linha["user"] == us and linha["pass"]==pw:
            return True, linha["id_role"]
        
    return False, None
        
def criar_cliente(user,saldo=0):
    """"
    Esta funçao serve para criar um cliente no ficheiro de clientes.
    Recebe um user, uma role e um saldo (por default saldo=0)
    """
    nome_ficheiro="./Banco/clientes.txt"

    try:
        utilizadores = pd.read_csv(nome_ficheiro, sep = ",")
    except Exception as e:
        return "Ocorreu um erro ao ler o ficheiro"
    
    nova_linha={"user":user,"saldo":saldo}
    ficheiro_concatenado = pd.concat([utilizadores,pd.DataFrame([nova_linha])])

    ficheiro_concatenado.to_csv(nome_ficheiro,index=False)
        
def criar_conta(us,pw,role,saldo):
    """
    Esta função serve para criar uma conta
    É pedido um utilizador e uma password.
    É feita a verificação se o user existe, 
        -caso exista: retorna mensagem a dizer que ja existe
        -caso nao exista: é adicionado o user e a password ao ficheiro de logins e criado o cliente no ficheiro de clientes
    """
    nome_ficheiro="./Banco/logins.txt"

    try:
        utilizadores = pd.read_csv(nome_ficheiro, sep = ",")
    except Exception as e:
        return "Ocorreu um erro ao ler o ficheiro"

    for indice, row in utilizadores.iterrows():
        if row["user"] == us:
            return "User já existente, utilize outro nome de utilizador"
    
    novo_login={"user":us,"pass":pw,"id_role":role}

    novo_ficheiro = pd.concat([utilizadores,pd.DataFrame([novo_login])], ignore_index=True)
    novo_ficheiro.to_csv(nome_ficheiro, index=False)

    criar_cliente(us,saldo)
    return "Conta criada com sucesso"