import pygame, sys
from Button import Button
from settings import *
from Level import Level
pygame.init()

def get_and_set_font(size):
    font = pygame.font.Font("Maze/Fonts/dogicapixelbold.ttf", size)
    return font

def settings_state():
    pygame.display.set_caption("Maze.Settings.State")

def credits_state():
    pygame.display.set_caption("Maze.Credits.State")

def play_state():
    pygame.display.set_caption("Maze.Play.State")
    level = Level(world_1_level1, screen)
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        fps_text = get_and_set_font(10).render("FPS: {}".format(str(round(clock.get_fps()))), True, WHITE, BLACK)
        fps_text_rect = fps_text.get_rect()
        fps_text_rect.center = (36, 16)
        
        screen.fill(BLACK)
        screen.blit(fps_text, fps_text_rect)
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        level.init()
        pygame.display.update()
        clock.tick(60)
        
def main_state():
    pygame.display.set_caption("Maze.Menu.State")
    
    while True:
        MAIN_MOUSE_POS = pygame.mouse.get_pos()
        menu_text = get_and_set_font(72).render("Maze", True, WHITE, BLACK)
        menu_text_rect = menu_text.get_rect()
        menu_text_rect.center = (WIDTH // 2, HEIGHT // 2 - 300)
        
        play_button = Button(None,(640, 240), "PLAY", get_and_set_font(32), "White", "Green")
        credits_button = Button(None,(640, 300), "CREDITS", get_and_set_font(32), "White", "Green")
        settings_button = Button(None, (36, 680), "*", get_and_set_font(64), "White", "Green")
        
        screen.fill(BLACK)
        screen.blit(menu_text, menu_text_rect)
        
        for button in [play_button, credits_button, settings_button]:
            button.changeColor(MAIN_MOUSE_POS)
            button.update(screen)
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evt.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(MAIN_MOUSE_POS):
                    play_state()
                if credits_button.checkForInput(MAIN_MOUSE_POS):
                    credits_state()
                if settings_button.checkForInput(MAIN_MOUSE_POS):
                    settings_state()
        pygame.display.update()
        
main_state()