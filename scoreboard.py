
from button import Button
from ship import Ship
from pygame.sprite import Group


class score_board(Button):

    def __init__(self, main_game):

        super().__init__(main_game)  #inheriting from button class

        self.bg_color = main_game.game_settings.screen_bg_color

        self.main_game = main_game

        self.font_color = (0,0,0)



        self.prep_score()  #calling method to make sure the game runs smoothly during execution by displaying its content before it is called from main progam
        self.prep_level()
        self.prep_highscore()


        self.ship = Ship(main_game)

        self.prep_life()


    def prep_score(self):

        rounded_score = round(self.main_game.game_stat.score, -1)

        self.stat_str = f"{rounded_score:,}"

        # print("Rounded score =", self.stat_str_test)

        # self.stat_str = str(self.main_game.game_stat.score)

        self.stat_img = self.font.render(self.stat_str, True, self.font_color, self.bg_color)

        self.stat_img_rect = self.stat_img.get_rect()

        self.stat_img_rect.right = self.display_rect.right - 20

        self.stat_img_rect.top = 10


    def prep_level(self):
        """ method to prepare level """
        level_str = str(self.main_game.game_stat.level)

        self.level_img = self.font.render(level_str, True, self.font_color, self.bg_color)

        self.level_img_rect = self.level_img.get_rect()

        self.level_img_rect.right = self.display_rect.right - 20

        self.level_img_rect.top = self.stat_img_rect.bottom + 10


    def prep_highscore(self):
        """ method to prepare high score """

        rounded_highscore = round(self.main_game.game_stat.highscore, -1)

        highscore_str = f"{rounded_highscore:,}"

        # highscore_str = str(self.main_game.game_stat.highscore)

        self.highscore_img = self.font.render(highscore_str, True, self.font_color, self.bg_color)

        self.highscore_img_rect = self.highscore_img.get_rect()

        self.highscore_img_rect.centerx = self.display_rect.centerx

        self.highscore_img_rect.top = 10


    def prep_life(self):

        self.ship_life = Group()

        for ship_number in range(self.main_game.game_settings.ship_lives):

            new_ship_icon = Ship(self.main_game)

            # new_ship_icon_rect = new_ship_icon.get_rect()
            new_ship_icon.rect.left = ship_number * (new_ship_icon.rect.width + 10)

            new_ship_icon.rect.top = 10

            self.ship_life.add(new_ship_icon)
        

    def draw(self):
        """ method to display everything on the screen """

        self.display.blit(self.stat_img, self.stat_img_rect)

        self.display.blit(self.level_img, self.level_img_rect)

        self.display.blit(self.highscore_img, self.highscore_img_rect)

        self.ship_life.draw(self.display)



