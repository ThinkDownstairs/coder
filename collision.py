

import pygame

def collide(s1: pygame.Surface, x1: int, y1: int, s2: pygame.Surface, x2: int, y2: int) -> bool:
    w1, h1 = s1.get_size()
    #r1, b1 = x1 + w1, y1 + h1
    w2, h2 = s2.get_size()
    #r2, b2 = x2 + w2, y2 + h2
    r1 = pygame.Rect(x1, y1, w1, h1)
    r2 = pygame.Rect(x2, y2, w2, h2)
    if r1.colliderect(r2):
        # TODO : check for pixel collision
        return True
    return False
