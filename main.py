import pygame

import DB
import settings
from game import Game
from input_screen import InputScreen

from menu import Menu

pygame.init()

# Настройка окна
screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
pygame.display.set_caption("Katamari 2D")

menu = Menu(screen)
game = Game(screen)
input_screen = InputScreen(screen)

running = True
print('Cur screen set MENU')
settings.CURRENT_SCREEN = "menu"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if settings.CURRENT_SCREEN == "menu":
            menu.handle_event(event)

        if settings.CURRENT_SCREEN == "input":
            player_name = input_screen.handle_event(event)
            if player_name is not None:
                s = DB.Database()
                s.add_record(player_name, settings.GAME_TIME)
                settings.CURRENT_SCREEN == "menu"
            pass


    if settings.CURRENT_SCREEN == "menu":
        menu.draw()
    if settings.CURRENT_SCREEN == "game":
        game.to_game()
    if settings.CURRENT_SCREEN == "input":
        input_screen.draw()

    pygame.display.flip()

#to_game()

pygame.quit()



