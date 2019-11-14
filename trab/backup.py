# movivento por seta
if event.type == pygame.KEYDOWN :
    if event.key == pygame.K_RIGHT:
        red['x'] += 10
    
    if event.key == pygame.K_LEFT:
        red['x'] -= 10
    
    if event.key == pygame.K_UP:
        red['y'] -= 10
    
    if event.key == pygame.K_DOWN:
        red['y'] += 10

# Run game

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    mouse = mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if mouse_click != (0,0,0) : 
        print(mouse, ' -> ', table.getMark(mouse_x, mouse_y))
        
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