import os
import time
import keyboard
from labirinto import Labirinto
from jogador import Jogador

def main():
    RED = "\033[31m"
    RESET = "\033[0m"

    mapas = [
        [
            list("############################"),
            list("#@       #                 #"),
            list("# #####  # ### # ######### #"),
            list("#     #  # #   #       #   #"),
            list("### # #### # ######### # ###"),
            list("#   #      #     #     #   #"),
            list("# ########## ### # #########"),
            list("#            #   #        x#"),
            list("############################")
        ],
        [
            list("#############################################"),
            list("#@     #             #                      #"),
            list("# ###  ####### # ### # ########### ######## #"),
            list("# #    #       # #   #       #       #    # #"),
            list("# # #### ###   # # ######### # ##### # ## # #"),
            list("# #      # #   # #       #   #     # #  # # #"),
            list("# ######## #   # ######### # ##### # #### # #"),
            list("#          # # #           #       #      #x#"),
            list("#############################################")
        ],
        [
            list("####################################################"),
            list("#@         #                   #                 # #"),
            list("# ######## # ###### ########## # ################# #"),
            list("#        # #      #          # #                 # #"),
            list("######## # ###### ########## # ################# # #"),
            list("#        #        #          #                   # #"),
            list("# ######################### ############### ###### #"),
            list("#                      #                  #       x#"),
            list("####################################################")
        ]
    ]

    # Colorir o 'x' em todo jogo.
    def colorize_map(map):
        return [[RED + cell + RESET if cell == 'x' else "\033[34m" + cell + RESET if cell == '@' else cell for cell in row] for row in map]

    mapas = [colorize_map(mapa) for mapa in mapas]

    for nivel, mapa in enumerate(mapas, start=1):
        print(f"Nivel {nivel}")
        labirinto = Labirinto(mapa)
        jogador = Jogador(labirinto)

        while True:
            #Limpando a tela
            if os.name == 'nt':  # Para Windows
                os.system('cls')
            else:  # Para sistemas Unix (Linux/Mac)
                os.system('clear')

            #Exibindo labirinto e pegando input do usuario
            labirinto.exibir()
            if keyboard.is_pressed('w'):
                if jogador.mover('w'):
                    print("Você completou o nível!")
                    time.sleep(1)  # Pausa para mostrar a mensagem
                    break
            elif keyboard.is_pressed('s'):
                if jogador.mover('s'):
                    print("Você completou o nível!")
                    time.sleep(1)
                    break
            elif keyboard.is_pressed('a'):
                if jogador.mover('a'):
                    print("Você completou o nível!")
                    time.sleep(1)
                    break
            elif keyboard.is_pressed('d'):
                if jogador.mover('d'):
                    print("Você completou o nível!")
                    time.sleep(1)
                    break
            time.sleep(0.1)  # Nao printar muito rapido
            if jogador.x == labirinto.linhas - 1 and jogador.y == labirinto.colunas - 1:
                print("Você completou o nível!")
                break

    print("Seus movimentos:")

if __name__ == "__main__":
    main()