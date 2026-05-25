# cpf = input ('digite seu CPF em hífen nem pontos: ')
# if len(cpf) != 11:
# 	print('cpf inválido')
# else:
# 	soma =0
# 	multiplicador = 10
# 	for i in range (9):
# 		soma += int (cpf[i]) * multiplicador
# 		multiplicador -= 1
# 	primeiro = 11 - soma%11
# 	if primeiro >=10:
# 		primeiro = 0
# soma = 0
# multiplicador = 11
# for i in range (10):
# 	soma += int(cpf[i]) * multiplicador
# 	multiplicador -= 1
# 	segundo = 11 - soma%11
# 	if segundo >= 10:
# 		segundo = 0
# if primeiro == int(cpf[9]) and segundo == int(cpf[10]):
# 	print ('cpf valido')
# else:
# 	print ('cpf invalido')


cpf = input("Digite seu CPF (sem hífen nem pontos): ").replace(".", "").replace("-", "")

if len(cpf) != 11:
    print("CPF inválido")
else:
    # Valida o CPF
    soma = 0
    multiplicador = 10
    for i in range(9):
        soma += int(cpf[i]) * multiplicador
        multiplicador -= 1
    primeiro = 11 - (soma % 11)
    if primeiro >= 10:
        primeiro = 0

    soma = 0
    multiplicador = 11
    for i in range(10):
        soma += int(cpf[i]) * multiplicador
        multiplicador -= 1
    segundo = 11 - (soma % 11)
    if segundo >= 10:
        segundo = 0

    if primeiro == int(cpf[9]) and segundo == int(cpf[10]):
        print("CPF válido")
    else:
        print("CPF inválido")