import pygame
import random

# cores RGB
preta = (0, 0, 0)
branco = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

# parametros da cobrinha
tamanho_quadrado = 20

def gerar_comida(largura, altura):
    # gera uma posição aleatória para a comida dentro dos limites da janela, garantindo que a comida apareça em um local válido
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y

def desenhar_comida(tela, tamanho, comida_x, comida_y):
    # desenha um retângulo vermelho representando a comida
    pygame.draw.rect(tela, vermelha, [comida_x, comida_y, tamanho, tamanho]) 

def desenhar_cobra(tela, tamanho, pixels):
    # desenha a cobrinha usando os pixels armazenados na lista, cada pixel é um retângulo verde
    for pixel in pixels:
        pygame.draw.rect(tela, verde, [pixel[0], pixel[1], tamanho, tamanho])
        
def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    else:
        velocidade_x = 0
        velocidade_y = 0

    return velocidade_x, velocidade_y

def desenhar_pontuacao(tela, pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 30) # define a fonte e o tamanho do texto
    texto = fonte.render(f"Pontos: {pontuacao}", True, branco) # renderiza o texto da pontuação, o segundo argumento é para ativar a suavização do texto e o terceiro é a cor do texto
    tela.blit(texto, [10, 10]) # desenha o texto na tela, o segundo argumento é a posição do texto
