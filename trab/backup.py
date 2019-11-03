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