class Position:
    """A new type for easier handling of position.

    Attributes:
        left (int): Left coordinate (also horizontal, column, or X)
        top (int): Top coordinate (also vertical, row, or Y)
    """
    def __init__(self, left: int, top: int) -> None:
        self.left = left
        self.top = top
