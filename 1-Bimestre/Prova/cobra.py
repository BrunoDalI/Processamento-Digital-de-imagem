

import pygame
from pygame.locals import *
import random
from sys import exit
from menu import *



# Posição inicial da cobra
x = 300
y = 300
# Tamanho do quadrado da cobra
d = 20


# Configurações da tela/janela
tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption('Snake crazy')




# Aplica o fundo do jogo
Fundo = pygame.image.load('img/fundo.png')


# Lista da cobra (é uma lista de lista para definir a longitude da cobra)
lista_cobra = [[x, y]]





dx = 0  # movimentação horizontal
dy = 0  # movimentação vertical


x_maca = (round(random.randrange(0, largura - 50) / 20) * 20)
y_maca = (round(random.randrange(0, altura - 50) / 20) * 20)


# para verificar se cobra morreu 
morreu = False


# Velocidade de atualização da tela 
clock = pygame.time.Clock()



# Desenha o corpo da cobra
def desenha_cobra(lista_cobra):
    # limpa a tela
    tela.blit(Fundo, (0,0))
    desenho = 1
    for unidade in lista_cobra:
        #pygame.draw.rect(tela, laranja, [unidade[0], unidade[1] , d, d])
        if desenho == 1:
            pygame.draw.circle(tela, (preto), (unidade[0], unidade[1]), d -10)
            pygame.draw.circle(tela, (verdeClaro), (unidade[0], unidade[1]), 8)
            pygame.draw.circle(tela, (azul), (unidade[0], unidade[1] + 6), 4)
            pygame.draw.circle(tela, (azul), (unidade[0], unidade[1] - 6), 4)
            desenho = 2
        elif desenho == 2:
            pygame.draw.circle(tela, (preto), (unidade[0], unidade[1]), d -10)
            pygame.draw.circle(tela, (verdeClaro), (unidade[0], unidade[1]), 8)
            pygame.draw.circle(tela, (vermelho), (unidade[0], unidade[1] + 6), 4)
            pygame.draw.circle(tela, (vermelho), (unidade[0], unidade[1] - 6), 4)
            desenho = 1




# Executa os movimentos da cobra
def mover_cobra(dx, dy, lista_cobra):
    # identifica quais teclas são clicadas
    for event in pygame.event.get():
       if event.type == QUIT:
            # para fechar a tela no x
            pygame.quit()
            exit()
       if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d

    x_novo = lista_cobra[-1][0] + dx
    y_novo = lista_cobra[-1][1] + dy

    lista_cobra.append([x_novo, y_novo])

    del lista_cobra[0]

    return dx, dy, lista_cobra




# Verifica se a cobra comeu a maça
def verifica_comida(dx, dy, x_maca, y_maca, lista_cobra):
    # musica quando come a maça
    musica_comeu = pygame.mixer.Sound('som/comeu.wav')

    macaFundo =  pygame.image.load('img/maca.png')
    
    # o head é o ultimo elemento da lista;
    head = lista_cobra[-1]

    x_novo = head[0] + dx
    y_novo = head[1] + dy

    if head[0] == x_maca and head[1] == y_maca:
        lista_cobra.append([x_novo, y_novo])
        x_maca= round(random.randrange(0, largura - 40) / 20) * 20
        y_maca = round(random.randrange(0, altura - 40) / 20) * 20
        musica_comeu.play()


    #pygame.draw.circle(tela, (laranja), (x_maca, y_maca), d-10)
    #pygame.draw.rect(tela, (vermelho), [x_comida, y_comida, d-2, d-2])
    tela.blit(macaFundo, (x_maca -27, y_maca - 27))
    return x_maca, y_maca, lista_cobra



# Verifica se a cobra ultrapassou as dimenssoes da tela
def verifica_obstaculo(lista_cobra):
    head = lista_cobra[-1]
    x = head[0]
    y = head[1]
    
    game_over = pygame.mixer.Sound('som/fim.wav')
    
    if (x not in range(680) or y not in range(500)):
        game_over.play()
        tela.fill((preto))
        # Fonte para mostrar as letras na tela
        fontefim = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Você ultrapassou o limite da tela'
        texto_formatado = fontefim.render(mensagem, True, branco)
        # para fechar a tela no x
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        tela.blit(texto_formatado, (170//2, altura//2)) # // para retornar um inteiro se não da erro
        pygame.display.update()




# Reinicia jogo
def reiniciar_jogo():
    global pts, llista_cobra,  dx, dy, x_maca, y_maca, morreu, x, y, x_novo, y_novo
    pts = 0
    lista_cobra = [[x, y]]
    lista_cobra = [[ ]]
    dx = 0
    dy = 0
    x = 0
    y = 0
    x_maca = (round(random.randrange(0, largura - 30) / 20) * 20)
    y_maca = (round(random.randrange(0, altura - 30) / 20) * 20)
    morreu = False



# Verifica se a cobra mordeu seu propio corpo
def verifica_mordeu(lista_cobra):
    head = lista_cobra[-1]
    corpo = lista_cobra.copy()
    del corpo[-1]
    for x, y in corpo:
        if x == head[0] and y == head[1]:
            morreu = True
            # mensagem = 'Game Over! Pressione a S para reiniciar'
            fontefim = pygame.font.SysFont('arial', 20, True, True)
            mensagem = 'Game Over! A cobra se mordeu'
            texto_formatado = fontefim.render(mensagem, True, preto)
            while morreu:
                #tela.fill((255,255,255))
                #reiniciar_jogo()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        # para fechar a tela no x
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                       if event.key == K_s:
                           reiniciar_jogo()
                tela.blit(texto_formatado, (300//2, altura//2)) # // para retornar um inteiro se não da erro
                pygame.display.update()

