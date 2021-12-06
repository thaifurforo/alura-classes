import random as rd
import jogos
import adivinhacao

def main():
    print('*********************************\nBem vindo ao jogo de Adivinhação!\n*********************************')
    print('Qual o nível de dificuldade?\n1 - Fácil\n2 - Médio\n3 - Difícil')
    nivel = int(input('Digite o nível de dificuldade escolhido (1 a 3):'))

    while nivel not in [1, 2, 3]:
        nivel = int(input('Opção inválida!\nDigite o nível de dificuldade escolhido (1 a 3):'))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    elif nivel == 3:
        total_de_tentativas = 5

    pontos = 1000
    numero_secreto = rd.randint(1, 100)
    chute = 0
    acertou = False
    for tentativa in range(1, total_de_tentativas + 1):
        print('*****************\nTentativa {} de {}.'.format(tentativa, total_de_tentativas))
        chute = int(input('Digite um número entre 1 e 100:'))

        if (chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100.')
            continue

        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto
        acertou = chute == numero_secreto
        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos

        print(f'Você digitou {chute}.')
        if(chute_maior):
            print('Você errou! Seu chute foi maior que o número secreto.')
        elif(chute_menor):
            print('Você errou! Seu chute foi menor que o número secreto.')
        elif(acertou):
            print(f'Você acertou e fez {pontos} pontos!')
            break
    if not acertou:
        print(f'O número secreto era {numero_secreto}. Você fez {pontos} pontos.')

    jogos.func_fazer_agora(adivinhacao)



if (__name__ == '__main__'):
     main()