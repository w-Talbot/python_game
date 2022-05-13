import pygame

class Level:
    def __init__(self):

        # get the display surface from anywhere in the code
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

    def run(self):
        # update and draw the game
        pass
