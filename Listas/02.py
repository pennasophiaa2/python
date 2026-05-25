#Crie um algoritimo que:
#-solicita quandos números quer armazenar:
#-soicita os numeros que serão armazenados:
#exibe todos ao final;

numeros = []  # lista pra guardar os números

# Solicita quantos números quer armazenar
quantidade = int(input('Quantos números você quer armazenar? '))

# Solicita os números que serão armazenados
for _ in range(quantidade):
    numero = float(input('Digite o número: '))
    numeros.append(numero)

# Exibe todos ao final
print('Números armazenados:')
for numero in numeros:
    print(numero)

#Soma de todos os valores

print (f'Total: {sum(numeros)}')
print (f'Máximo: {max(numeros)}')
print (f'Mínimo: {min(numeros)}')
print (f'Média: {sum(numeros)/len(numeros)}')