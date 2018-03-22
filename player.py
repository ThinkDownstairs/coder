
from typing import Tuple

import pygame
import color
import consts


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
        self._mouse_pos = None

    def input(self, mouse_pos: Tuple[int, int]) -> None:
        self._mouse_pos = mouse_pos

    def render(self, target: pygame.Surface) -> None:
        self._catcher.render(target, consts.SCREEN_W - self._catcher.surface.get_width(), self._mouse_pos[1])
        self._progger.render(target, self._mouse_pos[0], consts.SCREEN_H - self._progger.surface.get_height())

    def update(self, delta) -> None:
        self._catcher.update(delta)
        self._progger.update(delta)

    catcher = property(lambda s: s._catcher)
