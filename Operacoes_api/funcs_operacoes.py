import pandas as pd

def consultar_saldo(user):
    """
    Esta funçao serve para consultar o saldo de um utilizador
    params:
        user - username do utilizador a consultar o saldo
    return:
        saldo(int) - se o user existir
        "Não existe nenhuma conta com esse user"(str) - se o user nao existir
    """
    nome_ficheiro="./Banco/clientes.txt"
    try:
        utilizadores = pd.read_csv(nome_ficheiro, sep = ",")
    except Exception as e:
        return "Ocorreu um erro ao ler o ficheiro"
    
    for indice,row in utilizadores.iterrows():
        if row["user"]==user:
            return row["saldo"]
        
    return "Não existe nenhuma conta com esse user"

def deposito(user,valor):
    """
    Esta funçao serve para fazer um deposito na conta de um utilizador
    params:
        user - nome do user a depositar
        valor - valor a ser depositado na conta
    """
    nome_ficheiro="./Banco/clientes.txt"

    try:
        clientes = pd.read_csv(nome_ficheiro, sep = ",")
    except Exception as e:
        return "Ocorreu um erro ao ler o ficheiro"
    
    valor_depositar = float(valor)
        
    if user not in clientes["user"].values:
        return "Não existe uma conta com esse user"
    
    clientes.loc[clientes["user"]==user,"saldo"]+=valor_depositar
    clientes.to_csv(nome_ficheiro,index=False)
    return "Depósito efetuado com sucesso"
    
        
def levantamento(user,valor):
    """
    Esta funçao serve para fazer um levantamento da conta de um utilizador
    params:
        user - nome do user a levantar
        valor - valor a ser levantado da conta
    """
    nome_ficheiro="./Banco/clientes.txt"

    try:
        clientes = pd.read_csv(nome_ficheiro, sep = ",")
    except Exception as e:
        return "Ocorreu um erro ao ler o ficheiro"
    
    valor_debitar = float(valor)
        
    if user not in clientes["user"].values:
        return "Não existe uma conta com esse user"
    
    clientes.loc[clientes["user"]==user,"saldo"]-=valor_debitar
    clientes.to_csv(nome_ficheiro,index=False)
    return "Levantamento efetuado com sucesso"

def transferencia(user_envio,user_destino,valor):
    """
    Esta funçao serve para fazer uma transferencia de dinheiro entre contas
    params:
        user_envio: utilizador que faz o envio do dinheiro
        user_destino: utilizador que vai receber o dinheiro
        valor: valor que vai ser transferido do user_envio para o user_destino
    """
    nome_ficheiro="./Banco/clientes.txt"
    utilizador_existe=0
    valor_float=float(valor)
    try:
        clientes=pd.read_csv(nome_ficheiro, sep=",")
    except Exception as e:
        return "Ocorreu um erro ao ler o ficheiro"
    
    for indice, row in clientes.iterrows():
        if row["user"]==user_destino:
            utilizador_existe=1
    
    if utilizador_existe==0:        
        return "Não existe esse user. Tente novamente"
    else:
        for indice, row in clientes.iterrows():
            if row["user"]==user_envio:
                if row["saldo"] < valor_float:
                    return "Saldo insuficiente para transferencia"
                else:
                    clientes.loc[indice,"saldo"]=row["saldo"]-valor_float #tira saldo ao cliente a enviar
                    
                    
        for indice, row in clientes.iterrows():
                if row["user"]==user_destino:
                    clientes.loc[indice,"saldo"]=row["saldo"]+valor_float #coloca saldo ao cliente a receber
                    clientes.to_csv(nome_ficheiro,index=False)       
        return "Transferencia efetuada com sucesso!"    

def get_roles():
    """
    Esta funçao retorna todas as roles que existem no ficheiro de roles
    """
    nome_ficheiro="./Banco/roles.txt"

    try:
        roles_df=pd.read_csv(nome_ficheiro,sep=",")
    except Exception as e:
        return "Ocorreu um erro ao ler o ficheiro"
    
    dicionario_roles={}

    for indice,row in roles_df.iterrows():
        dicionario_roles[row["id_role"]]=row["nome"]

    return dicionario_roles