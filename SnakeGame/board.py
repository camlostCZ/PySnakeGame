"""
SnakeGame Board
"""

from snake import Snake

class Board:
    """
    Instance of this class is used to draw board and all objects on it.
    Including the snake.
    """
    
    def __init__(self, width: int, height: int, snake: Snake) -> None:
        self.width = width
        self.height = height
        self.snake = snake


    def draw(self, screen):
        # TODO Implement
        pass


    def check_snake_collision(self):