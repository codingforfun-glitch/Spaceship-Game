

class Game_Settings:
    
    def __init__(self):
        
        self.height = (800)
        self.width = (900)
        self.screen_bg_color = (230, 230, 230)


        #introuducing bullets

        self.bullet_height = 15
        self.bullet_width = 200

        self.bullet_color = (60,60,60)   #dark grey color

        self.bullet_limit = 4


        self.direction = 1 #1 means alien is moving to right and we will update this value to change alien direction later in our main game.

        self.drop_speed = 10 #dropping of fleet 10 pixel 

        # self.ship_lives = 3 
        self.initial_dynamic_settings()


    def initial_dynamic_settings(self):

        """method to setup initial game system settings once called upon"""

        self.alien_speed = 3

        self.bullet_speed = 7 

        self.ship_lives = 3 

        self.ship_speed_value = 5

        self.speed_multiplier  = 1.1

    def increase_tempo(self):

        """ method to increase the tempo of the game as game progresses"""

        self.alien_speed *= self.speed_multiplier

        self.bullet_speed *= self.speed_multiplier

        self.ship_speed_value *= self.speed_multiplier

        print(self.ship_speed_value)


            

  

        
    



        