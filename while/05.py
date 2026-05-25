from random import randint

numero = randint(1, 100)

while True:
    palpite = int(input("Tente adivinhar o número de 1 a 100: "))

    if palpite == numero:
        print("Parabéns! Você acertou!")
        break

    elif palpite > numero:
        print("O número é menor!")

    else:
        print("O número é maior!")