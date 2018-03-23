import pygame
import player

import snippets
import exceptions
import bugs
import collision

import status
import game_objects
from typing import List

class GoManager(object):
    def __init__(self):
        super().__init__()
        self._go_list = [] # type: List[GameObjects]

    def add_object(self, game_object: game_objects.GameObject):
        self._go_list.append(game_object)

    def clear_objects(self):
        self._go_list = []

    def render(self, target: pygame.Surface):
        for go in self._go_list:
            go.render(target)

    def update(self, delta: int, player_: player.Player, status_: status.Stati):
        for go in self._go_list:
            go.update(delta)

        #get all lists of different gameobjects
        snips = [go for go in self._go_list if isinstance(go, snippets.Snippet)]
        excepties = [go for go in self._go_list if isinstance(go, exceptions.Excepties)]
        bugs_ = [go for go in self._go_list if isinstance(go, bugs.Bugs)]

        for ex in excepties:
            player_.try_catch(ex)

        for s in snips:
            s_surface = s.surface
            s_x, s_y = s.pos
            for b in bugs_:
                if collision.collide(s_surface, s_x, s_y, b.surface, *b.pos):
                    s.delete()
                    b.delete()
                    status_.inc_point()

        # takes only those go to the list which are go._delete_me == true
        self._go_list = [go for go in self._go_list if not go._delete_me]



if __name__ == '__main__':
    print([i for i in range(0, 10) ])

