import pygame, sys
from Menu import Menu
from settings import running
pygame.init()

while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False
            sys.exit()
    pygame.display.update()
    Menu.Run()