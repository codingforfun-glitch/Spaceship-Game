import sys

import pygame

from pygame.sprite import Sprite

class Bullet(Sprite): #here bullet is child class and sprite is parent class from which we are inheriting

    def __init__(self, sp_game):

        super().__init__()  #this checks the functions of sprite is functioning properly which avoids error during the actual runtime

        self.display = sp_game.screen #this imports the screen from our main spaceship game because we need the surface to draw the bullets on

        self.display_rect = self.display.get_rect()

        self.settings = sp_game.game_settings
        self.ship = sp_game.ship

        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height) 
        #initializing the position of the bullet to the top of the screen

        self.rect.midtop = self.ship.rect.midtop # not sure if this works and i am conrfused in this part
        # this comment explains my understanding: we have to set the bullet to fire from the top of the ship and we can only use midtop
        # after getting the rect of the objects. as for ship, i tired to pull the ship rect by going through main game, then ship attribute
        # then to the ship_rect, but i am not sure this approach works or not

        self.bullet_y_position = float(self.rect.y)


    def update(self):

        self.bullet_y_position -=  self.settings.bullet_speed #this decreases the bullet position with respect to bullet speed.

        self.rect.y = self.bullet_y_position  #this should technically update the bullet y rect position as its value decreases

    def draw_bullet(self):
        pygame.draw.rect(self.display, self.settings.bullet_color, self.rect)    








        






