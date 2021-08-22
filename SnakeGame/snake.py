from errors import SnakeException
from position import Position
from direction import Direction

class Snake:
    """Snake class.

    Attributes:
        head: Position of the head
        body: List of body elements incl. head
        direction: The direction the snake is heading

    Methods:
        move(): Update position of the snake
        grow(): Add an element to snakes tail
        is_bite(): Check if snake bites itself
        build_body(): Create snake's body based on length and direction
    """

    def __init__(self, 
            position: Position, 
            length: int = 1, 
            direction: Direction = Direction.WEST) -> None:
        """Initialize snake object.

        Args:
            position (Position): Initial position of the snake.
            length (int, optional): Initial snake length. Defaults to 2.
            direction (Direction, optional): Initial direction. Defaults to Direction.WEST.
        """
        if length < 1:
            raise SnakeException("Invalid snake length")
        self.body = Snake.build_body(position, length, direction)  # List of positions
        self.head = self.body[0]
        self.direction = direction


    def move(self) -> None:
        """Move the snake in its current direction.
        """
        # Update position of all body elements from tail to head
        # (excluding head).
        for idx in range(self.body.length - 1, 0, -1):
            elem = self.body[idx]
            elem.top = self.body[idx - 1].top
            elem.left = self.body[idx - 1].left

        # Update position of the head
        dx, dy = self.direction.get_position_delta()
        self.head.top += dy
        self.head.left += dx


    def grow(self) -> None:
        """Grow the snake by one.

        Caution: This method has to be called just before move()
        so that the position of tail is updated correctly.
        """
        tail = self.body[-1]
        new_elem = Position(tail.left, tail.top)
        self.body.append(new_elem)


    def is_bite(self) -> bool:
        """Check if snake bites itself.

        This happens when the position of the head is the same as the
        position of any body element.

        Returns:
            bool: [description]
        """
        result = False
        for elem in self.body[1:]:
            result = result or \
                (self.head.top == elem.top and self.head.left == elem.left)
        return result


    @staticmethod
    def build_body(
            position: Position, 
            length: int, 
            direction: Direction) -> list[Position]:
        """Create snake's body (incl. head).

        Args:
            position (Position): Position of snake's head.
            length (int): Snake's length / size.
            direction (Direction): Direction the snake is heading.

        Returns:
            list[Position]: List of position of individual body parts.
        """
        result = []  # New body
        dx, dy = direction.get_position_delta()
        x, y = position.left, position.top
        for _ in range(length):
            result.append(Position(x, y))
            x -= dx  # Body grows in the opposite direction ...
            y -= dy  # ... than the snake is heading.
        return result