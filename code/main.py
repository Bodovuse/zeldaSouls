import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):

        #general set up of pygame, screen and clock
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        #captioning the window
        pygame.display.set_caption('ZELDALIKE')
        self.clock = pygame.time.Clock()

        #create instance of level class
        self.level = Level()

    def run(self):
        #event loop to close game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #fill screen
            self.screen.fill('black')
            #run game
            self.level.run()
            #update screen
            pygame.display.update()
            #controling FPS
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()