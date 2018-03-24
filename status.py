import pygame
import typing
import consts
import color

SPACING = 5

class Status(object):
    def __init__(self):
        super().__init__()
        self._level = 0 #type: int
        self._next_level = consts.LEVEL_1_POINTS
        self._points = 0 #type: int
        self._health = 3 # type: int
        self._font = pygame.font.Font('DejaVuSans.ttf', 18)
        self._dirty = True
        self._surface = None

    def update(self):
        if self._dirty:
            level_surface = self._font.render('level: {}'.format(self._level), True, color.BLUEVIOLET, None)
            points_surface = self._font.render('points: {}'.format(self._points), True, color.BLUEVIOLET, None)
            level_surface_size = level_surface.get_size()
            points_surface_size = points_surface.get_size()
            text_width = max(level_surface_size[0], points_surface_size[0])
            text_height = level_surface_size[1] + points_surface_size[1] + SPACING
            self._surface = pygame.Surface((text_width, text_height), pygame.SRCALPHA, None)
            self._surface.blit(points_surface, (0, 0))
            self._surface.blit(level_surface, (0, points_surface_size[1] + SPACING))
            self._dirty = False

    def render(self, target: pygame.Surface):
        if self._surface is not None:
            target.blit(self._surface, (0, 20))

    def inc_point(self, points: int = 1):
        self._points += points
        if self._points >= self._next_level:
            self._level += 1
            self._health = 3
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

