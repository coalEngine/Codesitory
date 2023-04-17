import pygame
pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze")
running = True
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font = pygame.font.Font("Maze/Fonts/dogicapixelbold.ttf", 32)
menu_text = font.render("Maze", True, WHITE, BLACK)
menu_text_rect = menu_text.get_rect()
menu_text_rect.center = (WIDTH // 2, HEIGHT // 2 - 200)