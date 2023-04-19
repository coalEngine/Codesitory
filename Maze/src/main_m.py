import pygame, sys
from Menu import Menu
from settings import *
pygame.init()


while running:
    screen.fill(BLACK)
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False
            sys.exit()
    Menu.Run()
    pygame.display.update()
    clock.tick(60)