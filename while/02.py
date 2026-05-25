#Crie um prgrama que recebe um numero indetermina de valores.
# Ao final, exibe qual foi o maior valor.
# Para parar o programa, o usuario informa "Sair"
#
#
# maior = None
# while True:
#     valor = input("Digite um valor ou sair: ")
#
#     if valor.lower() == "sair":
#         break
#
#     numero = int(valor)
#
#     if maior is None or numero > maior:
#         maior = numero
#
# print("Maior valor digitado:", maior)

contador = 0
while True:
    valor = input("Digite um valor ou sair: ")

    if valor.lower() == "sair":
        break
    if contador == 0:
        maximo = int(valor)
        contador +=1
        continue
    if int(valor) > maximo:
        maximo = int(valor)

if contador > 0:
    print (maximo)
else:
    print ("Nenhum número lançado")