
import pygame
import state_manager
import consts

from collections import namedtuple

Entry = namedtuple('Entry', ['player', 'level', 'points', 'timestamp'])
MAX_ENTRIES = 10

class Highscore(state_manager.State):
    def __init__(self, new_entry: Entry = None) -> None:
        super().__init__()
        self._entries = []
        self._new_entry = new_entry
        self._input_str = None if new_entry is None else ''
        self._input_font = pygame.font.Font('DejaVuSansMono.ttf', 24)
        self._input_surface = None
        self._entry_font = pygame.font.Font('DejaVuSans.ttf', 20)
        self._new_entry_font = pygame.font.Font('DejaVuSans-Bold.ttf', 20)
        self._entry_surfaces = None

    def _render_input(self):
        return self._input_font.render('Your Name: {:12}'.format(self._input_str), True, (255, 255, 255), None)

    def _addch(self, ch: str):
        if self._input_str is not None:
            if len(self._input_str) < 12:
                self._input_str += ch
                self._input_surface = self._render_input()
            print(self._input_str)

    def _clrch(self):
        if self._input_str is not None:
            if len(self._input_str) > 0:
                self._input_str = self._input_str[:-1]
                self._input_surface = self._render_input()
            print(self._input_str)

    def _done(self):
        new_entry = Entry(self._input_str, self._new_entry.level, self._new_entry.points, self._new_entry.timestamp)
        len_entries = len(self._entries)
        for i in range(MAX_ENTRIES):
            if i < len_entries:
                entry = self._entries[i]
                if new_entry.points >= entry.points:
                    # TODO : add
                    break
            else:
                # TODO : just add it here, there are less than MAX_ENTRIES entries
                break
        self._input_str = None


    def render(self) -> None:
        self.screen.fill((0, 0, 0))
        if self._input_str is not None:
            if self._input_surface is None:
                self._input_surface = self._render_input()
            self.screen.blit(self._input_surface, (consts.SCREEN_W // 2 - self._input_surface.get_width() // 2, 10))
        top = 100
        if self._entry_surfaces is not None:
            for entry_surface in self._entry_surfaces:
                self.screen.blit(entry_surface, (10, top))
                top += (entry_surface.get_height() * 1.3)
        pygame.display.flip()


    def input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_manager.terminate_main_loop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self._clrch()
                elif event.key == pygame.K_RETURN:
                    self._done()
                else:
                    ch = event.unicode
                    self._addch(ch)


    def update(self, delta: int, fps: float) -> None:
        if self._entry_surfaces is None:
            self._entry_surfaces = []
            for entry in self._entries:
                surface = self._entry_font.render('{timestamp:%Y-%m-%d %H:%M:%S} {player:12} {level:6} {points}'.format(
                    timestamp=entry.timestamp,
                    player=entry.player,
                    level=entry.level,
                    points=entry.points),
                    True,
                    (255, 255, 255),
                    None)
                self._entry_surfaces.append(surface)

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

