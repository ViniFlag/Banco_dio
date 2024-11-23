import textwrap;
def menu():
    print(textwrap.dedent("""
    ============= Menu =============   
    1 - Depositar 
    2 - Sacar
    3 - Extrato
    4 - Nova Conta
    5 - listar contas
    6 - Novo Usuário
    0 - Sair  
    =================================
"""))
    opcao = input("digite a opção desejada: ")
    return int(opcao)

def depositar(saldo, valor, extrato, /):
     if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Deposito concluido com Sucesso.")
     else:
        print("Operação inválida! O valor informado é inválido.")
     return saldo, extrato   

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
      valor = float(input("informe o valor do saque: "))
      
      excedeu_saldo = valor > saldo

      excedeu_limite = valor > limite

      excedeu_saques = numero_saques >= limite_saques
      if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

      elif excedeu_limite:
        print("Operação falhou! O valor do saque excedeu o limite.")

      elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

      elif valor > 0:
         saldo -= valor
         extrato += f"Saque: R$ {valor:.2f}\n" 
         numero_saques += 1
      else:
            print("Operação inválida! O valor informado é inválido.")
      return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n=============== EXTRATO ===============")
    print("Não foram realizadas movimentações na sua conta." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe seu cpf completo!(Somente números): ")
    usuarios = filtrar_usuario(cpf, usuarios)
    
    if usuarios:
         print("Já existe um usuario com esse cpf!")  
         return
    nome = input("Informe seu nome: ")
    data_nascimento = input("informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input ("informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nConta criada com sucesso!")

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")    

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3  
    AGENCIA= "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == 2:
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            criar_usuario(usuarios)
        
        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 0:
            break  
        else:
            print("Operação invalida, por favor selecione uma operação válida")



main()