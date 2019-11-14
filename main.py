'''
Trabalho Final da Disciplina de processos estocásticos
@author Micael Gomes
@author Saúl Milú

Jogo Trilha/Moinho 
Abordagem Genética para simular um oponente

cromossomo -> jogada atual, simulada por um matriz
'''

import sys, pygame
from controller import Controller
from genetic import getChromosome

# Iniciando o jogo e definindo título da Janela
pygame.init()

# Definindo Icone do Jogo
icon = pygame.image.load('assets/ico.png')
pygame.display.set_icon(icon)

# Propriedades da janela
size = width, height = 810, 600
screen = pygame.display.set_mode(size)

# imagem do tabuleiro
# tabuleiro = pygame.image.load('assets/tab.png')
if len(sys.argv) > 1:
    pygame.display.set_caption('Trilha - debug mode')
    tabuleiro = pygame.image.load('assets/tab_mark.png')
else:
    pygame.display.set_caption('Trilha')
    tabuleiro = pygame.image.load('assets/tab.png')
    
# objetos do jogo: marcador, peça situação e oposiçãos
mark = {'img': pygame.image.load('assets/mark.png'), 'x': -30, 'y': -30}
red  = {'img': pygame.image.load('assets/red.png'), 'x': -60, 'y': -60}
dark = {'img': pygame.image.load('assets/dark.png'), 'x': -60, 'y': -60}

# estilo do jogo
fontSize = 40
myfont = pygame.font.Font('assets/lobster.ttf', fontSize)
stringPlayer = myfont.render('Sua Vez!', False, (0, 0, 0))
stringMachine = myfont.render('Aguarde...', False, (0, 0, 0))

# Tabela de match points
# controlador de turnos
table = Controller()

# O player começa
table.turnPlayer = True

# número pra desenhar fora da tela
numOutScreen = -100

# render mark
def renderMark():
    positionNotFree = table.getMark(mouse_x, mouse_y)
    beFree = getChromosome()[positionNotFree] != 0 
    print('beFree -> ', beFree, 'pos -- ', positionNotFree)

    if table.match(mouse_x, mouse_y) and beFree:
        mark['x'] = table.getX(mouse_x)
        mark['y'] = table.getY(mouse_y)

    else:
        mark['x'] = numOutScreen
        mark['y'] = numOutScreen

# render peças
def render(qtd_pieces, pieces):
    diff = 35

    for i in range(qtd_pieces):
        if pieces[i] == 1:
            position = table.getMarkPosition(i+1)
            screen.blit(red['img'], (position[0]-diff, position[1]-diff))
        
        elif pieces[i] == 2:
            position = table.getMarkPosition(i+1)
            screen.blit(dark['img'], (position[0]-diff, position[1]-diff))


# flag de controle do jogo
run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    mouse = mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    
    if mouse_click != (0,0,0) : 
        print(mouse, ' -> ', table.getMark(mouse_x, mouse_y))

    screen.blit(tabuleiro, (0,0))

    # função que renderiza as peças do jogo
    render(27, getChromosome())
    
    # função que renderiza o marcador
    renderMark()

    screen.blit(mark['img'], (mark['x'], mark['y']))
    screen.blit(stringPlayer,(tabuleiro.get_width()-200, 35))
    pygame.display.flip()