import pygame
import animations

import status
import game_objects
import consts
import color
import random
from typing import Tuple, List

class Snippet(game_objects.GameObject):
    def __init__(self, status_: status.Status, mouse_pos_x: int) -> None:
        super().__init__()
        self._animation = animations.Snippet(random.choice([
            animations.Surfaces.FIBONACCI,
            animations.Surfaces.FOR_I_IN_RANGE,
            animations.Surfaces.FOR_ITEM_IN_ITEMS,
            animations.Surfaces.IMPORT_PYGAME,
            animations.Surfaces.PRINT_HELLO_WORLD,
            animations.Surfaces.REVERSE,
            animations.Surfaces.SQR_LAMBDA,
            animations.Surfaces.STR_JOIN,
            animations.Surfaces.XY_POINT]))
        self._x = mouse_pos_x - self._animation.surface.get_width() // 2
        self._y = consts.SCREEN_H
        self._h = self._animation.surface.get_height()
        self._status = status_

    def render(self, screen):
        self._animation.render(screen, self._x, self._y)

    def update(self, delta) -> None:
        self._animation.update(delta)
        if self._y < -self._h:
            self.delete()
            self._status.inc_point(self._status.level * 3)
        self._y -= (delta * consts.SNIPPET_SPEED)

    def _get_surface(self) -> pygame.Surface:
        return self._animation.surface
