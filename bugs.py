import pygame
import game_objects
import consts
import color
import animations
from typing import List, Tuple
import random

class Bugs(game_objects.GameObject):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self._x = x
        self._y = y
        self._animation = animations.Bug(random.choice([
            animations.Surfaces.BUG_RED_1,
            animations.Surfaces.BUG_RED_2,
            animations.Surfaces.BUG_GREEN_1,
            animations.Surfaces.BUG_GREEN_2,
            animations.Surfaces.BUG_YELLOW_1,
            animations.Surfaces.BUG_YELLOW_2,
            animations.Surfaces.BUG_GRAY_1,
            animations.Surfaces.BUG_GRAY_2]))

    def render(self, target: pygame.Surface):
        self._animation.render(target, self._x, self._y)

    def update(self, delta: int):
        self._animation.update(delta)

    def _get_surface(self) -> pygame.Surface:
        return self._animation.surface


