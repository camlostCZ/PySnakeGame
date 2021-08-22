"""
"""

import pygame


class SnakeGame:
    def __init__(self) -> None:
        self._init_pygame()
        self.screen = pygame.display.set_mode((1024, 768))


    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()


    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Snake Game")


    def _handle_input(self):
        """Game event handler.

        Used to process user input.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


    def _process_game_logic(self):
        pass


    def _draw(self):
        self.screen.fill(0, 0, 255)
        pygame.display.flip()
