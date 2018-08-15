#Camera module will keep track of sprite offset.

#The gamemode is defined in this module.

import pygame, maps
from pygame.locals import *
from loader import load_image
from random import randint

PENALTY_COOL = 180
FLAG_SCORE = 15
CRASH_PENALTY = -2
HALF_TILE = 225
FULL_TILE = 450
COUNTDOWN_FULL = 3600
COUNTDOWN_EXTEND = 750

#This class is used as a single object, which moves around
#and keeps track of player score. It also manages the countdown timer.
class Closed(pygame.sprite.Sprite):
#The player has collided and should pick the flag.
    def claim_flag(self):
        self.score += FLAG_SCORE
        self.timeleft += COUNTDOWN_EXTEND
        if self.timeleft > COUNTDOWN_FULL:
            self.timeleft = COUNTDOWN_FULL
#The player has crashed into another vehicle, deduct some points.
    def car_crash(self):
        if (self.penalty_cool == 0):
            self.score += CRASH_PENALTY
            self.penalty_cool = PENALTY_COOL
#Find an adequate point to spawn flag.     
    def generate_checkpoint(self,X,Y):           
        self.x = X 
        self.y = Y
        self.rect.topleft = self.x, self.y
        print(self.x,self.y)
#Reset the state of the timer, score and respawn the flag.
    def reset(self):
        self.timeleft = COUNTDOWN_FULL
        self.score = 0
        self.generate_finish()
        
#Initialize.. yes.
    def __init__(self,X,Y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('Closed.png', False)
        self.rect = self.image.get_rect()
        self.x = 5
        self.y = 5
        self.penalty_cool = PENALTY_COOL
        self.generate_checkpoint(X,Y)
        self.rect.topleft = self.x, self.y
        self.score = 0
        self.timeleft = COUNTDOWN_FULL

#Update the timer and reposition the flag by offset.
    def update(self, cam_x, cam_y):
        self.rect.topleft = self.x - cam_x , self.y - cam_y
        if (self.penalty_cool > 0):
            self.penalty_cool -= 1
        if (self.timeleft > 0):
            self.timeleft -= 1
