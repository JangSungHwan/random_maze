
import pygame, random, sys
from pygame.locals import *

TEXTCOLOR = (255, 255, 255)

windowSurface = pygame.display.set_mode((450, 650))

black = (0,0,0)
wid = 450
hei = 550



display = pygame.display.set_mode((wid,hei))

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits.
                    terminate()
                if event.key == K_m:
                    player = pygame.image.load('mommyson.png')
                    return
                return
    
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

    
def levelcollect():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: 
                    terminate()
                if event.key == K_1: 
                    return 20
                elif event.key == K_2:
                    return 30
                elif event.key == K_3: 
                    return 40
                elif event.key == K_4: 
                    return 60
                    
pygame.init()
font = pygame.font.SysFont(None, 48)

level = pygame.image.load('level.png')
display.blit(level, (0, 0))
pygame.display.update()

size = levelcollect()
gameOverSound = pygame.mixer.Sound('hongik.WAV')
pygame.mixer.music.load('Mommyson.WAV')
player = pygame.image.load('player.png')
mommyson = pygame.image.load('mommyson.png')
map1 = [[1]*(size+3) for i in range(size+3)]
def mapmake():

    mx=5
    my=5

    for i in range(30000):
        rotate = random.randint(1,4)
        if rotate == 1:
            if my == 5:
                continue
            if map1[mx][my - 2] == 1:
                my = my-1
                map1[mx][my] = 0
                my = my-1
                map1[mx][my] = 0
            else:
                my = my-2
        if rotate == 2:
            if mx == size - 3:
                continue
            if map1[mx+2][my] == 1:
                mx = mx+1
                map1[mx][my] = 0
                mx = mx+1
                map1[mx][my] = 0
            else:
                mx = mx+2
        if rotate == 3:
            if my == size-3:
                continue
            if map1[mx][my + 2] == 1:
                my = my+1
                map1[mx][my] = 0
                my = my+1
                map1[mx][my] = 0
            else:
                my = my+2
        if rotate == 4:
            if mx == 5:
                continue
            if map1[mx-2][my] == 1:
                mx = mx-1
                map1[mx][my] = 0
                mx = mx-1
                map1[mx][my] = 0
            else:
                mx = mx-2
    map1[size-3][size-3] = 4
    map1[2][2] = 3
    print(map1)


start = pygame.image.load('start.png')
display.blit(start, (0, 0))
pygame.display.update()
waitForPlayerToPressKey()

def moving():
    global scy_change, scx_change, scx, scy
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            if map1[scx+4][scy+5] != 1:
                scy_change = scy_change + 1
        if event.key == pygame.K_UP:
            if map1[scx+4][scy+3] != 1:
                scy_change = scy_change - 1
        if event.key == pygame.K_LEFT:
            if map1[scx+3][scy+4] != 1:
                scx_change = scx_change - 1
        if event.key == pygame.K_RIGHT:
            if map1[scx+5][scy+4] != 1:
                scx_change = scx_change + 1
        if event.key == pygame.K_r:
            scx = 1
            scy = 1
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN or \
            event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            scx_change = 0
            scy_change = 0
    scx += scx_change
    scy += scy_change

scx=1
scy=1
def mapdraw():
    for i in range(0,9):
        for j in range(0,9):
            if map1[scx+j][scy+i] == 1:
                display.blit(wall, (j*50, i*50))
            elif map1[scx+j][scy+i] == 0:
                display.blit(space, (j*50, i*50))
            elif map1[scx+j][scy+i] == 4:
                display.blit(goal, (j*50, i*50))
            elif map1[scx+j][scy+i] == 3:
                display.blit(hongik, (j*50, i*50))
    display.blit(player, (200, 200))


pygame.display.set_caption("홍대탈출!!!")
wall = pygame.image.load('wall.png')
space = pygame.image.load('space.png')
goal = pygame.image.load('goal.png')
hongik = pygame.image.load('hongik.png')
over = pygame.image.load('over.png')
scy_change = 0
scx_change = 0
x = 100
y = 100

topScore = 0

while True:
    mapmake()
    score = 100000
    pygame.mixer.music.play(-1, 0.0)
    while True:
        score -= 1
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            
            moving()

        mapdraw()

        pygame.display.update()
        display.fill(black)
        drawText('Time: %s' % (score), font, windowSurface, 10, 460)
        drawText('Best: %s' % (topScore), font, windowSurface, 10, 520)
        if map1[scx+4][scy+4] == 4 or score == 0:
            pygame.mixer.music.stop()
            gameOverSound.play()
            if score > topScore:
                topScore = score # set new top score
            scx = 1
            scy = 1
            break

    display.blit(over, (0, 0))
    pygame.display.update()
    waitForPlayerToPressKey()
    map1 = [[1]*(size+3) for i in range(size+3)]
    gameOverSound.stop()
