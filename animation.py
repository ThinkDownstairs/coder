
import pygame




class Animation(object):
    __slots__ = ('_count', '_sprites', '_idx', '_width', '_height', '_duration', '_tick', '_once', '_done')
    def __init__(self, sprite: pygame.Surface, count: int = 1, fps: int = 8, once: bool = False) -> None:
        super().__init__()
        self._count = count
        self._once = once
        self._done = False
        self._idx = 0
        self._width = sprite.get_width() // count
        self._height = sprite.get_height()
        self._duration = 1000 // fps
        self._sprites = [sprite.subsurface((self._width * i, 0, self._width, self._height)) for i in range(count)]
        self._tick = 0

    def update(self, delta: int) -> None:
        if self._done:
            return
        self._tick -= delta
        while self._tick <= 0:
            self._idx += 1
            self._tick += self._duration
        if self._idx >= self._count:
            self._idx %= self._count
            self._done = self._once
            if self._done:
                self._idx = self._count - 1 # ensure that we stop on the last animation frame

    def render(self, target: pygame.Surface, x: int, y: int) -> None:
        target.blit(self._sprites[self._idx], (x, y))

    width = property(lambda s: s._width)
    height = property(lambda s: s._height)
    surface = property(lambda s: s._sprites[s._idx])
    done = property(lambda s: s._done)







if __name__ == '__main__':
    import sys
    try:
        fn = sys.argv[1]
        cnt = int(sys.argv[2])
    except:
        fn = 'res/export/try-except.png'
        cnt = 6
    def load_image(filename: str) -> pygame.Surface:
        return pygame.image.load(filename).convert_alpha()
    pygame.init()
    screen = pygame.display.set_mode((480, 320))
    clock = pygame.time.Clock()
    running = True
    delta = 0
    a = Animation(load_image(fn), cnt, 5)
    while running:
        # INPUT
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                continue
        # UPDATE
        a.update(delta)
        # RENDER
        screen.fill((0,0,0))
        a.render(screen, 5, 5)
        #pygame.display.flip()
        pygame.display.update()
        # TICK
        delta = clock.tick(30)
