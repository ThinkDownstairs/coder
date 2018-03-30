
import pygame
import typing
import consts
import color
import random
import animations

SPACING = 5
START_MAX_HEALTH = 3
ABSOLUT_MAX_HEALTH = 6

class Status(object):
    def __init__(self):
        super().__init__()
        self._level = 0 #type: int
        self._next_level = consts.LEVEL_1_POINTS
        self._points = 0 #type: int
        self._health = 3 # type: int
        self._font = pygame.font.Font('DejaVuSansMono.ttf', 18)
        self._dirty = True
        self._surface = None
        self._coffees = [animations.Coffee() for _ in range(START_MAX_HEALTH)]
        self._broken_coffee = animations.CoffeeBroken()

    def reset(self):
        self._level = 0
        self._next_level = consts.LEVEL_1_POINTS
        self._points = 0
        self._health = 3
        self._dirty = True


    def update(self, delta: int):
        variation_from = int(delta * .5)
        variation_to = int(delta * 2)
        for coffee in self._coffees:
            coffee.update(random.randint(variation_from, variation_to))
        self._broken_coffee.update(delta)
        if self._dirty:
            level_surface = self._font.render('level:  {}'.format(self._level), True, color.BLUEVIOLET, None)
            points_surface = self._font.render('points: {}'.format(self._points), True, color.BLUEVIOLET, None)
            #coffe_surface = self._font.render('coffee: {}'.format(self._health), True, color.BLUEVIOLET, None)
            level_surface_size = level_surface.get_size()
            points_surface_size = points_surface.get_size()
            #coffe_surface_size = coffe_surface.get_size()
            text_width = max(level_surface_size[0], points_surface_size[0]) #, coffe_surface_size[0])
            text_height = level_surface_size[1] + SPACING + points_surface_size[1] # + SPACING + coffe_surface_size[1]
            self._surface = pygame.Surface((text_width, text_height), pygame.SRCALPHA, None)
            self._surface.blit(points_surface, (0, 0))
            self._surface.blit(level_surface, (0, points_surface_size[1] + SPACING))
            #self._surface.blit(coffe_surface, (0, points_surface_size[1] + SPACING + level_surface_size[1] + SPACING))
            self._dirty = False

    def render(self, target: pygame.Surface):
        if self._surface is not None:
            target.blit(self._surface, (0, 20))
        offset = 60
        start = consts.SCREEN_W - 60
        count = 0
        for coffee in self._coffees:
            count += 1
            if count > self._health:
                self._broken_coffee.render(target, start - (offset * count), 20)
            else:
                coffee.render(target, start - (offset * count), 20)


    def inc_point(self, points: int = 1):
        self._points = max(0, self._points + points) # do not allow negative points
        if self._points >= self._next_level:
            self._level += 1
            self._health = min(START_MAX_HEALTH + self._level // 3, ABSOLUT_MAX_HEALTH)
            while len(self._coffees) < self._health:
                self._coffees.append(animations.Coffee())
            if self._level == 1:
                self._next_level = consts.LEVEL_2_POINTS
            elif self._level == 2:
                self._next_level = consts.LEVEL_3_POINTS
            elif self._level == 3:
                self._next_level = consts.LEVEL_4_POINTS
            elif self._level == 4:
                self._next_level = consts.LEVEL_5_POINTS
            else:
                self._next_level += consts.LEVEL_5_POINTS
        self._dirty = True

    def dec_health(self, health: int = 1):
        self._health -= health
        self._dirty = True

    health = property(lambda s: s._health)
    level = property(lambda s: s._level)
    points = property(lambda s: s._points)

