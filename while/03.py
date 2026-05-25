#Crie um algoritimo que recebe um número indeterminado de valores, ao final diz
# quantos números eram positivos e quantos números eram negativos. Para encerrar o programa,
# o usuario digita 0.

positivos = 0
negativos = 0

while True:
    numero = int(input('Digite um  número: '))
    if numero == 0:
        break
    if numero > 0:
        positivos += 1
    else:
        negativos += 1
print ('Quantidade de positivos' , positivos)
print ('Quantidade de negativos' , negativos)