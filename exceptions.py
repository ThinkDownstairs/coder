import pygame

import game_objects
import consts
import color
import animations
from typing import Tuple, List
import random
import status

class Excepties(game_objects.GameObject):
    def __init__(self, status_: status.Status) -> None:
        super().__init__()
        self._animation =  animations.Error(random.choice([
            animations.Surfaces.FLOATINGPOINTERROR,
            animations.Surfaces.INDEXERROR,
            animations.Surfaces.KEYERROR,
            animations.Surfaces.MEMORYERROR,
            animations.Surfaces.NOTIMPLEMENTEDERROR,
            animations.Surfaces.OVERFLOWERROR,
            animations.Surfaces.RECURSIONERROR,
            animations.Surfaces.RUNTIMEERROR,
            animations.Surfaces.TYPEERROR]))
        self._y = random.randint(30, consts.SCREEN_H - 140)
        self._status = status_
        self._width = self._animation.surface.get_width()
        offset, range_ = consts.EXCEPTION_SPEEDS[min(self._status.level, len(consts.EXCEPTION_SPEEDS) - 1)]
        self._speed = offset + random.random() * range_


    def render(self, target) -> None:
        self._animation.render(target, self._x, self._y)
        #self._rect = pygame.Rect(int(self._x), int(self._y), consts.EXCEPTIE_W, consts.EXCEPTIE_H)
        #pygame.draw.rect(screen, self._col, self._rect, 0)

    def update(self, delta) -> bool:
        self._x += (delta * self._speed)
        self._animation.update(delta)
        if (self._x + self._width) > consts.SCREEN_W:
            self.delete()
            self._status.dec_health()
        #return (bool(self._x < 0) or self._is_catched)

    def _get_surface(self) -> pygame.Surface:
        return self._animation.surface

