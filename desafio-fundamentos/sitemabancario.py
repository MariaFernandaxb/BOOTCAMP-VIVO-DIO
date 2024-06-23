# DESAFIO:  Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. O objetivo é implementar três operações essenciais: depósito, saque e extrato. O sistema será desenvolvido para um banco que busca monetizar suas operações. Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as operações bancárias. Prepare-se para aprimorar suas habilidades e demonstrar sua capacidade de desenvolver soluções práticas e eficientes.


banco = '''
    [1] DEPÓSITO
    [2] SAQUE
    [3] EXTRATO
    [0] SAIR


    DIGITE A OPÇÃO DESEJADA:  '''

saldo = 0
limite = 500
extrato = ""
qntd_saques = 0
LIM_SAQUES = 3


while True:
    
    opcao = int(input(banco))

    if opcao == 1:
        valor = float(input("Informe o valor do depósito:R$  "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Falha na operação. Valor informado é inválido.")
    
    elif opcao == 2:
        valor = float(input("Informe o valor do saque:R$  "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = qntd_saques > LIM_SAQUES

        if excedeu_saldo:
            print("Falha na operação! Saldo insuficiente")
            
        elif excedeu_limite:
            print("Falha na operação! O valor do saque excedeu o limite")

        elif excedeu_saques:
            print("Falha na operação! Limite de saques excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R${valor:.2f}"
            qntd_saques += 1 

        else:
            print("Falha na operação. Valor informado é inválido.")

    elif opcao == 3:
        print('='*10, 'EXTRATO', '='*10)
        print('Não foram realizadas operações' if not extrato else extrato)
        print(f"\n Saldo R$ {saldo:.2f}")
        print('='*30)

    elif opcao == 0:
        print("Obrigado! Volte Sempre !")
        break

    else: 
        print("Opção inválida! Tente novamente. ")

