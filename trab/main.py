import sys, pygame
pygame.init()
pygame.display.set_caption('Trilha')

icon = pygame.image.load('assets/ico.png')
pygame.display.set_icon(icon)

size = width, height = 810, 600
speed = [1, 1]

screen = pygame.display.set_mode(size)

tabuleiro = pygame.image.load('assets/tab.png')
red = {'img': pygame.image.load('assets/red.png'), 'x': 25, 'y':25}
dark = {'img': pygame.image.load('assets/dark.png'), 'x': 105, 'y':105}
mark = {'img': pygame.image.load('assets/mark.png'), 'x': 525, 'y':285}

myfont = pygame.font.SysFont('assests/modak.ttf', 30)
textsurface = myfont.render('Sua Vez!', False, (0, 0, 0))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT:
                red['x'] += 10
            
            if event.key == pygame.K_LEFT:
                red['x'] -= 10
            
            if event.key == pygame.K_UP:
                red['y'] -= 10
            
            if event.key == pygame.K_DOWN:
                red['y'] += 10

    mouse = mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if mouse_click != (0,0,0): 
        print(mouse)
        mark['x'] = mouse_x - (mark['img'].get_width()/2)
        mark['y'] = mouse_y - (mark['img'].get_height()/2)

    if mouse_x >= 62 - 30 and mouse_x <= 62 + 30 and mouse_y >= 63 - 30 and mouse_y <= 63 + 30:
        mark['x'] = 62 - 15
        mark['y'] = 63 - 15

    else:
        mark['x'] = -30
        mark['y'] = -30

    screen.blit(tabuleiro, (0,0))
    screen.blit(textsurface,(tabuleiro.get_width()-100, 10))
    # screen.blit(red['img'], (red['x'], red['y']))
    # screen.blit(dark['img'], (dark['x'], dark['y']))
    screen.blit(mark['img'], (mark['x'], mark['y']))
    pygame.display.flip()