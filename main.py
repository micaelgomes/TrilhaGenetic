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
pygame.mixer.init() 
pygame.mixer.music.load('assets/music.mp3')

# Definindo Icone do Jogo
icon = pygame.image.load('assets/ico.png')
pygame.display.set_icon(icon)

# Propriedades da janela
size = width, height = 810, 600
screen = pygame.display.set_mode(size)

# imagem do tabuleiro
# tabuleiro = pygame.image.load('assets/tab.png')
if len(sys.argv) > 1:
    if sys.argv[1] == "--debug" or sys.argv[1] == "-d":
        pygame.display.set_caption('Trilha - debug mode')
        tabuleiro = pygame.image.load('assets/tab_mark.png')
        win = pygame.image.load('assets/win.png')
        loser = pygame.image.load('assets/loser.png')
    else:
        print('Flag ERROR: try --help to see more')
else:
    pygame.display.set_caption('Trilha')
    tabuleiro = pygame.image.load('assets/tab.png')
    win = pygame.image.load('assets/win.png')
    loser = pygame.image.load('assets/loser.png')
    
# objetos do jogo: marcador, peça situação e oposiçãos
mark = {'img': pygame.image.load('assets/mark.png'), 'x': -30, 'y': -30}
big_mark = {'img': pygame.image.load('assets/big_mark.png'), 'x': -30, 'y': -30}
close = {'img': pygame.image.load('assets/close.png'), 'x': -40, 'y': -40}
kill = {'img': pygame.image.load('assets/kill.png'), 'x': -200, 'y': -200}
rip = {'img': pygame.image.load('assets/rip.png'), 'x': -200, 'y': -200}
red  = {'img': pygame.image.load('assets/red.png'), 'x': -60, 'y': -60}
dark = {'img': pygame.image.load('assets/dark.png'), 'x': -60, 'y': -60}

# estilo do jogo
fontSize = 32
myfont = pygame.font.Font('assets/lobster.ttf', fontSize)
stringPlayer = myfont.render('Sua Vez!', False, (0, 0, 0))
stringMachine = myfont.render('Aguarde...', False, (0, 0, 0))

# strings de Stages
string1stage = myfont.render('1º Estágio', False, (0, 0, 0))
string2stage = myfont.render('2º Estágio', False, (0, 0, 0))
string3stage = myfont.render('3º Estágio', False, (0, 0, 0))

# API controller - (GAME)
table = Controller()

# API genentic
gene = Genetic()

# número pra desenhar fora da tela
numOutScreen = -200
 
# Controle de click inválido
nullMove = -1

# render mark
def renderMark():

    if table.playerTurn and not table.executeOrder66:
        position = table.getMark(mouse_x, mouse_y)
        beFree = gene.getChromosome()[position] == 0
        playerHere = gene.getChromosome()[position] == 1
        neighborFree = False
        
        if position != nullMove:
            neighbor = table.getNeighbor(position)
            for i in range(len(neighbor)):
                if gene.getChromosome()[neighbor[i]] == 0:
                    neighborFree = True

        if table.stage1_player and table.match(mouse_x, mouse_y) and beFree:
            mark['x'] = table.getX(mouse_x)
            mark['y'] = table.getY(mouse_y)

        elif table.stage2_player and table.match(mouse_x, mouse_y) and playerHere and neighborFree:
            mark['x'] = table.getX(mouse_x)
            mark['y'] = table.getY(mouse_y)

        elif table.stage3_player and table.match(mouse_x, mouse_y) and playerHere:
            mark['x'] = table.getX(mouse_x)
            mark['y'] = table.getY(mouse_y)

        else:
            mark['x'] = numOutScreen
            mark['y'] = numOutScreen

    else:
        position = table.getMark(mouse_x, mouse_y)
        hasOponent = gene.getChromosome()[position] == 2

        if table.stage1_player and table.match(mouse_x, mouse_y) and hasOponent:
            close['x'] = table.getX(mouse_x) - 10
            close['y'] = table.getY(mouse_y) - 10

        elif table.stage2_player and table.match(mouse_x, mouse_y) and hasOponent:
            close['x'] = table.getX(mouse_x) - 10
            close['y'] = table.getY(mouse_y) - 10

        elif table.stage3_player and table.match(mouse_x, mouse_y) and hasOponent:
            close['x'] = table.getX(mouse_x) - 10
            close['y'] = table.getY(mouse_y) - 10

        else:
            close['x'] = numOutScreen
            close['y'] = numOutScreen

