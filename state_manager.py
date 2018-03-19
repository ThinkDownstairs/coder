import pygame
from typing import Type
from typing import Dict

class State(object):
  def __init__(self) -> None:
    super().__init__()
    self._state_manager = None
    self._screen = None

  def set_state_manager(self, state_manager):
    self._state_manager = state_manager
    self._screen = state_manager.screen
    

  def render(self) -> None:
    pass

  def input(self) -> None:
    pass

  def update(self, delta: int, fps: float) -> None:
    pass

  def leave(self) -> None:
    pass

  def enter(self) -> None:
    pass

  state_manager = property(lambda s: s._state_manager)
  screen = property (lambda self: self._screen)

StateType = Type[State]

class StateManager(object):

  def __init__(self, screen) -> None:
    super().__init__()
    self._running = True # type: bool
    self._current = None # type: state.State
    self._next = None # type: state.State
    self._states = {} # type: Dict[state.StateType, state.State]
    self._screen = screen
    self._clock = pygame.time.Clock() # type: pygame.time.Clock
    self._delta = 0 # type: int
    self._fps = 0 # type: float

  def terminate_main_loop(self) -> None:
    self._running = False

  def add_state(self, state: State) -> None:
    self._states[type(state)] = state
    state.set_state_manager(self)
    if self._current is None:
      self.change_state(type(state))

  def has_state(self, state_type: StateType) -> bool:
    return state_type in self._states

  def change_state(self, state_type: StateType) -> None:
    self._next = self._states.get(state_type, None)

  def main_loop(self) -> None:
    self._running = True
    while self._running:
      self._fps = self._clock.get_fps()
      self._delta = self._clock.tick(250) # Here i get the ms 
      if self._next is not None:
        if self._current is not None:
          self._current.leave()
        self._current = self._next
        self._current.enter()
        self._next = None
      self._current.render()
      self._current.input()
      self._current.update(self._delta, self._fps)
  current = property (lambda self: self._current)
  next = property (lambda self: self._next)
  screen = property (lambda self: self._screen)