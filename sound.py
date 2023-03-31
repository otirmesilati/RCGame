import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()

