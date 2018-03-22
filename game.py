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
import go_manager

class Game(state_manager.State):
  def __init__(self) -> None:
    super().__init__()
    pygame.font.init() # init fonts, do i have to do it here?
    self._player = player.Player() # The one who shoots code snippets
    self._cursor = cursor.Cursor() #my cursor :D
    self._go_manager = go_manager.GoManager()
    self.mouse_pos = (0, 0)
    self._w, self._h = pygame.display.get_surface().get_size()
    self._next_bug_count = 0 # type: int
    self._delta = 0 # type: int
    self._fps = 0 # type: float
    self._except_list = None # type: List[exceptions.Excepties]


  def render(self) -> None:
    self._screen.fill(color.BLACK)
    self._player.render(self.screen)
    self._cursor.render(self._screen, self.mouse_pos, color.LIGHTSEAGREEN)
    self._go_manager.render(self._screen)

    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render(str(self.mouse_pos) + " fps: " + str(int(self._fps)), False, color.BLUEVIOLET)  # self._clock.get_fps()
    self.screen.blit(textsurface, (0, 0))

    pygame.display.update()

  def input(self) -> None:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.state_manager.terminate_main_loop()
      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        self.state_manager.terminate_main_loop()
      if event.type == pygame.MOUSEMOTION:
        self.mouse_pos = event.pos
      if event.type == pygame.MOUSEBUTTONDOWN:
        l, m, r = pygame.mouse.get_pressed()
        if l == 1:
          self._go_manager.add_object(snippets.Snippet(color.POWDERBLUE, self.mouse_pos[0]))
    self._player.input(self.mouse_pos)

  def update(self, delta: int, fps: float) -> None:
    self._delta = delta
    self._fps = fps
    self._next_bug_count -= delta
    self._go_manager.update(delta, self._player)
    if self._next_bug_count < 0:
      self._go_manager.add_object(bugs.Bugs(color.PURPLE2, random.randint(30, 600), random.randint(30, 600)))
      #for every bug comes an exception
      self._go_manager.add_object(exceptions.Excepties(color.BISQUE1))
      self._next_bug_count = random.randint(1500, 3500)

  def leave(self) -> None:
    pass

  def enter(self) -> None:
    pass
    
