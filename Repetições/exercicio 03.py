#Crie um algoritimo que recebe 10 números e retorna:
# - A soma entre eles
# - A média aritmética simples
# - Quantos eram pares
# - Quantos eram impares
# - Quantos positivos
# - Quantos negativos
# - Quantos zeros
# - Maior valor
# - Menor valor
#
# soma = 0
# pares = 0
# impares = 0
# positivos = 0
# negativos = 0
# zeros = 0
#
# for i in range(5):
#     numero = int(input("Digite um número: "))
#
#     if i == 0:
#         maior = numero
#         menor = numero
#
#     soma += numero
#
#     if numero % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
#
#     if numero > 0:
#         positivos += 1
#     elif numero < 0:
#         negativos += 1
#     else:
#         zeros += 1
#
#     if numero > maior:
#         maior = numero
#
#     if numero < menor:
#         menor = numero
#
# media = soma / 10
#
# print("Soma:", soma)
# print("Média:", media)
# print("Quantidade de pares:", pares)
# print("Quantidade de ímpares:", impares)
# print("Quantidade de positivos:", positivos)
# print("Quantidade de negativos:", negativos)
# print("Quantidade de zeros:", zeros)
# print("Maior valor:", maior)
# print("Menor valor:", menor)