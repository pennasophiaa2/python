#Crie um algoritimo que recebe vários nomes, ao final, exibe quantas letras
#foram digitadas
#Para parar, o usuário informa "PARAR", verificar quantas vogais tem

total_letras = 0
total_vogais = 0

while True:
    nome = input("Digite um nome ou PARAR: ")

    if nome == "PARAR":
        break

    total_letras += len(nome)

    for letra in nome.lower():
        if letra in "aeiou":
            total_vogais += 1

print("Total de letras digitadas:", total_letras)
print("Total de vogais:", total_vogais)

#REGEX (expressoes regulares) em python