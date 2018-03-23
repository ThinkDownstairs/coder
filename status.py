import pygame
import typing
import consts
import color

class Stati(object):
    def __init__(self):
        self._level = 0 #type: int
        self._points = 0 #type: int
        self._health = 3 # type: int

    def render(self, screen: pygame.Surface):
        myfont = pygame.font.SysFont('Comic Sans MS', 16)
        textsurface = myfont.render('level: {}, points: {}'.format(str(self._points), str(self._level)), False, color.BLUEVIOLET)  # self._clock.get_fps()
        screen.blit(textsurface, (0, 20))

    def inc_point(self, points: int = 1):
        self._points += points

    def dec_health(self, health: int = 1):
        self._health -= health

    health = property(lambda s: s._health)

