#! /usr/bin/env python

import os
import sys

import pygame

class Control(object):
    def __init__(self):
        pygame.init()
        os.environ["SDL_VIDEO_CENTERED"] = "TRUE"
        pygame.display.set_caption("Clash Royale Clone")
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.done = False

    def main_loop(self):
        while not self.done:
            self.done = True

def main():
    Control().main_loop()
    pygame.quit()
    sys.exit()

main()
