import pygame.font

class Button:

    def __init__(self, sp_game):

        self.display = sp_game.screen

        self.bg_color  = (0, 135, 0)

        self.display_rect = self.display.get_rect()

        self.settings = sp_game.game_settings

        self.font = pygame.font.SysFont(None, 48)    #none = pygame default font and 48 = size of the font

        self.font_color = (255, 255, 255)  #color of the font 


    def prep_button(self, message):

        # print(message)

        self.button_img = self.font.render(message, True, self.font_color, self.bg_color)

        self.button_img_rect = self.button_img.get_rect()

        # print(self.button_img_rect)

        self.button_img_rect.center = self.display_rect.center

        self.display.blit(self.button_img, self.button_img_rect)  

        # print("prep_button method ran")

    