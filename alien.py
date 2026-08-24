
import os

import pygame

from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, sp_game):
        super().__init__()

        self.screen = sp_game.screen
        self.path= os.path.join(os.path.dirname(__file__), 'alien.bmp')
        self.image = pygame.image.load(self.path)
        self.rect = self.image.get_rect()

        self.settings = sp_game.game_settings

        self.live_horizontal_direction = sp_game

        self.live_vertical_direction = sp_game

        self.x_posn = float(self.rect.x)

        self.y_posn = self.rect.y



    def alien_movement(self):
 
        # self.settings.alien_direction *= -1
        
        self.x_posn += self.settings.alien_speed * self.live_horizontal_direction.alien_direction #logic to change the x position of aliens including speed and direction
        #where if alien_direction is 1 then alien moves right and vice versa

        # self.y_posn = self.live_vertical_direction.current_yposition
    

        # print(self.x_posn)


    def update(self):


        self.alien_movement()
        self.rect.x = self.x_posn #this updates the rect x value with the most recent x position obtained from above line



      # self.x_posn += self.settings.game_settings.alien_speed #condition that increament the current rect with the alien speed value set in settings file



