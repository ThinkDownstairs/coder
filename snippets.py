import pygame

import game_objects
import consts
import color
from typing import Tuple, List

class Snippet(game_objects.GameObject):
    def __init__(self, color: Tuple[int, int, int], mouse_pos_x: int) -> None:
        super().__init__()
        self._rect = None # type: pygame.Rect
        self._textsurface = None # type: pygame.Surface
        self._myfont = None 
        self._x = mouse_pos_x
        self._y = 600
        self._col = color
        self._is_killed = False # type: bool


    def render(self, screen):    
        self._rect = pygame.Rect(self._x, self._y, consts.SNIPPET_W, consts.SNIPPET_H)
        pygame.draw.rect(screen, self._col, self._rect, 0)

    def update(self, delta) -> bool:
        self._y -= delta
        #return (bool(self._y < 0) or self._is_kill
