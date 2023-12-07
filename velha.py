def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, simbolo):
    # Verificar linhas e colunas
    for i in range(3):
        if all([tabuleiro[i][j] == simbolo for j in range(3)]) or all([tabuleiro[j][i] == simbolo for j in range(3)]):
            return True

    # Verificar diagonais
    if all([tabuleiro[i][i] == simbolo for i in range(3)]) or all([tabuleiro[i][2 - i] == simbolo for i in range(3)]):
        return True

    return False

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador = "X"
    jogo_em_andamento = True

    while jogo_em_andamento:
        exibir_tabuleiro(tabuleiro)

        linha = int(input(f"Jogador {jogador}, escolha a linha (0, 1, 2): "))
        coluna = int(input(f"Jogador {jogador}, escolha a coluna (0, 1, 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador

            if verificar_vitoria(tabuleiro, jogador):
                exibir_tabuleiro(tabuleiro)
                print(f"Parabéns, jogador {jogador} venceu!")
                jogo_em_andamento = False
            else:
                if all([c != " " for linha in tabuleiro for c in linha]):
                    exibir_tabuleiro(tabuleiro)
                    print("Empate!")
                    break

                jogador = "O" if jogador == "X" else "X"
        else:
            print("Posição ocupada. Escolha novamente.")

jogo_da_velha()
