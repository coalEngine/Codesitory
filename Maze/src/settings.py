import pygame
from Button import Button
pygame.init()

world_1_level1 = [
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX          ',
'X                                                                                                                                                        XX          ',
'XXXXXX                                                                                                                                                   XX          ',
'      XX                            XXX   XX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXX                                                        XX          ',
'       XX                       XX       X                                              X                                                  XXXX          XX          ',
'XXXXXXXXXXXXXXXXXXXXXXX       XX                                 XXXXXXXXXXXXXXXXXXXXXXXX                                           XX    X     XXXX     XX          ',
'X                                                                                                XXXXXX   XXXX  XX    XXX   XXX    X              XX     XX          ',
'X                        XX                                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                    XXX    XX          ',
'XXX                           X                  XXXXXXXXXXXXXXXX         X                   X                                                   XX     XX          ',
'X           XXXX    XXXX     XXX     XX                            XXXXXXXX                    X                                                  XX    XXX          ',
'X P  XXXXX    XX    XX        X       XX         XXXXXXXXXXXXXXXXXX                             XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                                                XXXXXXXXXXXXXXXX ',
]

tile_size = 64
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze")
running = True
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
