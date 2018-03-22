import pygame
import player

import snippets
import exceptions
import bugs

import game_objects
from typing import List

class GoManager(object):
    def __init__(self):
        self._go_list = [] # type: List[GameObjects]

    def add_object(self, game_object: game_objects.GameObject):
        self._go_list.append(game_object)

    def render(self, target: pygame.Surface):
        for go in self._go_list:
            go.render(target)

    def update(self, delta: int, player_: player.Player):
        for go in self._go_list:
            go.update(delta)

        #get all lists of different gameobjects
        snips = [go for go in self._go_list if isinstance(go, snippets.Snippet)]
        excepties = [go for go in self._go_list if isinstance(go, exceptions.Excepties)]
        bugs_ = [go for go in self._go_list if isinstance(go, bugs.Bugs)]

        # TODO : lukas !!!! player auf animationnen umgebaut,.. hier collision detection machen!! auf sprite, nicht rect!!
        # collision detection
        #catcher = player_.catcher.
        #for ex in excepties:
        #    if ex._rect.colliderect(catcher._rect):
        #        ex._delete_me = True

        for s in snips:
            for b in bugs_:
                if s._rect.colliderect(b._rect):
                    s._delete_me = True
                    b._delete_me = True

        # takes only those go to the list which are go._delete_me == true
        self._go_list = [go for go in self._go_list if not go._delete_me]


if __name__ == '__main__':
    print([i for i in range(0, 10) ])

