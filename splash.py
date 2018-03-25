

import os
import state_manager

import menu
import consts

import pygame

class Splash(state_manager.State):
    def __init__(self) -> None:
        super().__init__()
        self._count = 2500
        self._surface = pygame.image.load(os.path.join('res', 'export', 'metagamejam.png')).convert_alpha()


    def render(self) -> None:
        self.screen.blit(self._surface, (0, 0))
        pygame.display.flip()


    def input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_manager.terminate_main_loop()
            elif event.type == pygame.KEYDOWN:
                self.state_manager.change_state(menu.Menu)


    def update(self, delta: int, fps: float) -> None:
        self._count -= delta
        if self._count <= 0:
            self.state_manager.change_state(menu.Menu)


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
