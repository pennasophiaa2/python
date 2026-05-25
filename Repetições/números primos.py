#Crie um algoritimo que recebe um número e retorna se ele é primo ou não;
#Para isso, precisa apresender "Break"

#Estudar para próxima aula:
#while,break,continue,while True;

numero = int(input("Digite um número: "))

if numero <= 1:
    print("Não é primo")
else:
    primo = True

    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break  # interrompe o laço quando encontra um divisor

    if primo:
        print("É primo")
    else:
        print("Não é primo")