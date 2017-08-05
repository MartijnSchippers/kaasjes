import pygame as pg
from Settings import *
import random

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vx = 50
        self.vy = HEIGHT-100
        self.rect.y = self.vy
        self.lives = 3
        
    def update(self):
        self.vx = 0
        
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx = -5
        if keys[pg.K_RIGHT]:
            self.vx = 5
            
        self.rect.x += self.vx
        if self.rect.x < -10:
            self.rect.x = WIDTH - 10
        if self.rect.x > WIDTH - 10:
            self.rect.x = -10
        
class Kaasjes(pg.sprite.Sprite):
    def __init__(self, x, y, lekker):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((15, 15))
        if lekker:
            self.image.fill(YELLOW)
        if not lekker:
            self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
        
    def update(self):
        
        pass
        
        
    
