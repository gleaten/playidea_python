"""
유의할점: 파일제목을 pygame.py으로 하지 말 것. 
"""

import pygame


# CONSTANTS
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 600 
COLOR_SKY_BLUE = (153,255,255)
COLOR_DEEP_BLUE = (143,0,153)
PLOT_RADIUS = 10  # 주인공 원의 반경 
FPS = 120 # frame per sec

# INIT GAME
pygame.init()
pygame.display.set_caption("MY GAME")

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# starting point
pos_x, pos_y = SCREEN_WIDTH/2, 0

clock = pygame.time.Clock()

dy = 0 
life = 3 

Done = True
while Done:
    clock.tick(FPS)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            Done = False
    
    # Gravity
    dy += 0.1
    pos_y += dy
    
    if pos_y > SCREEN_HEIGHT:
        print("Die---")
        pos_x, pos_y = SCREEN_WIDTH/2, 0
        life -= 1 
        dy = 0 
        print(f"your life: {life}")
        if life == 0: 
            Done = False
    
    # KEY EVENTS
    key_event = pygame.key.get_pressed()
    
    if pos_x != 0: 
        if key_event[pygame.K_a]:
            pos_x -= 1
        
    if pos_x != SCREEN_WIDTH: 
        if key_event[pygame.K_d]:
            pos_x += 1
    
    if pos_y != 0: 
        if key_event[pygame.K_w]:
            pos_y -= 2
            dy = 0
        if key_event[pygame.K_UP]:
            pos_y -= 2
            dy = 0 
            
    if pos_y != SCREEN_HEIGHT: 
        if key_event[pygame.K_s]:
            pos_y += 1
            
    # PLOT 
    screen.fill(COLOR_SKY_BLUE)
    pygame.draw.circle(screen, COLOR_DEEP_BLUE, (pos_x,pos_y),PLOT_RADIUS)
    pygame.display.update()
    
# QUIT 
pygame.quit()
    