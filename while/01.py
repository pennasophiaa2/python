#while -> executa repetidamente até uma condição parar
#for -> executa número pré-definido de repetições

# numero = 1
# while numero <= 10:
#     print (numero)
#     numero +=1

#Criar um algoritimo que recebe vários números, e só para quando a soma deles for mais que 100

soma = 0
while True:
    numero = int(input('Digite um  número: '))
    soma +=numero
    if soma == 50 or soma > 100:
        break
print (soma)