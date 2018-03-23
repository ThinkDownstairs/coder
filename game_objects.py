import pygame

class GameObject(object):
    def __init__(self):
        self._rect = None # type: pygame.Rect
        self._x = 0 # type: int
        self._y = 0 # type: int
        self._delete_me = False # type: bool

    def render(self, target: pygame.Surface):
        pass

    def update(self, delta: int):
        pass

    def _get_surface(self) -> pygame.Surface:
        pass

    def delete(self) -> None:
        self._delete_me = True


    surface = property(lambda s: s._get_surface())
    pos = property(lambda s: (s._x, s._y))
    delete_me = property(lambda s: s._delete_me)

