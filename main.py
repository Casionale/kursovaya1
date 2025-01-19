import pygame
import DB
import settings
from credits_screen import CreditsScreen
from difficulty import Difficulty
from game import Game
from input_screen import InputScreen
from menu import Menu
from records_screen import RecordsScreen

pygame.init()

# Настройка окна
screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
pygame.display.set_caption("Katamacy is like Katamari Damacy but 2D")

menu = Menu(screen)
game = Game(screen)
input_screen = InputScreen(screen)
records_screen = RecordsScreen(screen)
credits_screen = CreditsScreen(screen)
difficulty_screen = Difficulty(screen)

running = True
print('Cur screen set MENU')
settings.CURRENT_SCREEN = "menu"

# Главный цикл игры
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if settings.CURRENT_SCREEN == "menu":
            menu.handle_event(event)

        if settings.CURRENT_SCREEN == "difficulty":
            difficulty_screen.handle_event(event)

        if settings.CURRENT_SCREEN == "input":
            player_name = input_screen.handle_event(event)
            if player_name is not None:
                s = DB.Database()
                s.add_record(player_name, settings.GAME_TIME, settings.GAME_DIFF)
                settings.CURRENT_SCREEN = "records"
            pass

        if settings.CURRENT_SCREEN == "records":
            records_screen.handle_event(event)

        if settings.CURRENT_SCREEN == "credit":
            credits_screen.handle_event(event)

    if settings.CURRENT_SCREEN == "menu":
        menu.draw()
    if settings.CURRENT_SCREEN == "game":
        game.to_game()
    if settings.CURRENT_SCREEN == "input":
        input_screen.draw()
    if settings.CURRENT_SCREEN == "difficulty":
        difficulty_screen.draw()
    if settings.CURRENT_SCREEN == "records":
        records_screen.draw()
    if settings.CURRENT_SCREEN == "credit":
        credits_screen.update()
        credits_screen.draw()

    pygame.display.flip()

pygame.quit()


