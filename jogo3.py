import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definição de variáveis
width, height = 800, 600
ball = pygame.Rect(width/2 - 15, height/2 - 15, 30, 30)
player = pygame.Rect(width - 20, height/2 - 60, 10, 120)
opponent = pygame.Rect(10, height/2 - 60, 10, 120)
bg_color = (0, 0, 0)
light_grey = (200, 200, 200)
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0

# Configuração da tela
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed = 7
            if event.key == pygame.K_UP:
                player_speed = -7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player_speed = 0

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= height:
        player.bottom = height

    # Desenhar elementos na tela
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (width/2, 0), (width/2, height))

    pygame.display.flip()
