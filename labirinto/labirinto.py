class Labirinto:
    def __init__(self, mapa):
        self.mapa = mapa
        self.linhas = len(mapa)
        self.colunas = len(mapa[0])

    def exibir(self):
        for linha in self.mapa:
            print("".join(linha))

    def posicao_valida(self, x, y):
        return 0 <= x < self.linhas and 0 <= y < self.colunas and self.mapa[x][y] != '#'