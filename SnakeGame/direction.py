from enum import Enum

class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

    def get_position_delta(self, direction: "Direction") -> tuple(int, int):
        d_x, d_y = 0
        if direction == Direction.NORTH:
            d_y = -1
        elif direction == Direction.EAST:
            d_x = 1
        elif direction == Direction.SOUTH:
            d_y = 1
        elif direction == Direction.WEST:
            d_x = -1
        return (d_x, d_y)
