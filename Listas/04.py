#crie um algoritimo que recebe 5 nomes e ao final, retorna:
#o nome mais comprido
#os nomes que começam com vogal.

nomes, nomes_vogais, maiores_nomes = [], [], ['',]

for _ in range(5):
    nome = input('Digite o nome: ')
    nomes.append(nome)
    if nome[0].lower() in 'AEIOUaeiou':
        nomes_vogais.append(nome)
    if len(nome) > len(maiores_nomes[0]):
        maiores_nomes.clear()
        maiores_nomes.append(nome)
    elif len (nome) == len(maiores_nomes [0]):
        maiores_nomes.append(nome)
print(f'Maiores nomes: {maiores_nomes}')
print(f'Nomes que iniciam com vogal: {nomes_vogais}')

