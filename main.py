import pygame
from constants import *
from Entity import *
import time
import random
displayResolution = (400,400)
screenCentre = (displayResolution[0]/2, displayResolution[1]/2)

isFullscreen = 0
canResize = 1
clock = pygame.time.Clock()

gameRunning = True


if __name__ == "__main__":

    pygame.init()
    if isFullscreen:
        window = pygame.display.set_mode(displayResolution, pygame.FULLSCREEN )
    else:
        window = pygame.display.set_mode(displayResolution)
    horizon = 200
    new_tree = Entity((200, 0, 0), "tree.png")
    #for i in range(0,50):
    #    new_tree = Entity((random.randrange(-500,500), 0, random.randrange(-500,500)), "tree.png")
    #    new_tree = Entity((random.randrange(-500,500), 0, random.randrange(-500,500)), "tree.png")


    player = Player((200,0,-100))
    entityList = list_sort(entityList)


    while gameRunning:
        clock.tick(60);
        #player input
        player.move()


        #draw
        window.fill(WHITE)
        pygame.draw.rect(window, GRASS_GREEN, (0, 200, 400, 200))
        pygame.draw.rect(window, SKY_BLUE,(0,0,400,200))
        pygame.draw.line(window, BLACK, (0, horizon), (400, horizon), 2)

        if (time.time())%1 == 0:
            entityList = list_sort(entityList)



        for entity in entityList:
            entity.draw(window, horizon, (player.x, player.y, player.z))

        pygame.display.flip()
        #closing input
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                gameRunning = False
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            gameRunning = False

        #player input



pygame.quit()
exit()