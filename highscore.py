
import os
import pickle

import pygame
import state_manager
import consts
import menu
import quit_

import background
import locations

from collections import namedtuple

Entry = namedtuple('Entry', ['player', 'level', 'points', 'timestamp'])
MAX_ENTRIES = 10

class Highscore(state_manager.State):
    def __init__(self, new_entry: Entry = None) -> None:
        super().__init__()
        self._entries = []
        self._count = 0
        self._new_entry = new_entry
        self._input_str = None if new_entry is None else ''
        self._input_font = pygame.font.Font('DejaVuSansMono.ttf', 24)
        self._input_surface = None
        self._count_surface = None
        self._new_points_surface = None
        self._entry_font = pygame.font.Font('DejaVuSansMono.ttf', 20)
        self._new_entry_font = pygame.font.Font('DejaVuSansMono-Bold.ttf', 20)
        self._entry_surfaces = None
        self._background = None
        self._filename = locations.user('highscore.dat')

    def _load(self):
        if os.path.exists(self._filename):
            with open(self._filename, 'rb') as f:
                data = pickle.load(f)
                v = data.get('version', 0)
                if v == 1:
                    self._entries = data.get('entries', [])
                    self._count = data.get('count', 0)
                else:
                    raise Exception('Unknown Highscore Data Version')

    def _save(self):
        with open(self._filename, 'wb') as f:
            data = {
                'version': 1,
                'entries': self._entries,
                'count': self._count}
            pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

    def _render_input(self):
        return self._input_font.render('Your Name: {:_<12}'.format(self._input_str), True, (255, 255, 255), None)

    def _render_new_points(self):
        return self._input_font.render('Level: {}    Points: {}'.format(self._new_entry.level, self._new_entry.points), True, (255, 255, 255), None)

    def _render_played_games(self):
        return self._entry_font.render('Played Games: {}'.format(self._count), True, (40, 210, 40), None)


    def _render_entry_surfaces(self):
        self._entry_surfaces = [self._entry_font.render('     TIMESTAMP             PLAYER         LEVEL         POINTS', True, (40, 210, 40), None)]
        for entry in self._entries:
            if entry == self._new_entry:
                font = self._new_entry_font
                color = (0, 255, 0)
            else:
                font = self._entry_font
                color = (40, 210, 40)
            surface = font.render('{timestamp:%Y-%m-%d %H:%M:%S}     {player:^12}     {level:0>7}     {points:0>12}'.format(
                timestamp=entry.timestamp,
                player=entry.player,
                level=entry.level,
                points=entry.points),
                True,
                color,
                None)
            self._entry_surfaces.append(surface)

    def _addch(self, ch: str):
        if self._input_str is not None:
            if len(self._input_str) < 12:
                self._input_str += ch
                self._input_surface = self._render_input()

    def _clrch(self):
        if self._input_str is not None:
            if len(self._input_str) > 0:
                self._input_str = self._input_str[:-1]
                self._input_surface = self._render_input()

    def _done(self):
        if self._input_str is not None:
            self._new_entry = Entry(self._input_str, self._new_entry.level, self._new_entry.points, self._new_entry.timestamp)
            len_entries = len(self._entries)
            for i in range(MAX_ENTRIES):
                if i < len_entries:
                    entry = self._entries[i]
                    if self._new_entry.points >= entry.points:
                        self._entries.insert(i, self._new_entry)
                        self._entry_surfaces = None # i want to rerender them
                        break
                else:
                    self._entries.insert(i, self._new_entry)
                    self._entry_surfaces = None # i want to rerender them
                    break
            if len(self._entries) > MAX_ENTRIES:
                self._entries = self._entries[:MAX_ENTRIES]
            self._save()
            self._input_str = None


    def render(self) -> None:
        #self.screen.fill((0, 0, 0))
        self._background.render(self.screen)
        if self._input_str is not None:
            if self._input_surface is None:
                self._input_surface = self._render_input()
            self.screen.blit(self._input_surface, (consts.SCREEN_W // 2 - self._input_surface.get_width() // 2, 10))
            if self._new_points_surface is None:
                self._new_points_surface = self._render_new_points()
            self.screen.blit(self._new_points_surface, (consts.SCREEN_W // 2 - self._new_points_surface.get_width() // 2, 10 + self._new_points_surface.get_height() + 10))
        if self._entry_surfaces is None:
            self._render_entry_surfaces()
        top = 140
        step = 1.8
        for entry_surface in self._entry_surfaces:
            self.screen.blit(entry_surface, (10, top))
            top += (entry_surface.get_height() * step)
            step = 1.4
        if self._count_surface is None:
            self._count_surface = self._render_played_games()
        self.screen.blit(self._count_surface, (10, top + 10))
        pygame.display.flip()


    def input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_manager.change_state(quit_.Quit)
            if event.type == pygame.KEYDOWN:
                if self._input_str is None:
                    self.state_manager.change_state(menu.Menu)
                if event.key == pygame.K_BACKSPACE:
                    self._clrch()
                elif event.key == pygame.K_RETURN:
                    self._done()
                elif event.key == pygame.K_ESCAPE:
                    self.state_manager.change_state(menu.Menu)
                else:
                    ch = event.unicode
                    self._addch(ch)


    def update(self, delta: int, fps: float) -> None:
        self._background.update(delta)

    def enter(self, prev_):
        self._load()
        self._background = background.Matrix(consts.SCREEN_W, consts.SCREEN_H)
        self._render_entry_surfaces()
        if self._input_str is not None:
            self._count += 1
        self._count_surface = self._render_played_games()

    def leave(self, next_):
        self._new_entry = None

if __name__ == '__main__':
    import consts
    def init():
        pygame.init()
        screen = pygame.display.set_mode((consts.SCREEN_W, consts.SCREEN_H))
        pygame.display.set_caption('Coder')
        pygame.mouse.set_visible(0)
        return screen
    sm = state_manager.StateManager(init())
    sm.add_state(Highscore(Entry('', 8, 1234, '2018-03-26 22:01:32')))
    sm.change_state(Highscore)
    sm.main_loop()

