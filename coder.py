import os, sys
import pygame
import state_manager
import game
import menu
import about
import quit_
import consts

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

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                #print event.button
                print(pygame.mouse.get_pos())

def init():
    pygame.init()
    screen = pygame.display.set_mode((consts.SCREEN_W, consts.SCREEN_H))
    pygame.display.set_caption('Coder')
    pygame.mouse.set_visible(0)
    return screen


if __name__ == '__main__':
    sm = state_manager.StateManager(init())
    m = menu.Menu()
    m.add(menu.MenuEntry('Start', game.Game))
    m.add(menu.MenuEntry('About', about.About))
    m.add(menu.MenuEntry('Quit', quit_.Quit))
    sm.add_state(m)
    sm.add_state(game.Game())
    sm.add_state(about.About())
    sm.add_state(quit_.Quit())
    sm.change_state(menu.Menu)
    sm.main_loop()

