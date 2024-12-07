# jogador.py
class Jogador:
    def __init__(self, labirinto):
        self.labirinto = labirinto
        self.x, self.y = self.encontrar_posicao_inicial()

    def encontrar_posicao_inicial(self):
        BLUE = "\033[34m"
        RESET = "\033[0m"
        player_symbol = '@'
        colored_player = BLUE + player_symbol + RESET
        
        for i in range(self.labirinto.linhas):
            for j in range(self.labirinto.colunas):
                if self.labirinto.mapa[i][j] == player_symbol or self.labirinto.mapa[i][j] == colored_player:
                    return i, j
        return None, None

    def mover(self, direcao):
        dx, dy = 0, 0
        if direcao == 'w':
            dx = -1
        elif direcao == 's':
            dx = 1
        elif direcao == 'a':
            dy = -1
        elif direcao == 'd':
            dy = 1

        novo_x, novo_y = self.x + dx, self.y + dy
        if self.labirinto.posicao_valida(novo_x, novo_y):
            # Guarda o caractere atual da nova posição
            destino = self.labirinto.mapa[novo_x][novo_y]
            
            # Move o jogador com a cor
            BLUE = "\033[34m"
            RESET = "\033[0m"
            self.labirinto.mapa[self.x][self.y] = ' '
            self.x, self.y = novo_x, novo_y
            self.labirinto.mapa[self.x][self.y] = BLUE + '@' + RESET
            
            # Verifica se chegou ao 'x'
            return 'x' in destino
        return False