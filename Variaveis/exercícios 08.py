# Criar um algoritmo que recebe 3 lados de um triângulo, e classifica entre:
# Isóceles -> 2 lados iguais
# Escaleno -> 3 lados diferentes
# Equilátero -> 3 lados iguais
# Não Triângulo -> quando um lado é maior que a soma dos outros 2.

l1 = int(input('Lado 1:'))
l2 = int(input('Lado 2:'))
l3 = int(input('Lado 3:'))

if l1 == l2 == l3:
    print('Equilátero')
elif l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
    print('Não Triângulo')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('Isóceles')
else:
    print('Escaleno')





