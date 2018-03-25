import state_manager
import pygame
import consts
import color
import player
import cursor
import bugs
import random
import snippets
import exceptions
import menu
import globals_
import status


class Game(state_manager.State):
    def __init__(self) -> None:
        super().__init__()
        pygame.font.init() # init fonts, do i have to do it here?
        self._cursor = cursor.Cursor() #my cursor :D
        self._go_manager = globals_.get_manager()
        self._status = status.Status()
        self._player = player.Player(self._status) # The one who shoots code snippets
        self.mouse_pos = (0, 0)
        self._w, self._h = pygame.display.get_surface().get_size()
        self._next_bug_count = 0 # type: int
        self._next_exception_count = 0 # type: int
        self._delta = 0 # type: int
        self._fps = 0 # type: float


    def render(self) -> None:
        self._screen.fill(color.BLACK)
        self._player.render(self.screen)
        self._cursor.render(self._screen, self.mouse_pos, color.LIGHTSEAGREEN)
        self._go_manager.render(self._screen)
        self._status.render(self._screen)

        myfont = pygame.font.SysFont('Comic Sans MS', 16)
        textsurface = myfont.render(str(self.mouse_pos) + " fps: " + str(int(self._fps)), False, color.BLUEVIOLET)  # self._clock.get_fps()
        self.screen.blit(textsurface, (0, 0))

        pygame.display.update()

    def input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_manager.terminate_main_loop()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.state_manager.change_state(menu.Menu)
            if event.type == pygame.MOUSEMOTION:
                self.mouse_pos = event.pos
                self._player.set_pos(self.mouse_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                l, m, r = pygame.mouse.get_pressed()
                if l == 1:
                    self._go_manager.add_object(self._player.fire())

    def update(self, delta: int, fps: float) -> None:
        self._delta = delta
        self._fps = fps
        self._next_bug_count -= delta
        self._next_exception_count -= delta
        self._go_manager.update(delta, self._player, self._status)

        if self._next_bug_count <= 0:
            self._go_manager.add_object(bugs.Bugs(self._status))
            self._next_bug_count = random.randint(*consts.MSEC_BETWEEN_BUGS[min(len(consts.MSEC_BETWEEN_BUGS) - 1, self._status.level)])

        if self._next_exception_count <= 0:
            self._go_manager.add_object(exceptions.Excepties(self._status))
            self._next_exception_count = random.randint(*consts.MSEC_BETWEEN_EXCEPTIONS[min(len(consts.MSEC_BETWEEN_EXCEPTIONS) - 1, self._status.level)])

        if self._status.health <= 0:
            self.state_manager.change_state(menu.Menu) ## TODO : game over state  and/or highscore
        self._status.update()

    def leave(self, next_: state_manager.StateType) -> None:
        pass

    def enter(self, prev_: state_manager.StateType) -> None:
        if prev_ == menu.Menu:
            self._go_manager.clear_objects()

