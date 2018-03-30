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
import locations


def init():
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.mixer.init()
    pygame.init()
    pygame.display.set_icon(pygame.image.load(locations.image('coder-icon.png')))
    screen = pygame.display.set_mode((consts.SCREEN_W, consts.SCREEN_H))#, pygame.DOUBLEBUF)
    pygame.display.set_caption('CODER  a game for the #MetaGameJam 17. - 31. March 2018', 'c0d3r')
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

