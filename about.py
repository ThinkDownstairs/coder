
import state_manager
import background

import menu

import pygame
import consts

SPEED = 0.1

ABOUT = [
    r'    ____          _            ',
    r'   / ___|___   __| | ___ _ __  ',
    r"  | |   / _ \ / _` |/ _ \ '__| ",
    r'  | |__| (_) | (_| |  __/ |    ',
    r'   \____\___/ \__,_|\___|_|    ',
    '',
    'a game for the MetaGameJam 17-31 March 2018',
    '',
    '',
    '~~~~~~~~~~~~',
    'idea, code, graphics',
    '',
    'Daniel Nimmervoll',
    'Lukas Singer',
    '~~~~~~~~~~~~',
    '',
    '',
    '~~~~~~~~~~~~',
    'sounds',
    '',
    'OpenGameArt.org',
    ''
    'Effects:',
    'Prinsu-Kun', # dead.wav
    'qubodup', # insectoralien.flac
    'Ogrebane', # teleport.wav
    'Sudocolon', # menu_choise.mp3
    ''
    'Song:',
    'CH-AY-NA by Sprint',
    '~~~~~~~~~~~~',
    '',
    '',
    '~~~~~~~~~~~~',
    'tools',
    '',
    'vim',
    'vscode',
    'gimp',
    'inkscape',
    'audacity',
    'python',
    'pyinstaller',
    'pygame',
    '~~~~~~~~~~~~',
    '',
    '',
    '~~~~~~~~~~~~',
    'special thanks',
    '',
    'Jana F.',
    'Melanie D.',
    '~~~~~~~~~~~~',
    '',
    '',
    '~~~~~~~~~~~~',
    '',
    'THANKS FOR PLAYING',
    '',
    '~~~~~~~~~~~~',
    '~~~~~~~~~~',
    '~~~~~~~~',
    '~~~~~~',
    '~~~~',
    '~~',
    '']


class About(state_manager.State):
    def __init__(self) -> None:
        super().__init__()
        self._surface = None
        self._background = None
        self._y = None

    def _render_surface(self):
        font = pygame.font.Font('DejaVuSansMono.ttf', 20)
        top = 0
        line_height = int(font.get_height() * 1.3)
        self._surface = pygame.Surface((consts.SCREEN_W, line_height * (len(ABOUT) + 2)), pygame.SRCALPHA, None)
        for txt in ABOUT:
            surf = font.render(txt, True, (255, 255, 255), None)
            self._surface.blit(surf, (self._surface.get_width() // 2 - surf.get_width() // 2, int(top)))
            top += line_height

    def render(self) -> None:
        self._background.render(self.screen)
        self.screen.blit(self._surface, (0, int(self._y)))
        pygame.display.flip()

    def input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_manager.terminate_main_loop()
            elif event.type == pygame.KEYDOWN:
                self.state_manager.change_state(menu.Menu)


    def update(self, delta: int, fps: float) -> None:
        self._y -= (SPEED * delta)
        if self._y < -self._surface.get_height():
            self.state_manager.change_state(menu.Menu)
        self._background.update(delta)

    def leave(self, next_: state_manager.StateType) -> None:
        pass

    def enter(self, prev_: state_manager.StateType) -> None:
        if self._surface is None:
            self._render_surface()
        # always create a new background,
        # so that characters start falling from the top :-)
        self._background = background.Matrix(consts.SCREEN_W, consts.SCREEN_H)
        self._y = consts.SCREEN_H + 1

if __name__ == '__main__':
    def init():
        pygame.init()
        screen = pygame.display.set_mode((consts.SCREEN_W, consts.SCREEN_H))
        pygame.display.set_caption('Coder')
        pygame.mouse.set_visible(0)
        return screen
    sm = state_manager.StateManager(init())
    a = About()
    sm.add_state(a)
    sm.change_state(About)
    sm.main_loop()
