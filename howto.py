import state_manager
import pygame
import os
import locations
import menu
import color
import background
import consts

class HowTo(state_manager.State):
    def __init__(self) -> None:
        super().__init__()
        self._skip = False
        self._surface = pygame.image.load(locations.image('howto-splash.png')).convert_alpha()
        self._background = background.FloatingEditors(consts.SCREEN_W, consts.SCREEN_H)


    def render(self) -> None:
        self.screen.fill(color.GRAY12)
        self._background.render(self.screen)
        self.screen.blit(self._surface, (0, 0))
        pygame.display.flip()

    def input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._skip = True
            elif event.type == pygame.KEYDOWN:
                self._skip = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                l, m, r = pygame.mouse.get_pressed()
                if l == 1:
                    self._skip = True


    def update(self, delta: int, fps: float) -> None:
        self._background.update(delta)
        if self._skip:
            self.state_manager.change_state(menu.Menu)

    def leave(self, next_: state_manager.StateType) -> None:
        self._skip = False

    def enter(self, prev_: state_manager.StateType) -> None:
        pass
