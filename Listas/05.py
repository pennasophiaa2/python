#crie um algoritimo que controla as movimentações de bolsas de sangue do hemosc:
#O programa deve ter as seguintes opções:

#-Doar sangue (define qual tipo e acrescente 1 unidade)
#-Retirar sangue (define qual tipo e retira múltiplas de 5 unicades;
#- Visualizzar saldo de bolsas
#- Consultar movimentações de estoque

# Sistema de Controle de Bolsas de Sangue - HEMOSC


tipos = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
saldos = [10, 10, 12, 11, 6, 6, 2, 1]

movimentacoes = []


def mostrar_tipos():
    print("\nTipos disponíveis:")
    for tipo in tipos:
        print("-", tipo)


def doar_sangue():
    mostrar_tipos()

    tipo = input("\nDigite o tipo sanguíneo da doação: ").upper()

    if tipo in tipos:
        indice = tipos.index(tipo)

        saldos[indice] += 1

        mensagem = f"Doação: +1 bolsa de {tipo}"
        movimentacoes.append(mensagem)

        print("Doação registrada com sucesso!")

    else:
        print("Tipo sanguíneo inválido!")


def retirar_sangue():
    mostrar_tipos()

    tipo = input("\nDigite o tipo sanguíneo da retirada: ").upper()

    if tipo in tipos:

        indice = tipos.index(tipo)

        quantidade = int(input("Quantidade de bolsas (múltiplo de 5): "))

        if quantidade % 5 != 0:
            print("Erro: a quantidade deve ser múltipla de 5!")
            return

        if quantidade > saldos[indice]:
            print("Erro: estoque insuficiente!")
            return

        saldos[indice] -= quantidade

        mensagem = f"Retirada: -{quantidade} bolsas de {tipo}"
        movimentacoes.append(mensagem)

        print("Retirada registrada com sucesso!")

    else:
        print("Tipo sanguíneo inválido!")


def visualizar_saldos():

    print("\n===== SALDOS =====")

    for i in range(len(tipos)):
        print(f"{tipos[i]}: {saldos[i]} bolsas")


def consultar_movimentacoes():

    print("\n===== MOVIMENTAÇÕES =====")

    if len(movimentacoes) == 0:
        print("Nenhuma movimentação registrada.")

    else:
        for mov in movimentacoes:
            print("-", mov)


while True:

    print("\n===== HEMOSC =====")
    print("1 - Doar sangue")
    print("2 - Retirar sangue")
    print("3 - Visualizar saldo")
    print("4 - Consultar movimentações")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        doar_sangue()

    elif opcao == '2':
        retirar_sangue()

    elif opcao == '3':
        visualizar_saldos()

    elif opcao == '4':
        consultar_movimentacoes()

    elif opcao == '5':
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida!")