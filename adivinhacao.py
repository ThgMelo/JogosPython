import random

def jogar():
    print('*********************************')
    print('Bem vindo ao jogo de adivinhação!')
    print('*********************************\n')

    numero_secreto = round(random.randrange(1, 101))

    total_de_tentativas = 0
    pontos = 1000

    print('Qual o nível de dificuldade?')
    print('(1) Fácil | (2) Médio | (3) Difícil')
    nivel = int(input('Defina o nível: '))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f'Tentativa {rodada} de {total_de_tentativas}')
        chute_str = int(input('Digite o seu numero entre 1 e 100: '))
        print('Você digitou ', chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print('Você deve digitar um número entre 1 e 100!')
            continue



        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f'Você acertou e fez {pontos} pontos!')
            break
        else:
            if maior:
                print('Você errou! O seu chute foi maior que o número secreto.\n')
            elif menor:
                print('Você errou! Seu chute foi menor que o número secreto\n')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print('\nFim do jogo')

if __name__ == '__main__':
    jogar()