import pygame as pg
from Settings import *
from Sprites import *
import random
#C:\Users\Rita\Documents\martijn\Games\kaasjes\main.py

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        
        
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.kaasjes = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        for i in ALL_KAASJES:
            self.kaasjes.add(Kaasjes(i[0], i[1], i[2]))
        self.run()
    
    def run(self):
        self.playing = True
        while self.playing == True:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            
    
    def update(self):
        #update all sprites
        self.all_sprites.update()
        
        #collision
        hits = pg.sprite.spritecollide(self.player, self.kaasjes, False)
        if hits:
            hits[0].kill()

        for i in self.kaasjes:
            i.rect.top += 2
            if i.rect.top > HEIGHT:
                i.kill()
                ALL_KAASJES.append((random.randint(0, WIDTH-20), 0))
                
        while len(self.kaasjes) < 4:
            lekker = True
            number = random.randint(0, 4)
            if number == 4:
                lekker = False
            k = Kaasjes(random.randrange(0, WIDTH-20), random.randrange(-15, 0), lekker)
            self.kaasjes.add(k)
            
            
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
       
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.kaasjes.draw(self.screen)
        pg.display.flip()
    def show_start_screen(self):
        pass
        
    def show_go_screen(self):
        pass
    
g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()
    
pg.quit()
    
