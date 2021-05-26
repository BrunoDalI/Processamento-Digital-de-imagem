


from cobra import *



pygame.init()




# Calcula os pontos das jogadas
def pontos(lista_cobra):
    pts = str(len(lista_cobra) -1)
    fonte = pygame.font.SysFont("hack", 30, True, False)
    escore = fonte.render(f'Score: ' + pts, True, preto)
    tela.blit(escore, [0, 0])


    

while True:
    pygame.display.update()
    desenha_cobra(lista_cobra)
    # passa as novas coordenadas para atualizar a movimentação
    dx, dy, lista_cobra = mover_cobra(dx, dy, lista_cobra)
    x_maca, y_maca, lista_cobra = verifica_comida(dx, dy, x_maca, y_maca, lista_cobra)

    verifica_obstaculo(lista_cobra)
    verifica_mordeu(lista_cobra)
    pontos(lista_cobra)

   # velocidade da cobra 
    clock.tick(10)



    
