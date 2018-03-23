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
        self._y = consts.SCREEN_H - 50
        self._col = color
        self._is_killed = False # type: bool
        self._dummy = pygame.Surface((5, 30))


    def render(self, screen):
        pygame.draw.rect(screen, self._col, self._rect, 0)

    def update(self, delta) -> bool:
        self._y -= delta
        self._rect = pygame.Rect(self._x, self._y, consts.SNIPPET_W, consts.SNIPPET_H)
        #return (bool(self._y < 0) or self._is_kill

    def _get_surface(self) -> pygame.Surface:
        return self._dummy
