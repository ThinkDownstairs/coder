import pygame
import color
import consts


class Cursor():
    def __init__(self) -> None:
        self.rect = None
        self._textsurface = None

    def render(self, screen, mouse_pos, p_color):    
        self.rect = (mouse_pos[0], mouse_pos[1], consts.CURSOR_W, consts.CURSOR_H)
        pygame.draw.rect(screen, p_color, self.rect, 0)
