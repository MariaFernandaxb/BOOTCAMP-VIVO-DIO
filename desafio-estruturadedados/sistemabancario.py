import textwrap

def menu():
    menu = """
    [1] DEPÓSITO 
    [2] SAQUE
    [3] EXTRATO
    [4] ABRIR CONTA
    [5] LISTA CONTA
    [6] NOVO USUÁRIO
    [0] SAIR 
    
    DIGITE A OPÇÃO DESEJADA:  """

    return float(input(textwrap.dedent(menu)))


def deposito(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}"
        print("Depósito realizado com sucesso! ")

    else:
        print("Falha na operação! O valor informardo é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, qntd_saques, lim_saques):
    excedeu_saldo = valor > saldo
    excedeu_lim = valor > limite
    excedeu_saques = qntd_saques >= lim_saques

    if excedeu_saldo: 
        print("Falha na operação! Saldo insuficiente.")

    elif excedeu_lim:
        print("Falha na operação! O valor de saque excede o limite.")

    elif excedeu_saques:
        print("Falha na operação! Número máximo de saque excedido. " )

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}"
        qntd_saques += 1
        print("Saque realizado com sucesso! ")
        
    else: 
        print("Falha na operação! Valor informado é inválido")
    
    return saldo, extrato

def mostrar_extrato(saldo,/, *, extrato):
    print("="*5, "EXTRATO", "="*5)
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("="*20)

def criar_usuario(usuarios):
    cpf = input("Informe o número do CPF: ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Usuário já cadastrado. Tente Novamente!")
        return

    nome = input("DIGITE O NOME COMPLETO: ")
    data_nasc = input("DIGITE A DATA DE NASCIMENTO: ")
    endereco = input("DIGITE O ENDERECO(logradouro, nº, bairro, cidade/sigla do estado): ")

    usuarios.append({"nome": nome, "data_nasc":data_nasc, "cpf":cpf, "endereco":endereco})

    print(" <<<<< USUÁRIO CADASTRADO COM SUCESSO ! >>>>>")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, num_conta, usuarios):
    cpf = input("DIGITE O CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("<<<<< CONTA CRIADA COM SUCESSO! >>>>>")
        return{"agencia":agencia, "num_conta":num_conta, "usuario":usuario}
    
    print("Usuario não encontrado. criação de conta encerrado ...")

def listar_contas(contas):
    for conta in contas: 
        linha = f"""
            Agencia: {conta['agencia']}
            Conta Corrente: {conta['num_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("="*100)
        
        print(textwrap.dedent(linha))


def main():
    LIM_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    qntd_saques = 0
    usuario = []
    contas = []


    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input("Informe o valor do depósito:R$  "))

            saldo, extrato = deposito(saldo, valor, extrato)
        
        elif opcao == 2:
            valor = float(input("Informe o valor do saque:R$  "))

            saldo, extrato= sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite, 
                qntd_saques=qntd_saques,
                lim_saques=LIM_SAQUES                
            )
            
     
        elif opcao == 3:
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            criar_usuario(usuario)
        
        elif opcao == 5:
            listar_contas(contas)    

        elif opcao == 6:
            num_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, num_conta, usuario)

            if conta:
                contas.append(conta)
        
        elif opcao == 0:
            print("Obrigado! Volte Sempre !")
            break

        else: 
            print("Opção inválida! Tente novamente. ")


main()