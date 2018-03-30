
import state_manager
import pygame
import os
import animations
import quit_
import menu
import consts


LEFT = 25
TOP = 5
STEP = 20
WIDTH = 90
HEIGHT = 90

ATOM_TEXT = """ """
EMACS_TEXT = """ """
INTELLIJ_TEXT = """ """
NANO_TEXT = """ """
VIM_TEXT = """ """
VSCODE_TEXT = """ """
RANDOM_TEXT = """ """


chosen_editor = None

class Chooser(state_manager.State):
    def __init__(self) -> None:
        super().__init__()
        self._idx = 0
        self._mouse = (consts.SCREEN_W + 1, consts.SCREEN_H + 1)
        font = pygame.font.Font('DejaVuSansMono.ttf', 20)
        self._texts = [
            font.render(ATOM_TEXT, True, (255, 255, 255), None),
            font.render(EMACS_TEXT, True, (255, 255, 255), None),
            font.render(INTELLIJ_TEXT, True, (255, 255, 255), None),
            font.render(NANO_TEXT, True, (255, 255, 255), None),
            font.render(VIM_TEXT, True, (255, 255, 255), None),
            font.render(VSCODE_TEXT, True, (255, 255, 255), None),
            font.render(RANDOM_TEXT, True, (255, 255, 255), None)]
        self._animations = [
            animations.Player(animations.Surfaces.ATOM),
            animations.Player(animations.Surfaces.EMACS),
            animations.Player(animations.Surfaces.INTELLIJ),
            animations.Player(animations.Surfaces.NANO),
            animations.Player(animations.Surfaces.VIM),
            animations.Player(animations.Surfaces.VSCODE),
            animations.RandomEditor()]

    def _select(self, clicked: bool):
        global chosen_editor
        x, y = self._mouse
        if TOP < y < (HEIGHT + TOP):
            for i in range(len(self._animations)):
                if (LEFT + i * (WIDTH + STEP)) < x < ((LEFT + i * (WIDTH + STEP)) + WIDTH):
                    self._idx = i
                    if clicked:
                        if isinstance(self._animations[self._idx], animations.Player):
                            chosen_editor = self._animations[self._idx]
                        else:
                            chosen_editor = None
                        self.state_manager.change_state(menu.Menu)
                    break


    def render(self) -> None:
        left = LEFT
        top = TOP
        step = STEP
        self.screen.fill((0, 0, 0))
        for i in range(len(self._animations)):
            s = self._animations[i].surface
            w, h = s.get_size()
            self.screen.blit(s, (left, top))
            if i == self._idx:
                pygame.draw.rect(self.screen, (255, 255, 255), (left - 2, top - 2, w + 4, h + 4), 3)
            left += (w + step)
        self.screen.blit(self._texts[self._idx], (LEFT, TOP + HEIGHT + (3 * STEP)))
        pygame.draw.line(self.screen, (255, 255, 255), (self._mouse[0], self._mouse[1] - 10), (self._mouse[0], self._mouse[1] + 10), 2)
        pygame.draw.line(self.screen, (255, 255, 255), (self._mouse[0] - 10, self._mouse[1]), (self._mouse[0] + 10, self._mouse[1]), 2)
        pygame.display.flip()

    def input(self) -> None:
        global chosen_editor
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_manager.change_state(quit_.Quit)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._idx -= 1
                    if self._idx < 0:
                        self._idx = len(self._animations) - 1
                elif event.key == pygame.K_RIGHT:
                    self._idx += 1
                    if self._idx >= len(self._animations):
                        self._idx = 0
                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    if isinstance(self._animations[self._idx], animations.Player):
                        chosen_editor = self._animations[self._idx]
                    else:
                        chosen_editor = None
                    self.state_manager.change_state(menu.Menu)
                elif event.key == pygame.K_ESCAPE:
                    self.state_manager.change_state(menu.Menu)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                l, m, r = pygame.mouse.get_pressed()
                if l == 1:
                    self._select(True)
            elif event.type == pygame.MOUSEMOTION:
                self._mouse = event.pos
                self._select(False)


    def update(self, delta: int, fps: float) -> None:
        for animation in self._animations:
            animation.update(delta)

    def leave(self, next_: state_manager.StateType) -> None:
        pass

    def enter(self, prev_: state_manager.StateType) -> None:
        global chosen_editor
        if chosen_editor is None:
            self._idx = len(self._animations) - 1
        else:
            for i in range(len(self._animations)):
                if self._animations[i] == chosen_editor:
                    self._idx = i
                    break