def removeMark():
    close['x'] = numOutScreen
    close['y'] = numOutScreen
    mark['x'] = numOutScreen
    mark['y'] = numOutScreen

# render peças
def render(qtd_pieces, pieces, clone):
    diff = 35

    for i in range(0, qtd_pieces):
        if pieces[i] == 1:
            position = table.getXY(i)
            screen.blit(red['img'], (position[0]-diff, position[1]-diff))
        
        elif pieces[i] == 2:
            position = table.getXY(i)
            screen.blit(dark['img'], (position[0]-diff, position[1]-diff))

        elif clone[i] == 3:
            position = table.getXY(i)
            screen.blit(big_mark['img'], (position[0]-diff, position[1]-diff))

# Define em qual estágio o jogo se encontra
def setState():
    qtdPlayer = gene.getQtdPiecesPlayer()
    qtdMachine = gene.getQtdPiecesMachine()
    machinePassed1Stage = False

    # variável de teste de fase 
    # table.passed1Stage = True

    if gene.qtdFixedPlayer <= 9 and not table.passed1Stage:
        table.stage1_player = True
        table.stage2_player = False
        table.stage3_player = False

    elif gene.qtdFixedPlayer > 9:
        table.passed1Stage = True

    if gene.qtdFixedMachine <= 9 and not table.passed1Stage:
        table.stage1_machine = True
        table.stage2_machine = False
        table.stage3_machine = False
    elif gene.qtdFixedMachine > 9:
        machinePassed1Stage = True

    if qtdPlayer <= 3 and table.passed1Stage: 
        table.stage1_player = False
        table.stage2_player = False
        table.stage3_player = True

    if qtdMachine <= 3 and table.passed1Stage:
        table.stage1_machine = False
        table.stage2_machine = False
        table.stage3_machine = True
    
    if not (qtdPlayer <= 3) and table.passed1Stage: 
        table.stage1_player = False
        table.stage2_player = True
        table.stage3_player = False

    if not (qtdMachine <= 3) and machinePassed1Stage:
        table.stage1_machine = False
        table.stage2_machine = True
        table.stage3_machine = False


    print('player-',table.stage1_player, table.stage2_player, table.stage3_player)
    print('machine-',table.stage1_machine, table.stage2_machine, table.stage3_machine)

# Ação efetiva do jogo (player)
def actionGame():

    if not table.executeOrder66:
        # Controle de ação do Player
        if table.playerTurn:
            if table.stage1_player:
                position = table.getMark(mouse_x, mouse_y)
                beFree = gene.getChromosome()[position] == 0

                if beFree:
                    gene.setPositionPlayer(position)
                    if gene.qtdFixedPlayer <= 9:
                        gene.qtdFixedPlayer += 1
                    removeMark()
                    table.playerTurn = False

            if table.stage2_player:
                position = table.getMark(mouse_x, mouse_y)
                playerHere = gene.getChromosome()[position] == 1
                freePositionToGo = gene.getClone()[position] == 3
                neighborFree = False
            
                if position != nullMove:
                    neighbor = table.getNeighbor(position)
                    for i in range(len(neighbor)):
                        if gene.getChromosome()[neighbor[i]] == 0:
                            neighborFree = True

                if playerHere and neighborFree:
                    gene.removePiecePlayer(position)
                    neighbor = table.getNeighbor(position)

                    for i in range(len(neighbor)):
                        if gene.getChromosome()[neighbor[i]] == 0:
                            gene.setPossibleMovePlayer(neighbor[i])

                if freePositionToGo:
                    gene.setPositionPlayer(position)
                    removeMark()
                    gene.resetClone()
                    table.playerTurn = False

            if table.stage3_machine:
                position = table.getMark(mouse_x, mouse_y)
                playerHere = gene.getChromosome()[position] == 1
                freePositionToGo = gene.getClone()[position] == 3

                if playerHere :
                    gene.removePiecePlayer(position)
                    chromosome = gene.getChromosome()

                    for i in range(gene.getSizeChromosome()):
                        if position != i:
                            if gene.getChromosome()[chromosome[i]] == 0:
                                gene.setPossibleMovePlayer(i)

                if freePositionToGo:
                    gene.setPositionPlayer(position)
                    removeMark()
                    gene.resetClone()
                    table.playerTurn = False

    
    else:
        position = table.getMark(mouse_x, mouse_y)
        hasOponent = gene.getChromosome()[position] == 2

        if hasOponent:
            gene.kill1PieceMachine(position)
            table.executeOrder66 = False
            removeMark()

