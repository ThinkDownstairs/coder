
from typing import Tuple

import pygame

import game_objects
import animations
import globals_

class Effect(game_objects.GameObject):

    def __init__(self, start_pos: Tuple[int, int], end_pos: Tuple[int, int]):
        super().__init__()
        self._x, self._y = start_pos
        self._end_x, self._end_y = end_pos

        # TODO cals dx, dy for a straight line

        self._animation = animations.Effect()
        globals_.get_manager().add_object(self)


    def render(self, target: pygame.Surface):
        self._animation.render(target, self._x, self._y)

    def update(self, delta: int):
        self._animation.update(delta)
        if int(self._x) > self._end_x:
            self._x -= 1
        elif int(self._x) < self._end_x:
            self._x += 1
        if int(self._y) > self._end_y:
            self._y -= 1
        elif int(self._y) < self._end_y:
            self._y += 1


    def _get_surface(self) -> pygame.Surface:
        return self._animation.surface
