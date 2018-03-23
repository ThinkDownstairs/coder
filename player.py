
from typing import Tuple

import pygame
import color
import consts
import snippets
import exceptions
import collision


import random

import animations


class Player(object):
    def __init__(self) -> None:
        super().__init__()
        self._catcher = animations.TryExcept()
        self._progger = animations.Player(random.choice([ ## TODO : refactor to let the use decide which editor to use, not random
            animations.Surfaces.ATOM,
            animations.Surfaces.EMACS,
            animations.Surfaces.INTELLIJ,
            animations.Surfaces.NANO,
            animations.Surfaces.VIM,
            animations.Surfaces.VSCODE]))
        self._pos = (consts.SCREEN_W // 2, consts.SCREEN_H // 2)

    def set_pos(self, pos: Tuple[int, int]) -> None:
        self._pos = pos

    def render(self, target: pygame.Surface) -> None:
        cw, ch = self._catcher.surface.get_size()
        pw, ph = self._progger.surface.get_size()
        self._catcher.render(target, consts.SCREEN_W - cw , self._pos[1] - (ch // 2))
        self._progger.render(target, self._pos[0] - (pw // 2), consts.SCREEN_H - ph)

    def update(self, delta) -> None:
        self._catcher.update(delta)
        self._progger.update(delta)

    def fire(self) -> snippets.Snippet:
        return snippets.Snippet(color.POWDERBLUE, self._pos[0])

    def try_catch(self, exceptie: exceptions.Excepties) -> None:
        cw, ch = self._catcher.surface.get_size()
        if collision.collide(self._catcher.surface, consts.SCREEN_W - cw, self._pos[1] - (ch // 2), exceptie.surface, *exceptie.pos):
            exceptie.delete()

    catcher = property(lambda s: s._catcher)
