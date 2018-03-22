import pygame
import color
import consts


class Player(object):
    def __init__(self) -> None:
        self._rect = None
        self._textsurface = None
        self._myfont = None

    def render(self, screen, mouse_pos, height, axis, p_color, fps):
        if axis == "progger": # blue shape
            self._rect = pygame.Rect(mouse_pos[0], height - consts.CODER_H, consts.CODER_W, consts.CODER_H)
        if axis == "catcher": # red shape
            self._rect = pygame.Rect(0, mouse_pos[1], consts.CODER_W, consts.CODER_H)
        self._myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self._textsurface = self._myfont.render(str(mouse_pos) + " fps: " + str(int(fps)), False, color.BLUEVIOLET)  # self._clock.get_fps()
        screen.blit(self._textsurface, (0, 0))
        # if width is zero rectangle can be filled
        pygame.draw.rect(screen, p_color, self._rect, 0)

    def is_collide(self, ex: pygame.Rect):
        pass
        #if (self._rect is not None) and (ex is not None):
            #return self._rect.colliderect(ex)

    def update(self, excepties_list):
        pass
        #for ex in excepties_list:
        #    ex._is_catched = self.is_collide(ex._rect)
        #    if ex._is_catched: print("catched")
