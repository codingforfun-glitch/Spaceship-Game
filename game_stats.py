
class Stats:

    def __init__(self):

        """ Stats class iniital values that is already set """

        self.score_multiplier = 1.1
        self.highscore = 0
        self.initial_stats()     

        

    def initial_stats(self):
        """ method to set initial values """
        self.score = 0

        self.single_alien_points = 50

        self.level = 1


    def update_stats(self):
        """ method to update initial values as game progresses"""

        # self.single_alien_points += 15 

        self.single_alien_points = int(self.single_alien_points * self.score_multiplier) 

        self.level += 1

        # print("current level: ", self.level)

        # print ("current:", self.score)

        # print("single alien points: ", self.single_alien_points)

    def _check_highscore(self):

        if self.score > self.highscore:

            self.highscore = self.score


            print("current score:\n", self.score)

            print("current highscore:", self.highscore)


            