import pygame

import game_objects
import consts
import color
import animations
from typing import Tuple, List
import random

class Excepties(game_objects.GameObject):
    def __init__(self, color: Tuple[int, int, int]) -> None:
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
        self._y = random.randint(10, 500)
        self._col = color # TODO : nicht mehr benötigt.


    def render(self, target) -> None:
        self._animation.render(target, self._x, self._y)
        #self._rect = pygame.Rect(int(self._x), int(self._y), consts.EXCEPTIE_W, consts.EXCEPTIE_H)
        #pygame.draw.rect(screen, self._col, self._rect, 0)

    def update(self, delta) -> bool:
        self._x += (delta * consts.EXCEPTIE_SPEED)
        self._animation.update(delta)
        #return (bool(self._x < 0) or self._is_catched)

    def _get_surface(self) -> pygame.Surface:
        return self._animation.surface

