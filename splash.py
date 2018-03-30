

import os
import state_manager

import menu
import highscore
import howto
import game
import quit_
import about
import consts
import locations

import pygame

class Splash(state_manager.State):
    def __init__(self) -> None:
        super().__init__()
        self._initialized = False
        self._was_rendered = False
        self._skip = False
        self._tick = 2500
        self._idx = 0
        self._splashs_loaded = False
        self._surfaces = [pygame.image.load(locations.image('metagamejam-splash.png')).convert_alpha()]



    def render(self) -> None:
        self.screen.blit(self._surfaces[min(len(self._surfaces) - 1, self._idx)], (0, 0))
        pygame.display.flip()
        self._was_rendered = True


    def input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_manager.terminate_main_loop()
            elif event.type == pygame.KEYDOWN:
                self._skip = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                l, m, r = pygame.mouse.get_pressed()
                if l == 1:
                    self._skip = True



    def update(self, delta: int, fps: float) -> None:
        if self._was_rendered:
            if not self._splashs_loaded:
                self._surfaces += [
                    pygame.image.load(locations.image('coder-splash.png')).convert_alpha(),
                    pygame.image.load(locations.image('thinkdownstairs-splash.png')).convert_alpha()]
                self._splashs_loaded = True
                return
            if self._initialized:
                if self._skip:
                    self._skip = False
                    self._idx += 1
                    self._tick = 2500
                    if self._idx >= len(self._surfaces):
                        self.state_manager.change_state(menu.Menu)
                    return
                self._tick -= delta
                if self._tick <= 0:
                    self._idx += 1
                    self._tick = 2500
                    if self._idx >= len(self._surfaces):
                        self.state_manager.change_state(menu.Menu)
                    return
            else:
                m = menu.Menu()
                m.add(menu.MenuEntry('Start', game.Game))
                m.add(menu.MenuEntry('HowTo', howto.HowTo))
                m.add(menu.MenuEntry('Highscore', highscore.Highscore))
                m.add(menu.MenuEntry('About', about.About))
                m.add(menu.MenuEntry('Quit', quit_.Quit))
                self.state_manager.add_state(m)
                self.state_manager.add_state(howto.HowTo())
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
