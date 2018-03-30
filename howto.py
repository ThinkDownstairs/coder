import state_manager
import pygame
import os
import locations
import menu

class HowTo(state_manager.State):
    def __init__(self) -> None:
        super().__init__()
        self._tick = 3000
        self._skip = False
        self._surface = pygame.image.load(locations.image('quit.png')).convert_alpha()


    def render(self) -> None:
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
        self._tick -= delta
        if self._skip or self._tick <= 0:
            self.state_manager.change_state(menu.Menu)

    def leave(self, next_: state_manager.StateType) -> None:
        pass

    def enter(self, prev_: state_manager.StateType) -> None:
        self._tick = 3000
