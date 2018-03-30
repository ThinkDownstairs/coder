
from typing import Tuple

import pygame
import color
import consts
import snippets
import exceptions
import collision
import status

import sound
import globals_

import random

import animations
import no_game_object


class Player(object):
    def __init__(self, status_: status.Status, editor: animations.Surfaces = None) -> None:
        super().__init__()
        self._catcher = animations.TryExcept()
        if editor is None:
            self._progger = animations.Player(random.choice([
                animations.Surfaces.ATOM,
                animations.Surfaces.EMACS,
                animations.Surfaces.INTELLIJ,
                animations.Surfaces.NANO,
                animations.Surfaces.VIM,
                animations.Surfaces.VSCODE]))
        else:
            self._progger = editor
        self._status = status_
        self._sound = globals_.get_sound()
        self._pos = (consts.SCREEN_W // 2, consts.SCREEN_H // 2)

    def reset(self, editor: animations.Surfaces = None):
        if editor is None:
            self._progger = animations.Player(random.choice([
                animations.Surfaces.ATOM,
                animations.Surfaces.EMACS,
                animations.Surfaces.INTELLIJ,
                animations.Surfaces.NANO,
                animations.Surfaces.VIM,
                animations.Surfaces.VSCODE]))
        else:
            self._progger = editor
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
        self._sound.play(sound.Sounds.FIRE)
        return snippets.Snippet(self._status, self._pos[0])

    def try_catch(self, exceptie: exceptions.Excepties) -> None:
        cw, ch = self._catcher.surface.get_size()
        cx, cy = consts.SCREEN_W - cw, self._pos[1] - (ch // 2)
        if collision.collide(self._catcher.surface, cx, cy, exceptie.surface, *exceptie.pos):
            exceptie.delete()
            no_game_object.NoGameObject(animations.CatchException(), cx, cy - 10)
            self._sound.play(sound.Sounds.CATCH)


    catcher = property(lambda s: s._catcher)

