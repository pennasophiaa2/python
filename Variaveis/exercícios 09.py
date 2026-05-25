# Crie um algoritmo que recebe o nome de uma pessoa e classifique:
# começa com vogal
# começa com consoante
# inicio e fim iguais
# inicio e fim diferentes

# nome = 'Luan'
# print(len(nome))
# print(nome[0])

nome = input('Nome:').upper()

if nome[0] == nome[-1]:
    print('inicio e fim iguais')
else:
    print('inicio e fim diferentes')
if nome[0] == 'A' or nome[0] == 'E' or nome[0] == 'I' or nome[0] == 'O' or nome[0] == 'U':
    print('Começa com vogal')
else:
    print('Começa com consoante')