# Ação efetiva do jogo (machine)
def machineAction():
    if not table.playerTurn: 
        if table.stage1_machine:
            gene.setPositionMachine1stage()
            if gene.qtdFixedMachine <= 9:
                gene.qtdFixedMachine += 1
            table.playerTurn = True

        if table.stage2_machine:
            gene.setPositionMachine2stage()
            table.playerTurn = True

        if table.stage3_machine:
            gene.setPositionMachine3stage()
            table.playerTurn = True

# flags de controles do jogo
run = True
canMoove = True
last_frame_move = pygame.time.get_ticks()
timeToClick = 0.500
pygame.mixer.music.play()
finish = False

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    mouse = mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if mouse_click != (0,0,0) and canMoove:
        marker = table.getMark(mouse_x, mouse_y) 
        print(mouse, ' -> ', marker)
        
        canMoove = False
        last_frame_move = pygame.time.get_ticks()

        if marker != nullMove: actionGame()
        
    machineAction()
    now_frame = pygame.time.get_ticks()
    delta = (now_frame - last_frame_move) / 1000.0

    if delta >= timeToClick and canMoove == False:
        canMoove = True

    if gene.getQtdPiecesPlayer() < 3 and table.passed1Stage:
        gene.resetChromosome()
        screen.blit(loser, (0,0))
        
    elif gene.getQtdPiecesMachine() < 3 and table.passed1Stage:
        gene.resetChromosome()
        screen.blit(win, (0,0))
    else:
        screen.blit(tabuleiro, (0,0))
    
    # função que renderiza as peças do jogo 
    render(gene.getSizeChromosome(), gene.getChromosome(), gene.getClone())

    # função que renderiza o marcador
    renderMark()

    # definir estágio do jogo
    setState()

    if table.isTrailPlayer(gene.getChromosome()): 
        print("Trilha Player!!")
        table.executeOrder66 = True
    if table.isTrailMachine(gene.getChromosome()): 
        print("Trilha Machine!!")
        gene.removePieceMachine()

    # checagem de trilha dupla
    table.disolveTrail(gene.getChromosome())

    screen.blit(mark['img'], (mark['x'], mark['y']))
    screen.blit(close['img'], (close['x'], close['y']))
    screen.blit(kill['img'], (kill['x'], kill['y']))

    if table.playerTurn and not finish: screen.blit(stringPlayer,(tabuleiro.get_width()-200, 35))
    elif not table.playerTurn and not finish: screen.blit(stringMachine,(tabuleiro.get_width()-200, 35))

    if table.stage1_player and not finish: screen.blit(string1stage,(tabuleiro.get_width()-200, 100))
    elif table.stage2_player and not finish: screen.blit(string2stage,(tabuleiro.get_width()-200, 100))
    elif table.stage3_player and not finish: screen.blit(string3stage,(tabuleiro.get_width()-200, 100))
    
    if table.executeOrder66: 
        kill['x'] = 600
        kill['y'] = 350
    else:
        kill['x'] = -200
        kill['y'] = -200
    
    pygame.display.flip()