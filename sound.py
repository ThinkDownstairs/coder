
import os

import enum
from enum import auto

import pygame

class Sounds(enum.Enum):
    MUSIC = auto()
    CATCH = auto()
    KILL = auto()
    BUG = auto()
    FIRE = auto()

    def get_filename(self):
        fn = None
        if self == Sounds.MUSIC: fn = 'CH-AY-NA.ogg'
        elif self == Sounds.CATCH: fn = 'dead.wav'
        elif self == Sounds.KILL: fn = 'teleport.wav'#'insectoralien.flac'
        elif self == Sounds.BUG: fn = 'teleport.wav'
        elif self == Sounds.FIRE: fn = 'teleport.wav'
        else: raise Exception('Unknown Sound: {}'.format(str(self)))
        return os.path.join('res', 'sounds', fn)

_sounds = None
class Sound(object):
    def __init__(self):
        super().__init__()
        global _sounds
        if _sounds is None:
            _sounds = {e: pygame.mixer.Sound(e.get_filename()) for e in Sounds}
            m = _sounds.get(Sounds.MUSIC)
            if m is not None:
                m.set_volume(.35)
        self._sounds = _sounds

    def play(self, sound_: Sounds, loop: bool = False):
        s = self._sounds.get(sound_)
        if s is not None:
            s.play(-1 if loop else 0)

    def stop(self, sound_: Sounds):
        s = self._sounds.get(sound_)
        if s is not None:
            s.stop()





if __name__ == '__main__':
    import time
    import random
    pygame.init()
    #snd = pygame.mixer.Sound('res/sounds/CH-AY-NA.ogg')
    #eff = pygame.mixer.Sound('res/sounds/dead.wav')
    #snd.play(-1)
    #while True:
        #time.sleep(.1)
        #if random.random() < 0.05:
            #eff.play()
    s = Sound()
    s.play(Sounds.MUSIC, True)
    cnt = 0
    while cnt < 1000:
        cnt += 1
        time.sleep(.1)
        if random.random() < .05:
            s.play(random.choice([Sounds.BUG, Sounds.CATCH, Sounds.FIRE, Sounds.KILL]))

    for _s in Sounds:
        s.stop(_s)



