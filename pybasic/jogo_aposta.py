#pequeno jogo de aposta em python

numero_secreto = 35
total_de_tentativas = 5

while (total_de_tentativas > 0):
    chute = int(input('Digite o seu número: '))
    print('Você digitou: ', chute)
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if(acertou):
        print('Você acertou')
        break
    elif(maior):
        print('Você errou! O seu chute foi maior que o número secreto')
    elif(menor):
        print('Você errou! O seu chute foi menor que o número secreto')

    total_de_tentativas = total_de_tentativas - 1
