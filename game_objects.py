import pygame

class GameObject(object):
    def __init__(self):
        self._rect = None # type: pygame.Rect
        self._x = None # type: int
        self._y = None # type: int
        self._delete_me = None # type: bool

    def render(self, target: pygame.Surface):
        pass

    def update(self, delta: int):
        pass
