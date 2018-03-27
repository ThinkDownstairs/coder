

import os
import state_manager

import menu
import highscore
import game
import quit_
import about
import consts

import pygame

class Splash(state_manager.State):
    def __init__(self) -> None:
        super().__init__()
        self._initialized = False
        self._was_rendered = False
        self._skip = False
        self._count = 2500
        self._surface = pygame.image.load(os.path.join('res', 'export', 'metagamejam.png')).convert_alpha()


    def render(self) -> None:
        self.screen.blit(self._surface, (0, 0))
        pygame.display.flip()
        self._was_rendered = True


    def input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_manager.terminate_main_loop()
            elif event.type == pygame.KEYDOWN:
                self._skip = True


    def update(self, delta: int, fps: float) -> None:
        if self._was_rendered:
            if self._initialized:
                if self._skip:
                    self.state_manager.change_state(menu.Menu)
                    return
                self._count -= delta
                if self._count <= 0:
                    self.state_manager.change_state(menu.Menu)
                    return
            else:
                m = menu.Menu()
                m.add(menu.MenuEntry('Start', game.Game))
                m.add(menu.MenuEntry('Highscores', highscore.Highscore))
                m.add(menu.MenuEntry('About', about.About))
                m.add(menu.MenuEntry('Quit', quit_.Quit))
                self.state_manager.add_state(m)
                self.state_manager.add_state(highscore.Highscore())
                self.state_manager.add_state(game.Game())
                self.state_manager.add_state(about.About())
                self.state_manager.add_state(quit_.Quit())
                self._initialized = True



if __name__ == '__main__':
    def init():
        pygame.init()
        screen = pygame.display.set_mode((consts.SCREEN_W, consts.SCREEN_H))
        pygame.display.set_caption('Coder')
        pygame.mouse.set_visible(0)
        return screen
    sm = state_manager.StateManager(init())
    s = Splash()
    sm.add_state(s)
    sm.change_state(Splash)
    sm.main_loop()
