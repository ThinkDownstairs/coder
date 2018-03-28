import os, sys
import pygame
import state_manager
import game
import menu
import about
import quit_
import consts
import bugreport
import splash
import highscore

if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', name)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print ('Cannot load sound:', wav)
    return sound

def init():
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.mixer.init()
    pygame.init()
    screen = pygame.display.set_mode((consts.SCREEN_W, consts.SCREEN_H))
    pygame.display.set_caption('CODER  a game for the #MetaGamaJam 17. - 31. March 2018')
    pygame.mouse.set_visible(0)
    return screen


if __name__ == '__main__':
    try:
        sm = state_manager.StateManager(init())
        sm.add_state(splash.Splash())
        sm.change_state(splash.Splash)
        sm.main_loop()
        pygame.quit()
    except:
        bugreport.bugreport()

