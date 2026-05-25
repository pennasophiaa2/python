# Programa de casa de câmbio.
# Crie um programa que pergunte qual moeda deseja obter e qual moeda irá dar em troca:
# A. Moedas a considerar: Dolar, Real, Euro e Libra esterlina
# B. Informar as cotações das moedas em uma variável já no início do código

#  EX:
#  Quero: Euro
#  Tenho: Real
#  Valor desejado: 100 Euros
#  Valor necessário: 578,00 Reais

#  EX2:
#  Quero: Libra esterlina
#  Tenho: Euro
#  Valor desejado: 100 Libras
#  Valor necessário: 120 Euros

menu = '''
[1] Real
[2] Dolar
[3] Euro
[4] Libra'''
real_dolar = 5.02
real_euro = 5.85
real_libra = 6.79

print(menu)
entrada = int(input('Qual moeda você tem?'))
saida = int(input('Qual moeda você deseja?'))
valor = float(input('Quanto você deseja da moeda de saida?'))

valor_em_reais = 0
if entrada == 1 and saida == 1:
    valor_em_reais = valor
elif entrada == 2:
    valor_em_reais = valor * real_dolar
elif entrada == 3:
    valor_em_reais = valor * real_euro
elif entrada == 4:
    valor_em_reais = valor * real_libra

if saida == 1: #quer real
    print('Valor em reais', valor_em_reais)
elif saida == 2: #quer dolar
    print('Valor em dólares', valor_em_reais/real_dolar)
elif saida == 3: #quer euro
    print('Valor em euros', valor_em_reais/real_euro)
elif saida == 4: #quer libra
    print('Valor em libras', valor_em_reais/real_libra)

#Estudar: Laço de repetição FOR
