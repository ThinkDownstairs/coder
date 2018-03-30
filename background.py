
from typing import List

import pygame
import color
import locations

from collections import namedtuple
import random
import animations

class FloatingEditors(object):
    class Editor(object):
        def __init__(self, x, y, velocity, surface) -> None:
            super().__init__()
            self.x = int(x)
            self.y = y
            self.velocity = velocity
            self.surface = surface

    def __init__(self, w: int, h: int) -> None:
        super().__init__()
        self._items = []
        self._editors = [
            animations.Player(animations.Surfaces.ATOM).surface,
            animations.Player(animations.Surfaces.VIM).surface,
            animations.Player(animations.Surfaces.EMACS).surface,
            animations.Player(animations.Surfaces.VSCODE).surface,
            animations.Player(animations.Surfaces.INTELLIJ).surface,
            animations.Player(animations.Surfaces.NANO).surface]
        self._next_editor = 0
        self._w = w
        self._h = h

    def update(self, delta: int):
        for item in self._items:
            item.y -= (item.velocity * delta)
        self._next_editor -= delta
        if self._next_editor <= 0:
            editor = self._editors[random.randint(0, len(self._editors) - 1)]
            self._items.append(FloatingEditors.Editor(
                random.randint(0, self._w - editor.get_width()), self._h - 5,
                .10 + random.random() * .25,
                editor))
            self._next_editor = random.randint(50, 500)
        self._items = [item for item in self._items if item.y > -100]


    def render(self, target: pygame.Surface):
        for item in self._items:
            target.blit(item.surface, (item.x, int(item.y)))



class Matrix(object):
    __slots__ = ('_chars', '_surfaces', '_tick', '_width', '_height', '_max_idx', '_min_new', '_max_new')

    class Char(object):
        __slots__ = ('x', 'y', 'v', 'surface')
        def __init__(self, x, y, velocity, surface) -> None:
            super().__init__()
            self.x = int(x)
            self.y = y
            self.v = velocity
            self.surface = surface

    def __init__(self, w: int, h: int) -> None:
        super().__init__()
        self._chars = [] # type: List[Char]
        self._surfaces = [] # type: List[chr, pygame.Surface]
        self._max_idx = len(self._surfaces)
        self._tick = 0
        self._width = w
        self._height = h
        self._min_new = max(1, w // 120)
        self._max_new = max(2, w // 30)
        self._init_surfaces()

    def _init_surfaces(self):
        CHARS = '#+!{}[]&%$?' + ''.join(map(chr, range(ord('a'), ord('z')))) + ''.join(map(chr, range(ord('A'), ord('Z'))))
        font = pygame.font.Font(locations.font('DejaVuSansMono.ttf'), 12)
        surface = font.render(CHARS, True, (70, 150, 25), None).convert_alpha()
        width = surface.get_width() // len(CHARS)
        height = surface.get_height()
        for i in range(len(CHARS)):
            subsurface = surface.subsurface((i * width, 0, width, height))
            self._surfaces.append(subsurface)
        self._max_idx = len(self._surfaces) - 1

    def update(self, delta: int) -> None:
        self._tick -= delta
        if self._tick <= 0:
            for i in range(random.randint(self._min_new, self._max_new)):
                c = Matrix.Char(random.randint(1, self._width), -10, .15 + (random.random() * .2), self._surfaces[random.randint(0, self._max_idx)])
                self._chars.append(c)
            self._tick = 125
            self._chars = [c for c in self._chars if c.y < self._height]
        for c in self._chars:
            c.y += (c.v * delta)

    def render(self, target: pygame.Surface) -> None:
        target.fill(color.GRAY12)
        for c in self._chars:
            target.blit(c.surface, (c.x, int(c.y)))



if __name__ == '__main__':
    SIZE = 600, 600
    pygame.init()
    screen = pygame.display.set_mode(SIZE, pygame.DOUBLEBUF)
    clock = pygame.time.Clock()
    running = True
    delta = 0
    b = Matrix(*SIZE)
    fpss = []
    min_fps = -1000
    while running:
        # INPUT
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                continue
        # UPDATE
        b.update(delta)
        # RENDER
        b.render(screen)
        #pygame.display.flip()
        pygame.display.update()
        # TICK
        delta = clock.tick(1000)
        #fps = 1000 / delta
        #if len(fpss) > 100:
        #    print('avg fps {:.1f}    min fps: {:.1f}'.format(sum(fpss) / 100, min(fpss)))
        #    if min_fps < 0:
        #        min_fps = 1000 # hack to ignore the first run
        #    elif min(fpss) < min_fps:
        #        min_fps = min(fpss)
        #    fpss = []
        #fpss.append(fps)
    #print('MIN: {:.2f}'.format(min_fps))
