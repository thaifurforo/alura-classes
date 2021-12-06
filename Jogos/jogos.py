import adivinhacao
import forca
import jogos

def main():
    print('******************\nEscolha o seu jogo!\n******************')
    print('1 - Forca\n2 - Adivinhação')

    jogo = int(input('Escolha um jogo:'))
    if (jogo == 1):
        print('Jogando forca.')
        forca.main()
    elif (jogo == 2):
        print('Jogando adivinhação.')
        adivinhacao.main()
    else:
        while jogo not in [1, 2]:
            jogo = int(input('Opção inválida! Escolha um jogo:'))

def func_fazer_agora(jogo_escolhido):
    print('Fim de jogo.\n'
          'O que você gostaria de fazer agora?\n'
          '1 - Nova partida\n'
          '2 - Retornar ao menu principal\n'
          '3 - Sair')
    fazer_agora = int(input())
    if (fazer_agora == 1):
        jogo_escolhido.main()
    elif (fazer_agora == 2):
        main()
    elif (fazer_agora == 3):
        pass
    else:
        while fazer_agora not in [1, 2, 3]:
            print('Opção inválida.\n'
                  'O que você gostaria de fazer agora?\n'
                  '1 - Nova partida\n'
                  '2 - Retornar ao menu principal\n'
                  '3 - Sair')
            fazer_agora = int(input())

if (__name__ == '__main__'):
     main()