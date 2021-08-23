"""
SnakeGame Board

I'm still considering logical separation of this code (i.e. game board)
from the game itself.
Maybe it's too much - too many references to the snake object
passed from one constructor to another, etc.
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
        """(This should return some value which indicates whether:
            - snake collided with a wall
            - snake's found food
            - snake's found poison
            - etc.
            )
        """
        pass