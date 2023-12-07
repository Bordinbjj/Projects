import random

def criar_tabuleiro(linhas, colunas, bombas):
    tabuleiro = [[' ' for _ in range(colunas)] for _ in range(linhas)]
    bombas_plantadas = 0
    while bombas_plantadas < bombas:
        x = random.randint(0, linhas - 1)
        y = random.randint(0, colunas - 1)
        if tabuleiro[x][y] != '*':
            tabuleiro[x][y] = '*'
            bombas_plantadas += 1
    return tabuleiro

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))

def contar_bombas_vizinhas(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == '*':
        return '*'

    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])
    bombas_vizinhas = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            nova_linha = linha + i
            nova_coluna = coluna + j
            if (0 <= nova_linha < linhas and 0 <= nova_coluna < colunas and tabuleiro[nova_linha][nova_coluna] == '*'):
                bombas_vizinhas += 1

    if bombas_vizinhas > 0:
        return str(bombas_vizinhas)
    return ' '

def revelar_celula(tabuleiro, tabuleiro_mostrado, linha, coluna):
    if 0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0]):
        if tabuleiro_mostrado[linha][coluna] == ' ':
            tabuleiro_mostrado[linha][coluna] = contar_bombas_vizinhas(tabuleiro, linha, coluna)
            if tabuleiro_mostrado[linha][coluna] == ' ':
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        revelar_celula(tabuleiro, tabuleiro_mostrado, linha + i, coluna + j)

def jogar():
    linhas = 5
    colunas = 5
    bombas = 5

    tabuleiro = criar_tabuleiro(linhas, colunas, bombas)
    tabuleiro_mostrado = [[' ' for _ in range(colunas)] for _ in range(linhas)]

    while True:
        mostrar_tabuleiro(tabuleiro_mostrado)

        linha = int(input('Digite o número da linha: '))
        coluna = int(input('Digite o número da coluna: '))

        if tabuleiro[linha][coluna] == '*':
            print('Você perdeu!')
            print('Tabuleiro final:')
            mostrar_tabuleiro(tabuleiro)
            break
        else:
            revelar_celula(tabuleiro, tabuleiro_mostrado, linha, coluna)

        celulas_restantes = sum(row.count(' ') for row in tabuleiro_mostrado)
        if celulas_restantes == bombas:
            print('Parabéns! Você ganhou!')
            break

if __name__ == "__main__":
    jogar()


