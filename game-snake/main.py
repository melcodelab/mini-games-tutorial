import pygame
from game import gerar_comida, desenhar_comida, desenhar_cobra, selecionar_velocidade, desenhar_pontuacao, tamanho_quadrado, preta

pygame.init() # inicializando o pygame
pygame.display.set_caption("Jogo da Cobrinha 🐍") # Nomeando a janela que abre o jogo 
largura, altura = 1000, 800 # tamanho da janela que abre o jogo
tela = pygame.display.set_mode((largura, altura)) # cria uma janela com as dimensões definidas
relogio = pygame.time.Clock() # controla a velocidade que o jogo roda

# parametros da cobrinha
velocidade_cobra = 15

# criar um loop infinito para manter o jogo executando
def executar_jogo():
    fim_de_jogo = False

    x = largura / 2 # posição inicial da cobrinha no eixo x
    y = altura / 2 # posição inicial da cobrinha no eixo y

    # cobrinha comeca parada
    velocidade_x = 0 # velocidade inicial da cobrinha no eixo x
    velocidade_y = 0 # velocidade inicial da cobrinha no eixo y

    tamanho_cobra = 1 # tamanho inicial da cobrinha
    pixels = [] # lista para armazenar os pixels da cobrinha

    comida_x, comida_y = gerar_comida(largura, altura) # posição inicial da comida

    while not fim_de_jogo:
        tela.fill(preta) # preenche a tela com a cor preta

        for evento in pygame.event.get(): # pega cada evento dentro do jogo, como o clique de um botão ou o fechamento da janela
            if evento.type == pygame.QUIT: # se o evento for o fechamento da janela, o jogo termina
                fim_de_jogo = True
            elif evento.type == pygame.KEYDOWN: # se o evento for o pressionamento de uma tecla, verifica qual tecla foi pressionada
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key) # chama a função para selecionar a velocidade da cobrinha com base na tecla pressionada


        # chama a função para desenhar a comida na tela
        desenhar_comida(tela, tamanho_quadrado, comida_x, comida_y) 

        # atualiza a posição da cobrinha com base na velocidade
        if x < 0 or x >= largura or y < 0 or y >= altura: # verifica se a cobrinha bateu na parede, comparando a posição da cabeça da cobrinha com os limites da janela
            fim_de_jogo = True # se a cobrinha bater na parede, o jogo termina

        x += velocidade_x
        y += velocidade_y

        # desenhar a cobrinha
        pixels.append([x, y]) 
        # mantém a lista de pixels com o tamanho da cobrinha, removendo os pixels mais antigos
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        for pixel in pixels[:-1]: # verifica se a cobrinha bateu em si mesma, comparando cada pixel com a posição da cabeça da cobrinha (último pixel)
            if pixel == [x, y]:
                fim_de_jogo = True # se a cobrinha bater em si mesma, o jogo termina
        
        desenhar_cobra(tela, tamanho_quadrado, pixels) # chama a função para desenhar a cobrinha na tela
        desenhar_pontuacao(tela, tamanho_cobra - 1) # chama a função para desenhar a pontuação na tela, a pontuação é o tamanho da cobrinha menos 1 (pois começa com tamanho 1)
        

        # atualização da tela
        pygame.display.update()

        # criar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1 # aumenta o tamanho da cobrinha
            comida_x, comida_y = gerar_comida(largura, altura) # gera uma nova posição para a comida

        relogio.tick(velocidade_cobra) # controla a velocidade do jogo

if __name__ == "__main__":
    executar_jogo()