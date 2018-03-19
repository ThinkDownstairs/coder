import pygame
import game_objects
import consts
import color
from typing import List, Tuple

class Bugs(game_objects.GameObject):
    def __init__(self, color: Tuple[int, int, int], x: int, y: int) -> None:
        super().__init__()
        self._rect = None # type: pygame.Rect
        self._x = x
        self._y = y
        self._col = color
        self._delete_me = False # type: bool        

    def render(self, screen):    
        self._rect = pygame.Rect(self._x, self._y, consts.BUG_W, consts.BUG_H)
        pygame.draw.rect(screen, self._col, self._rect, 0)

    def update(self, delta: int):
        pass

    def is_collided(self, sprite: pygame.Rect):
        if self._rect != None:
            return self._rect.colliderect(sprite)
        else: return False
        