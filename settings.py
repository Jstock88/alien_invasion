class Settings():

    def __init__(self):

        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        #Ship settings
        self.ship_speed_factor = 1.0

        #Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 160, 160, 160
        self.bullets_allowed = 3
