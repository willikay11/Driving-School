#The MIT License (MIT)

#Copyright (c) 2012 Robin Duda, (chilimannen)

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

#Camera module will keep track of sprite offset.

#Player module, the car.
import os, sys, pygame, math, maps
from pygame.locals import *
from random import randint
from loader import load_image

GRASS_SPEED = 0.715
GRASS_GREEN = 75
CENTER_X = -1
CENTER_Y = -1

#Rotate car.
def rot_center(image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

def findspawn(X,Y):
        return X, Y

#define car as Player.
class Finish(pygame.sprite.Sprite):
    def __init__(self,X,Y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('finish.png')
        self.rect = self.image.get_rect()
        self.image_orig = self.image
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        CENTER_X =  int(pygame.display.Info().current_w /2)
        CENTER_Y =  int(pygame.display.Info().current_h /2)
        self.x = CENTER_X
        self.y = CENTER_Y
        self.rect.topleft = self.x, self.y
        self.x, self.y = findspawn(X,Y)
        self.dir = 0
        self.speed = 0.0
        self.maxspeed = 7.5
        self.minspeed = -1.85
        self.acceleration = 0.095
        self.deacceleration = 0.12
        self.softening = 0.04
        self.steering = 1.60
        self.tracks = False

#fix this function 
    def update(self, last_x, last_y):
        self.x = self.x + self.speed * math.cos(math.radians(270-self.dir))
        self.y = self.y + self.speed * math.sin(math.radians(270-self.dir))
        #self.reset_tracks()
