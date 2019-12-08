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
from genetic import Genetic

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
fontSize = 32
myfont = pygame.font.Font('assets/lobster.ttf', fontSize)
stringPlayer = myfont.render('Sua Vez!', False, (0, 0, 0))
stringMachine = myfont.render('Aguarde...', False, (0, 0, 0))
string1stage = myfont.render('1º Estágio', False, (0, 0, 0))
string2stage = myfont.render('2º Estágio', False, (0, 0, 0))
string3stage = myfont.render('3º Estágio', False, (0, 0, 0))

# API controller - (GAME)
table = Controller()

# API genentic
gene = Genetic()

# número pra desenhar fora da tela
numOutScreen = -100
 
# Controle de click inválido
nullMove = -1

# render mark
def renderMark():
    position = table.getMark(mouse_x, mouse_y)
    beFree = gene.getChromosome()[position] == 0
    playerHere = gene.getChromosome()[position] == 1

    if table.stage1 and table.match(mouse_x, mouse_y) and beFree:
        mark['x'] = table.getX(mouse_x)
        mark['y'] = table.getY(mouse_y)

    elif table.stage2 and table.match(mouse_x, mouse_y) and playerHere:
        mark['x'] = table.getX(mouse_x)
        mark['y'] = table.getY(mouse_y)

    elif table.stage2 and table.match(mouse_x, mouse_y) and playerHere:
        pass

    else:
        mark['x'] = numOutScreen
        mark['y'] = numOutScreen

# render peças
def render(qtd_pieces, pieces):
    diff = 35

    for i in range(0, qtd_pieces):
        if pieces[i] == 1:
            position = table.getXY(i)
            screen.blit(red['img'], (position[0]-diff, position[1]-diff))
        
        elif pieces[i] == 2:
            position = table.getXY(i)
            screen.blit(dark['img'], (position[0]-diff, position[1]-diff))

# Define em qual estágio o jogo se encontra
def setState():
    qtdPlayer = gene.getQtdPiecesPlayer()
    qtdMachine = gene.getQtdPiecesMachine()

    if qtdPlayer < 9 and qtdMachine < 9:
        table.stage1 = True
        table.stage2 = False
        table.stage3 = False

    elif qtdPlayer <= 3 or qtdMachine <= 3: 
        table.stage1 = False
        table.stage2 = False
        table.stage3 = True
    else :
        table.stage1 = False
        table.stage2 = True
        table.stage3 = False

# Ação efetiva do jogo
def actionGame():
    if table.stage1:
        position = table.getMark(mouse_x, mouse_y)
        beFree = gene.getChromosome()[position] == 0

        if beFree:
            gene.setPositionPlayer(position)
            gene.setPositionMachine1stage()

    if table.stage2:
        position = table.getMark(mouse_x, mouse_y)
        playerHere = gene.getChromosome()[position] == 1

        if playerHere:
            gene.removePiece(position)


# flag de controle do jogo
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    mouse = mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    
    if mouse_click != (0,0,0) :
        marker = table.getMark(mouse_x, mouse_y) 
        print(mouse, ' -> ', marker)
        
        if marker != nullMove: actionGame()

    screen.blit(tabuleiro, (0,0))

    # função que renderiza as peças do jogo
    render(gene.getSizeChromosome(), gene.getChromosome())
    # render(24, gene.getChromosome())
    
    # função que renderiza o marcador
    renderMark()

    # definir estágio do jogo
    setState()

    if table.isTrailPlayer(gene.getChromosome()): print("Trilha Player!!")
    if table.isTrailMachine(gene.getChromosome()): print("Trilha Machine!!")

    screen.blit(mark['img'], (mark['x'], mark['y']))
    screen.blit(stringPlayer,(tabuleiro.get_width()-200, 35))

    if table.stage1: screen.blit(string1stage,(tabuleiro.get_width()-200, 100))
    elif table.stage2: screen.blit(string2stage,(tabuleiro.get_width()-200, 100))
    else: screen.blit(string3stage,(tabuleiro.get_width()-200, 100))
    
    pygame.display.flip()