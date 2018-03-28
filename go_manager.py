import pygame
import player

import snippets
import exceptions
import bugs
import collision

import globals_
import sound

import status
import game_objects
from typing import List

class GoManager(object):
    def __init__(self):
        super().__init__()
        self._go_list = [] # type: List[GameObjects]
        self._sound = globals_.get_sound() # type: sound.Sound

    def add_object(self, game_object: game_objects.GameObject):
        self._go_list.append(game_object)

    def clear_objects(self):
        self._go_list = []

    def render(self, target: pygame.Surface):
        for go in self._go_list:
            go.render(target)

    def update(self, delta: int, player_: player.Player, status_: status.Status):
        for go in self._go_list:
            go.update(delta)

        bugs_ = [go for go in self._go_list if isinstance(go, bugs.Bugs)]

        for go in self._go_list:
            if isinstance(go, exceptions.Excepties):
                player_.try_catch(go)

            elif isinstance(go, snippets.Snippet):
                s = go
                s_surface = s.surface
                s_x, s_y = s.pos
                for b in bugs_:
                    if not b._delete_me:
                        if collision.collide(s_surface, s_x, s_y, b.surface, *b.pos):
                            self._sound.play(sound.Sounds.KILL)
                            s.delete()
                            b.delete()
                            status_.inc_point()
                            break

        # takes only those go to the list which are go._delete_me == true
        self._go_list = [go for go in self._go_list if not go._delete_me]


