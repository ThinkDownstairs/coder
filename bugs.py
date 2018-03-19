import pygame
import consts
import color
from typing import List

class Bugs(object):
    def __init__(self, color, x, y) -> None:
        self._rect = None # type: pygame.Rect
        self._textsurface = None
        self._myfont = None 
        self._x = x
        self._y = y
        self._col = color
        self._is_killed = False # type: bool        

    def render(self, screen):    
        self._rect = pygame.Rect(self._x, self._y, consts.BUG_W, consts.BUG_H)
        pygame.draw.rect(screen, self._col, self._rect, 0)

    def is_collided(self, sprite: pygame.Rect):
        if self._rect != None:
            return self._rect.colliderect(sprite)
        else: return False


class BugManager(object):
    def __init__(self) -> None:
        self._bugs = []
        self._snippets = None # type: list

    def add_bug(self, color, x, y):
        self._bugs.append(Bugs(color, x, y))

    def inject_snippets(self, snippets: List[pygame.Rect]) -> None:
        self._snippets = snippets

    def render(self, screen):
        for bug in self._bugs:
            for snip in self._snippets:
                if snip._rect != None:
                    if bug.is_collided(snip._rect):
                        bug._is_killed = True
                        snip._is_killed = True
            bug.render(screen)
        self._bugs = list(filter(lambda b: not b._is_killed, self._bugs)) # some weird stuff from lukas ask lukas
        