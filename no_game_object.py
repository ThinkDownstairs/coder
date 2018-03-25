
import pygame
import animation
import game_objects
import globals_


class NoGameObject(game_objects.GameObject):
    def __init__(self, animation_: animation.Animation, x: int, y: int):
        super().__init__()
        self._x = x
        self._y = y
        self._animation = animation_
        globals_.get_manager().add_object(self)

    def render(self, target: pygame.Surface) -> None:
        self._animation.render(target, self._x, self._y)

    def update(self, delta: int):
        if self._animation.done:
            self.delete()
        else:
            self._animation.update(delta)

    def _get_surface(self):
        return self._animation.surface

