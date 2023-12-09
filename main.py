import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        pygame.display.set_caption("Mike's Realm")
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        print("Check 2")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()
             
if __name__ == "__main__":
    print("Check 0")
    game = Game()
    print("Check 1")
    game.run()
