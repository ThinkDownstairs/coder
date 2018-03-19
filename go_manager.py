import pygame

import game_objects
from typing import List

class GoManager(object):
    def __init__(self):
        self._go_list = [] # type: List[GameObjects]

    def add_object(self, game_object: game_objects.GameObjects):
        self._go_list.append(game_object)

    def render(self):
        for go in self._go_list:
            go.render()
 
    def update(self):
        for go in self._go_list:
            go.update()
        # takes only those go to the list which are go._delete_me == true
        self._go_list = [go for go in self._go_list if not go._delete_me]


if __name__ == '__main__':
    print([i for i in range(0, 10) ])
    
