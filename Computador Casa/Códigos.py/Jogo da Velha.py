import pygame
import sys

pygame.init()

LARGURA, ALTURA = 300, 300
TAMANHO_CELULA = LARGURA // 3
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Velha")

tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
jogador_atual = "X"


def desenhar_tabuleiro():
    tela.fill(BRANCO)
    for i in range(1, 3):
        pygame.draw.line(tela, PRETO, (0, i * TAMANHO_CELULA), (LARGURA, i * TAMANHO_CELULA), 3)
        pygame.draw.line(tela, PRETO, (i * TAMANHO_CELULA, 0), (i * TAMANHO_CELULA, ALTURA), 3)
        

def desenhar_pecas():
    for i in range(3):
        for j in range(3):
            x = j * TAMANHO_CELULA + TAMANHO_CELULA // 2
            y = i * TAMANHO_CELULA + TAMANHO_CELULA // 2
            if tabuleiro[i][j] == "X":
                pygame.draw.line(tela, VERMELHO, (x - 50, y - 50), (x + 50, y + 50), 5)
                pygame.draw.line(tela, VERMELHO, (x + 50, y - 50), (x - 50, y + 50), 5)
            elif tabuleiro[i][j] == "O":
                pygame.draw.circle(tela, PRETO, (x, y), 50, 5)


def verificar_vitoria():
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] != " ":
            return linha[0]
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] != " ":
            return tabuleiro[0][col]
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return tabuleiro[0][2]
    return None


def verificar_empate():
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True


def reiniciar_jogo():
    global tabuleiro, jogador_atual
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"


# Loop principal do jogo
rodando = True
while rodando:
    desenhar_tabuleiro()
    desenhar_pecas()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            linha = y // TAMANHO_CELULA
            coluna = x // TAMANHO_CELULA
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = jogador_atual
                vencedor = verificar_vitoria()
                if vencedor:
                    print(f"Jogador {vencedor} venceu!")
                    reiniciar_jogo()
                elif verificar_empate():
                    print("Empate!")
                    reiniciar_jogo()
                else:
                    jogador_atual = "O" if jogador_atual == "X" else "X"

    pygame.display.update()

pygame.quit()
sys.exit()
