
from collections import namedtuple

import state_manager
import background
import sound
import quit_

import pygame
import consts


class MenuEntry(object):
    def __init__(self, name: str, typ) -> None:
        super().__init__()
        self._name = name
        self._typ = typ
        self._surface = None
        self._surface_selected = None
        self._x = 0
        self._y = 0
        self._h = 0
        self._w = 0

    def prepare(self, font: pygame.font.Font, font_selected: pygame.font.Font) -> None:
        surface = font.render(self._name, True, (255, 255, 255), None)
        surface_selected = font_selected.render(self._name, True, (255, 255, 255), None)
        self._w = max(surface.get_width(), surface_selected.get_width()) + 20
        self._h = max(surface.get_height(), surface_selected.get_height()) + 10
        self._surface = pygame.Surface((self._w, self._h), pygame.SRCALPHA, None)
        self._surface.blit(surface, (self._w // 2 - surface.get_width() // 2, self._h // 2 - surface.get_height() // 2))
        self._surface_selected = pygame.Surface((self._w, self._h), pygame.SRCALPHA, None)
        self._surface_selected.fill((0, 0, 0))
        self._surface_selected.blit(surface_selected, (self._w // 2 - surface_selected.get_width() // 2, self._h // 2 - surface_selected.get_height() // 2))

    def contains_pos(self, x: int, y: int) -> bool:
        return (self._x < x < (self._x + self._surface.get_width())) and (self._y < y < (self._y + self._surface.get_height()))

    def set_pos(self, x: int, y: int):
        self._x = x
        self._y = y

    def render(self, target: pygame.Surface, selected: bool):
        s = self._surface_selected if selected else self._surface
        target.blit(s, (self._x, self._y))
        if selected:
            pygame.draw.rect(target, (255, 255, 255), (self._x, self._y, s.get_width(), s.get_height()), 3)

    def __hash__(self):
        return hash(self._name)
    def __eq__(self, other):
        return hash(self) == hash(other)

    height = property(lambda s: s._h)
    width = property(lambda s: s._w)
    typ = property(lambda s: s._typ)




class Menu(state_manager.State):
    def __init__(self) -> None:
        super().__init__()
        self._menu_entries = []
        self._initialized = False
        self._mouse = (consts.SCREEN_W + 1, consts.SCREEN_H + 1)
        self._idx = 0
        self._background = None
        self._font = pygame.font.Font('DejaVuSansMono.ttf', 24)
        self._font_selected = pygame.font.Font('DejaVuSansMono-Bold.ttf', 28)
        self._sound = sound.Sound()

    def add(self, menu_entry: MenuEntry):
        menu_entry.prepare(self._font, self._font_selected)
        self._menu_entries.append(menu_entry)

    def select(self, idx: int) -> None:
        if idx != self._idx:
            self._idx = idx % len(self._menu_entries)
            self._sound.play(sound.Sounds.MENU_HOVER)

    def render(self) -> None:
        self.screen.fill((0, 0, 0))
        self._background.render(self.screen)
        for i in range(len(self._menu_entries)):
            self._menu_entries[i].render(self.screen, self._idx == i)
        pygame.draw.line(self.screen, (255, 255, 255), (self._mouse[0], self._mouse[1] - 10), (self._mouse[0], self._mouse[1] + 10), 2)
        pygame.draw.line(self.screen, (255, 255, 255), (self._mouse[0] - 10, self._mouse[1]), (self._mouse[0] + 10, self._mouse[1]), 2)
        #pygame.draw.rect(self.screen, (255, 255, 255), (*self._mouse, 10, 10))
        pygame.display.flip()

    def input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_manager.change_state(quit_.Quit)
            elif event.type == pygame.KEYDOWN:
                i = 0
                if event.key in (pygame.K_UP, pygame.K_LEFT):
                    i = -1
                elif event.key in (pygame.K_DOWN, pygame.K_RIGHT):
                    i = 1
                if i != 0:
                    self.select(self._idx + i)
                    continue
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    me = self._menu_entries[self._idx]
                    self._sound.play(sound.Sounds.MENU_SELECT)
                    self.state_manager.change_state(me.typ)
                    continue
            elif event.type == pygame.MOUSEMOTION:
                self._mouse = event.pos
                for i in range(len(self._menu_entries)):
                    if self._menu_entries[i].contains_pos(*self._mouse):
                        self.select(i)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                l, m, r = pygame.mouse.get_pressed()
                if l == 1:
                    me = self._menu_entries[self._idx]
                    if me.contains_pos(*self._mouse):
                        self._sound.play(sound.Sounds.MENU_SELECT)
                        self.state_manager.change_state(me.typ)

    def update(self, delta: int, fps: float):
        self._background.update(delta)


    def enter(self, prev_: state_manager.StateType) -> None:
        self._background = background.FloatingEditors(consts.SCREEN_W, consts.SCREEN_H)
        self._idx = 0
        if not self._initialized:
            h = sum([me.height + 10 for me in self._menu_entries])
            w = max([me.width for me in self._menu_entries])
            offset = h // len(self._menu_entries)
            t = consts.SCREEN_H // 2 - h // 2
            for i in range(len(self._menu_entries)):
                self._menu_entries[i].set_pos(consts.SCREEN_W // 2 - self._menu_entries[i].width // 2, t)
                t += offset
            self._initialized = True


if __name__ == '__main__':
    import game
    import about
    def init():
        pygame.init()
        screen = pygame.display.set_mode((consts.SCREEN_W, consts.SCREEN_H))
        pygame.display.set_caption('Coder')
        pygame.mouse.set_visible(0)
        return screen
    sm = state_manager.StateManager(init())
    m = Menu()
    m.add(MenuEntry('Start', game.Game))
    m.add(MenuEntry('About', about.About))
    m.add(MenuEntry('Quit', None))
    sm.add_state(m)
    sm.add_state(game.Game())
    sm.add_state(about.About())
    sm.change_state(Menu)
    sm.main_loop()

