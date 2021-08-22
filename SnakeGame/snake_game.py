"""
"""

from SnakeGame.direction import Direction
import pygame

from position import Position
from snake import Snake


class SnakeGame:
    GAME_FPS = 60


    def __init__(self) -> None:
        self._init_pygame()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1024, 768))

        self.board = None
        self.snake = Snake(Position(10, 10))


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

        is_key_pressed = pygame.key.get_pressed()
        if is_key_pressed[pygame.K_RIGHT]:
            self.snake.direction = Direction.EAST
        elif is_key_pressed[pygame.K_LEFT]:
            self.snake.direction = Direction.WEST
        elif is_key_pressed[pygame.K_UP]:
            self.snake.direction = Direction.NORTH
        elif is_key_pressed[pygame.K_DOWN]:
            self.snake.direction = Direction.SOUTH


    def _process_game_logic(self):
        self.snake.move()


    def _draw(self):
        self.screen.fill(0, 0, 255)
        pygame.display.flip()
        self.clock.tick(SnakeGame.GAME_FPS)
