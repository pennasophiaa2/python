from random import randint

cabecalho = '''                                                                      
    ▄▄▄▄▄            ▄▄                                               
    ▀▀▀██            ██                                               
       ██   ▄████▄   ██ ▄██▀    ▄████▄   ██▄████▄  ██▄███▄    ▄████▄  
       ██  ██▀  ▀██  ██▄██     ██▄▄▄▄██  ██▀   ██  ██▀  ▀██  ██▀  ▀██ 
       ██  ██    ██  ██▀██▄    ██▀▀▀▀▀▀  ██    ██  ██    ██  ██    ██ 
 █▄▄▄▄▄██  ▀██▄▄██▀  ██  ▀█▄   ▀██▄▄▄▄█  ██    ██  ███▄▄██▀  ▀██▄▄██▀ 
  ▀▀▀▀▀      ▀▀▀▀    ▀▀   ▀▀▀    ▀▀▀▀▀   ▀▀    ▀▀  ██ ▀▀▀      ▀▀▀▀   
                                                   ██                 
                                                                     '''
menu = '''
(1) Pedra
(2) Papel
(3)Tesoura
Escolha:'''

print(cabecalho)
opçao = int(input(menu))
valor = randint(1,3)
# Verificar se a opção escolhida é válida;
if opçao >= 1 and opçao <= 3:
    print('Jogada Válida')
    if opçao == valor:
        print('Empate')
    if opçao == 1 and valor == 3 or opçao == 2 and valor == 3 or opçao == 3 and valor == 2:
        print('Você Ganhou')
    else:
        print('Você Perdeu')

    if opçao == 1:
        print('Você Jogou Pedra')
    elif opçao == 2:
        print('Você Jogou Papel')
    else:
        print('Você Jogou Tesoura')

    if valor == 1:
        print(' PC Jogou Pedra')
    elif valor ==2:
        print('PC Jogou Papel')
    else:
        print('PC Jogou Tesoura')

else:
    print('Jogada Inválida')

