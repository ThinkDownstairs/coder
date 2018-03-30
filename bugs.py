import pygame
import game_objects
import consts
import color
import animations
from typing import List, Tuple
import random
import status
import math


LEVEL_1_BUGS = [animations.Surfaces.BUG_GREEN_1, animations.Surfaces.BUG_GREEN_2]
LEVEL_2_BUGS = [animations.Surfaces.BUG_YELLOW_1, animations.Surfaces.BUG_YELLOW_2]
LEVEL_3_BUGS = [animations.Surfaces.BUG_GRAY_1, animations.Surfaces.BUG_GRAY_2]
LEVEL_4_BUGS = [animations.Surfaces.BUG_RED_1, animations.Surfaces.BUG_RED_2]

BUG_POINTS = {
    animations.Surfaces.BUG_GREEN_1: 1,
    animations.Surfaces.BUG_GREEN_2: 1,
    animations.Surfaces.BUG_YELLOW_1: 10,
    animations.Surfaces.BUG_YELLOW_2: 10,
    animations.Surfaces.BUG_GRAY_1: 100,
    animations.Surfaces.BUG_GRAY_2: 100,
    animations.Surfaces.BUG_RED_1: 1000,
    animations.Surfaces.BUG_RED_2: 1000}

class Bugs(game_objects.GameObject):
    def __init__(self, status_: status.Status) -> None:
        super().__init__()
        self._x = random.randint(consts.BUG_FIELD_X, consts.SCREEN_W - 160) * 1.0
        self._y = random.randint(consts.BUG_FIELD_Y, consts.SCREEN_H - 160) * 1.0
        self._status = status_

        lvl = status_.level
        bug_type = self._random(lvl)
        self._plus_points = BUG_POINTS[bug_type]

        # the higher the level, the more negative points
        self._minus_points = self._plus_points * max(1, lvl // 3)

        direction = random.random() * 3.14159 * 2
        speed = (.001 * (1 + lvl)) + (random.random() * (.0025 * (1 + lvl)))
        self._dy = math.sin(direction) * speed
        self._dx = math.cos(direction) * speed

        self._animation = animations.Bug(bug_type)

    def _is_on_screen(self) -> bool:
        if (0 < self._x < consts.SCREEN_W) and (0 < self._y < consts.SCREEN_H):
            return True
        if ((self._x + self._animation.surface.get_width()) < 0) or ((self._y + self._animation.surface.get_height()) < 0):
            return False
        return True

    def render(self, target: pygame.Surface):
        self._animation.render(target, int(self._x), int(self._y))

    def update(self, delta: int):
        self._animation.update(delta)
        self._x += (self._dx * delta)
        self._y += (self._dy * delta)
        if not self._is_on_screen():
            self._status.inc_point(-self._minus_points)
            self.delete()

    def _get_surface(self) -> pygame.Surface:
        return self._animation.surface

    def _random(self, lvl: int): # {{{1
        if lvl < 1:
            return random.choice(LEVEL_1_BUGS)
        elif lvl < 2:
            if random.random() < .5:
                return random.choice(LEVEL_1_BUGS)
            else:
                return random.choice(LEVEL_2_BUGS)
        elif lvl < 3:
            r = random.random()
            if r < .333:
                return random.choice(LEVEL_1_BUGS)
            elif r < .666:
                return random.choice(LEVEL_2_BUGS)
            else:
                return random.choice(LEVEL_3_BUGS)
        elif lvl < 4:
            r = random.random()
            if r < .25:
                return random.choice(LEVEL_1_BUGS)
            elif r < .5:
                return random.choice(LEVEL_2_BUGS)
            elif r < .75:
                return random.choice(LEVEL_3_BUGS)
            else:
                return random.choice(LEVEL_4_BUGS)
        elif lvl < 5:
            r = random.random()
            if r < .2:
                return random.choice(LEVEL_1_BUGS)
            elif r < .4:
                return random.choice(LEVEL_2_BUGS)
            elif r < .6:
                return random.choice(LEVEL_3_BUGS)
            else:
                return random.choice(LEVEL_4_BUGS)
        else:
            r = random.random()
            if r < .15:
                return random.choice(LEVEL_1_BUGS)
            elif r < .3:
                return random.choice(LEVEL_2_BUGS)
            elif r < .45:
                return random.choice(LEVEL_3_BUGS)
            else:
                return random.choice(LEVEL_4_BUGS)

    # properties {{{1
    points = property(lambda s: s._plus_points)



