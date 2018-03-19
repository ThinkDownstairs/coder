import pygame

import game_objects
import consts
import color
from typing import Tuple, List
import random

class Excepties(game_objects.GameObject):
    def __init__(self, color: Tuple[int, int, int]) -> None:
        super().__init__()
        self._rect = None # type: pygame.Rect
        self._x = 600
        self._y = random.randint(10, 600) 
        self._col = color
        self._delete_me = False # type: bool


    def render(self, screen):    
        self._rect = pygame.Rect(int(self._x), int(self._y), consts.EXCEPTIE_W, consts.EXCEPTIE_H)
        pygame.draw.rect(screen, self._col, self._rect, 0)

    def update(self, delta) -> bool:
        self._x -= (delta * consts.EXCEPTIE_SPEED)
        #return (bool(self._x < 0) or self._is_catched)

