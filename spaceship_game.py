import sys
import pygame
import time

from ship import Ship
from settings import Game_Settings
from bullet import Bullet
from alien import Alien

from button import Button

from game_stats import Stats

from scoreboard import score_board

class spaceship_game:

    def __init__(self):

        pygame.init()

        self.game_settings = Game_Settings()

        self.screen = pygame.display.set_mode((self.game_settings.width,self.game_settings.height))   

        self.fullscreen_dispaly = False 
        # 
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)  

        self.game_name = pygame.display.set_caption("spaceship game")

        self.frame_rate = pygame.time.Clock()

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()

        self.alien_direction = self.game_settings.direction

        self.game_is_active = False #we created a new attribute taht is always true

        self.create_fleet()

        self.play_button = Button(self)

        self.game_stat = Stats()

        self.scoreboard = score_board(self)

    

    def run_game(self):


        while True:


            self._check_game_events()   # check if any key is being pressed or not

            # self.play_button.prep_button("Play")

            # self._check_life()

            self.screen.fill(self.game_settings.screen_bg_color)  # once the above are checkd then the updated screen is created with the background color provided 

            self.ship.display_ship() # this draws the ship in the canvas with ship's updated/original position

            self.aliens.draw(self.screen)

            self.scoreboard.draw()



            if self.game_is_active:  #if true then only run the following else program freezes

                self.ship._move_ship()  # if the key to move the ship is pressed then the method _move_ship() will operate

                self.bullets.update() #moves the bullet upward by the speed value

                self.drawing_bullet() #this draws the bullet in the canvas with the updated/original position


                self.remove_bullet() # now this method will check if the updated bullet position is at y value less than 0; if less, then the bullet
                # is removed

                self.aliens.update()

                
                self._collision_detection()


                self._check_alien_ship_collision()            

                self._check_bottom_edge()

                self._check_edge()

            else:
                
                self.play_button.prep_button("Play")



            # print("mouse_position:", self._check_mouse_events)


            pygame.display.flip() #this updates the screen each time anything happens
            self.frame_rate.tick(60) #this limit the frame of the game to 60 per second



    def _check_game_events(self):
         
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit() 

            else:    

                self._check_keydown_events(event)
                self._check_keyup_events(event)  

                self._check_mouse_events(event)  



    def _check_mouse_events(self, event):

        # mouse_pos = pygame.mouse.get_pos()

        # return mouse_pos



        if event.type == pygame.MOUSEBUTTONDOWN:
            # if event.key == pygame.BUTTON_LEFT:

                mouse_pos = pygame.mouse.get_pos()

                # print("mouse position:", mouse_pos)

                if self.play_button.button_img_rect.collidepoint(mouse_pos): #collidepoint() is a method on pygame's Rect class. 
                    #It checks whether a given point falls inside that rectangle's boundaries, and returns True or False.
                    self.game_is_active = True

                    pygame.mouse.set_visible(False)

                    # print("Button working")  #for testing purposes





    def _check_keydown_events(self,event):            
            
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.move_right = True

            elif event.key == pygame.K_LEFT:
                self.ship.move_left = True    

            elif event.key == pygame.K_UP:
                self.ship.move_up = True       


            elif event.key == pygame.K_DOWN:
                self.ship.move_down = True  

            elif event.key == pygame.K_F11:

                self.fullscreen_dispaly = not self.fullscreen_dispaly  

            #  toggle the screen, overwrite fullscreen_display each time the loop runs 

                if self.fullscreen_dispaly:
                    self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

                else:
                    self.screen = pygame.display.set_mode((self.game_settings.width,self.game_settings.height))   

                self.ship.screen_rect = self.screen.get_rect()   

            elif event.key == pygame.K_SPACE:
                self._fire_bullets()

            elif event.key == pygame.K_q:
                sys.exit()     

    def _check_keyup_events(self,event):                 

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.move_right = False     

            elif event.key == pygame.K_LEFT:
                self.ship.move_left = False

            elif event.key == pygame.K_UP:
                self.ship.move_up = False

            elif event.key == pygame.K_DOWN:
                self.ship.move_down = False      

            # elif event.key == pygame.K_F11:
            #     self.screen = pygame.display.set_mode((self.game_settings.width,self.game_settings.height))    

    def _fire_bullets(self):            

        if len(self.bullets) < self.game_settings.bullet_limit:                       
                new_bullet = Bullet(self)    
                self.bullets.add(new_bullet) #adding new bullets each time in the self.bullet sprite group to perfrom action
                # print(self.bullets)



    def _collision_detection(self):  #method to detect bullet_alien collision, once no aliens are left the fleet is recreated

        collision = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True) 
        """ NOTE: groupcollide function returns dictionary values with keys and values assigned to them """

        # print(collision)

        for alien in collision.values():

            """ here in this loop we loop through just values of the dictionary returned by groupcollide function and assign them to alien variable """
    
            # print(type(alien), alien) #testing

            self.game_stat.score = self.game_stat.score + len(alien) * self.game_stat.single_alien_points
            """ line to increase score based on the 'n' number of aliens that was touched by one single bullet"""
            #once this line executes then .score value in game_stats is updated with the recently assigned value

            # print("score count: ", self.game_stat.score)

            # self.scoreboard.prep_score()

            # self.game_stat._check_highscore()

            self.scoreboard.prep_score() #calling prep_score() method to prepare the scoreboard with the most recent updated alien score value

            
    
        if not self.aliens: #this if statement checks if there are aliens or not in the self.aliens group  
                    
                    self.bullets.empty() #this basically empties up the self.bullet group

                    self.game_settings.increase_tempo()  #method call to increase tempo of the game

                    self.create_fleet() #this recreates the alien fleet after none aliens are left in the screen

                    self.game_stat.update_stats() #method call to update stat with most recent value

                    self.scoreboard.prep_level()  #we are now callin

                    

                    # print(len(self.aliens)) #testing purposes

              
                
    def remove_bullet(self):
        for bullet in self.bullets.copy(): #copy of list of sprite
            if bullet.rect.bottom < 0:
                bullet.kill()     

        

    def drawing_bullet(self):

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def create_fleet(self):
        alien = Alien(self)
        self.alien_x = alien.rect.width  #takes width of alien image and stores in self.alien_x attribute 
        self.alien_y = alien.rect.height #takes height of alien image and stores in self.alien_y attribute
        # self.aliens.add(alien)
        # # self.aliens.draw(self.screen)
        self.current_xposition = self.alien_x #her self.current_xposition value is equal to self.alien_x 

        # self.current_xposition = alien.current_x_posn

        # print(self.current_xposition)

        self.current_yposition = self.alien_y #here self.current_yposition value is equal to self.alien_y 

        self._create_aliens(self.current_xposition,self.current_yposition, self.alien_x,self.alien_y) #passing self.currnet_xposition and self.current_yposition
        #to the parameter; x_position and y_position and resepctive




        # self.aliens.update()
        
    def _create_aliens(self,x_position,y_position, row_aliens, next_row):   #this method creates aliens with multiple rows and columns

        while y_position < (self.game_settings.height -  7 * next_row): #while loop to create columns of aliens

            while x_position < (self.game_settings.width - row_aliens):    #nested while loop to first create rows
                new_alien = Alien(self) #temporary instance of alien called as new_alien which will be have the properties from alien class
                new_alien.rect.x = x_position #setting the x rect value of temp alien instance equal to passed value in x_posiiton
                new_alien.rect.y = y_position #similarly to new_alien.rect.x

                new_alien.x_posn = float(x_position) #here we are updating the x_posn for each new_alien created with the updated value in x_position from their
                #default init value set in alien.py in self.x_posn = float(self.rect.x) which will then enable displaying multiplue rows of aliens in the display

                self.aliens.add(new_alien) #builtin pygame function add to add the created alien to the group self.aliens
                # self.aliens.draw(self.screen)
                x_position += 2 * row_aliens #updates the x_position once the alien is created to move next step in the loop to create another alien in the same row


            x_position = self.alien_x  #this executes once the row is filled with aliens and when the program moves to next column to add aliens. this basically
            #brings the x_position back to the default starting position due to which the fist alien in 2nd column will be in same location as the very first alien 
            #in the first row

            y_position += 2 * next_row    # this updates the y_postion meaning, it moves the code execution to next column once the aliens in the rows are filled completely
        


    def _check_edge(self): #method to check for alien edges

        """ method to check left or right edges of the screen """

        for alien in self.aliens.sprites(): #looks for each aliens in self.aliens group and here single alien is the temp variable name 'alien' in for loop
            # print(alien.rect.right,"\n")
            # print(self.game_settings.width)

            if alien.rect.right >= self.game_settings.width or alien.rect.left <= 0: #this checks wether the alien's left and right edges has touched the wall or not

                self._update_aliens() #once edge is detected the _update_aliens() method runs 

                break

        # print(self.current_yposition)


    def _update_aliens(self): #here in update aliens, we update aliens based on the drop speed and the direction once edge detection is set to true
     
     for alien in self.aliens.sprites(): #same as before, loops through each aliens in self.aliens group
        alien.rect.y += self.game_settings.drop_speed #changes the y rect of alien object with respect to the drop speed 

     self.alien_direction *= -1 #then changes the direction of alien to either negative if positive and vice versa

    def _check_bottom_edge(self):

        """ method to check whether alien has touched the bottom edge of the screen or not """

        # print(self.alien_y)

        for alien in self.aliens.sprites():  #this for loop loops through every aliens in self.aliens sprite group

            if alien.rect.bottom >= self.game_settings.height: #and the if statement checks if even any one of the looped aliens have touched the bottom of the 
                #screen or not
                self._recreate_aliens_bullets()

                self.game_settings.ship_lives -= 1

                self._check_life()

                self.scoreboard.prep_life()

                break





    def _check_alien_ship_collision(self):

        """ method to check for alien and ship collision """

        # for alien in self.aliens.sprites():

        # detect_collision = pygame.sprite.spritecollide(self.ship, self.aliens, False)

        detect_collision = pygame.sprite.spritecollideany(self.ship, self.aliens) #pygame builtin function to check for the collisoin of any objects 
        #it takes sprite and group as args

        if detect_collision: #if detect_collison is true then only run the following

            self._recreate_aliens_bullets() #calls _recreate_aliens_bullets() 

            self.game_settings.ship_lives -= 1 #reduces the no of ship the player has

            self._check_life() #calls _check_life()

            # print("ship collision trigger") #testing

            self.scoreboard.prep_life()


    def _recreate_aliens_bullets(self): #method which empties up the screen entirely and creates new fleet of aliens upon called
                
                time.sleep(0.5) #if the if statement is true then the whole program freezes for .5 secondes

                self.aliens.empty() #the aliens in self.aliens gets emptied 

                self.bullets.empty() #also the bullets are emptied

                self.ship.update() #calls update from ship 

                self.create_fleet() #then we recreate the fleet different aliens

    def _check_life(self):  #method that checks life remaining upon called

        # print (self.game_settings.ship_lives) #testing

        if self.game_settings.ship_lives <= 0: #if logic that checks the no of remaining ship the player has

            # print(self.game_settings.ship_lives) #testing

            self.game_is_active = False #only runs when the player is out of ship or remaining ship   

            self.game_stat._check_highscore()    

            self.scoreboard.prep_highscore()    

            self.game_settings.initial_dynamic_settings()

            self.game_stat.initial_stats()

            pygame.mouse.set_visible(True)

            self.scoreboard.prep_score()



if __name__ == '__main__':
    sg = spaceship_game()
    sg.run_game()

