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
import time

# Iniciando o jogo e definindo título da Janela
pygame.init()
pygame.display.set_caption('Trilha')

# tempo inicial
deltaTime = int(round(time.time() * 1000)) 

# Definindo Icone do Jogo
icon = pygame.image.load('assets/ico.png')
pygame.display.set_icon(icon)

# Propriedades da janela
size = width, height = 810, 600
screen = pygame.display.set_mode(size)

# imagem do tabuleiro
# tabuleiro = pygame.image.load('assets/tab.png')
if len(sys.argv) > 1:
    tabuleiro = pygame.image.load('assets/tab_mark.png')
else:
    tabuleiro = pygame.image.load('assets/tab.png')
    
# objetos do jogo: marcador, peça situação e oposiçãos
red  = {'img': pygame.image.load('assets/red.png'), 'x': -60, 'y': -60}
dark = {'img': pygame.image.load('assets/dark.png'), 'x': -60, 'y': -60}
mark = {'img': pygame.image.load('assets/mark.png'), 'x': -30, 'y': -30}

# estilo do jogo
myfont = pygame.font.SysFont('assests/modak.ttf', 30)
stringPlayer = myfont.render('Sua Vez!', False, (0, 0, 0))
stringMachine = myfont.render('Aguarde...', False, (0, 0, 0))

# Tabela de match points
# controlador de turnos
table = Controller()

# O player começa
table.turnPlayer = True

# número pra desenhar fora da tela
numOutScreen = -30

# flag de controle do jogo
run = True

while run:
    
    # atualizando o tempo
    deltaTime = int(round(time.time() * 1000)) - deltaTime

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    mouse = mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if mouse_click != (0,0,0) and deltaTime > 1000000: 
        print(mouse, ' -> ', table.getMark(mouse_x, mouse_y))

        deltaTime = 0

        if table.turnPlayer:
            red['x'] = table.getX(mouse_x) - 20 
            red['y'] = table.getY(mouse_y) - 20 
        else:
            dark['x'] = table.getX(mouse_x) - 20    
            dark['y'] = table.getY(mouse_y) - 20    

        table.turnPlayer = not table.turnPlayer
        table.turnMachine = not table.turnMachine

    if table.match(mouse_x, mouse_y):
        mark['x'] = table.getX(mouse_x)
        mark['y'] = table.getY(mouse_y)

    else:
        mark['x'] = numOutScreen
        mark['y'] = numOutScreen

    screen.blit(tabuleiro, (0,0))
    
    if table.turnPlayer:
        screen.blit(stringPlayer,(tabuleiro.get_width()-150, 50))
    else:
        screen.blit(stringMachine,(tabuleiro.get_width()-150, 50))

    screen.blit(mark['img'], (mark['x'], mark['y']))
    screen.blit(red['img'], (red['x'], red['y']))
    screen.blit(dark['img'], (dark['x'], dark['y']))
    
    pygame.display.flip()