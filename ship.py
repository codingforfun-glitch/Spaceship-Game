import os
import pygame

from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,main_game):

        super().__init__()


        self.sg_game_screen = main_game.screen
        self.screen_rect = self.sg_game_screen.get_rect()

        ship_path = os.path.join(os.path.dirname(__file__), 'ship.bmp')
        self.image  = pygame.image.load(ship_path)
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        # print(self.rect)

        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

        self.settings = main_game.game_settings

        self.store_position_x = float(self.rect.x)
        self.store_position_y = float(self.rect.y)

        # self.ship_speed = self.settings.ship_speed_value
        

    def _move_ship(self):
       
        if self.move_right and self.rect.right < self.screen_rect.right:
         self.store_position_x += self.settings.ship_speed_value

        if self.move_left and self.rect.left > self.screen_rect.left:
         self.store_position_x -= self.settings.ship_speed_value

        if self.move_up and self.rect.top > self.screen_rect.top:
         self.store_position_y  -= self.settings.ship_speed_value

        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
          self.store_position_y  += self.settings.ship_speed_value

        self.rect.x = self.store_position_x
        self.rect.y = self.store_position_y


    def update(self):

        self.rect.midbottom = self.screen_rect.midbottom

        self.store_position_x = self.rect.x

        self.store_position_y = self.rect.y

        

        print(self.rect)



    def display_ship(self):
     self.sg_game_screen.blit(self.image,self.rect)        
              
             
        

     
        




        
            