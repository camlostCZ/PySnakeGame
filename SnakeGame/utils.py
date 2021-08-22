"""
Useful functions used across the project.
"""

from pygame.image import load
from pygame import Surface


def load_sprite(name: str, with_alpha: bool = True) -> Surface:
    """Load sprite from file.

    Args:
        name (str): Sprite name.
        with_alpha (bool, optional): Flag if load with alpha channel. Defaults to True.

    Returns:
        Surface: The sprite as loaded from file.
    """
    path = f"assets/sprites/{name}.png"
    loaded_sprite = load(path)

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()
