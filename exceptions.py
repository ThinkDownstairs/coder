import pygame
import consts
import color
from typing import Tuple, List
import random

class Excepties(object):
    def __init__(self, color: Tuple[int, int, int]) -> None:
        self._rect = None # type: pygame.Rect
        self._x = 600
        self._y = random.randint(10, 600) 
        self._col = color
        self._is_catched = False # type: bool


    def render(self, screen):    
        self._rect = pygame.Rect(int(self._x), int(self._y), consts.EXCEPTIE_W, consts.EXCEPTIE_H)
        pygame.draw.rect(screen, self._col, self._rect, 0)

    def update(self, delta) -> bool:
        self._x -= (delta * consts.EXCEPTIE_SPEED)
        return (bool(self._x < 0) or self._is_catched)


class ExceptiesManager(object):
    def __init__(self) -> None:
        self._exception_list = [] #type: List[Excepties]

    def add_exceptie(self, color):
        self._exception_list.append(Excepties(color))

    def render(self, screen, delta):
        for exceptie in self._exception_list:
            if exceptie.update(delta):
                self._exception_list.remove(exceptie) # remove snips from list
            exceptie.render(screen)

    def get_exceptions_list(self) -> List[Excepties]:
        return self._exception_list