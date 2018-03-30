

import pygame

def collide(s1: pygame.Surface, x1: float, y1: float, s2: pygame.Surface, x2: float, y2: float) -> bool:
    l1, t1 = int(x1), int(y1)
    l2, t2 = int(x2), int(y2)
    w, h = s1.get_size()
    r1, b1 = l1 + w, t1 + h
    w, h = s2.get_size()
    r2, b2 = l2 + w, t2 + h
    if (((l2 < l1 < r2) or (l2 < r1 < r2)) and ((t2 < t1 < b2) or (t2 < b1 < b2)) or \
        ((l1 < l2 < r1) or (l1 < r2 < r1)) and ((t1 < t2 < b1) or (t1 < b2 < b1))):
       for x in range(max(l1, l2), min(r1, r2)):
           for y in range(max(t1, t2), min(b1, b2)):
               if (s1.get_at((x - l1, y - t1)).a > 1) and (s2.get_at((x - l2, y - t2)).a > 1):
                   return True
    return False

