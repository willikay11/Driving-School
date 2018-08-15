#Camera module will keep track of sprite offset.

#Map file.

import os, sys, pygame, math
from pygame.locals import *
from loader import load_image
from random import randrange

#Map filenames.

map_files = []
map_tile = ['servicelane_without_parking.png',#0
            'null.png',#1
            'Four_lane_left_out.png',#2
            'Four_lane_right_in.png',#3
            'Four_lane_left_in.png',#4
            'Four_lane_right_out.png',#5
            'Three_lane_left_out.png',#6
            'Three_lane_right_in.png',#7
            'Three_lane_left_in.png',#8
            'Three_lane_right_out.png',#9
            'first_quadrant.png',#10
            'second_quadrant.png',#11
            'third_quadrant.png',#12
            'fourth_quadrant.png',#13
            'servicelane_with_parking.png',#14
            'flush_parking.png',#15
            'servicelane_90_2.png',#16
            'right_four_laneCompletelyDashed.png',#17
            'left_four_laneCompletelyDashed.png',#18
            'servicelane_300.png',#19
            'three_lane_left_completely_dashed_out.png',#20
            'three_lane_left_completely_dashed_in.png',#21
            'right_four_laneCompletelyDashed - 1.png',#22
            'left_four_laneCompletelyDashed - 1.png'#23
            ]

#Map to tile.
crossing = 0
straight = 1
turn     = 2
split    = 3
deadend  = 4
null     = 5

#tilemap.
map_1 = [
          [2,1,3,1,1,3,1,1,1,4],
          [1,5,1,5,4,0,1,2,5,4],
          [1,4,3,1,3,3,1,3,2,1],
          [3,1,3,1,3,5,4,5,1,1],
          [3,2,1,5,1,5,3,1,0,3],
          [1,2,0,1,0,3,0,4,1,1],
          [1,5,1,4,2,1,1,2,3,1],
          [1,2,0,1,3,3,0,0,2,1],
          [1,1,4,2,2,5,1,2,1,3],
          [2,3,1,3,1,1,3,1,1,2]
        ]

map_2 = [
    [0,1,1,18,17,1],
    [0,1,1,2,3,1],
    [19,21,8,10,11,7],
    [19,20,6,13,12,9],
    [14,1,15,4,5,1],
    [0,16,16,23,22,16]
    ]

#tilemap rotation, x90ccw
map_1_rot = [
          [1,1,0,1,1,0,1,1,1,3],
          [0,0,0,0,1,0,1,0,0,0],
          [0,1,2,1,0,2,1,2,0,0],
          [1,1,0,1,3,0,0,0,0,0],
          [1,0,0,0,0,0,1,1,0,3],
          [0,2,0,1,0,0,0,3,0,0],
          [0,0,0,1,3,0,0,1,3,0],
          [0,1,0,1,0,2,0,0,3,0],
          [0,0,2,1,3,0,0,2,1,3],
          [2,2,1,2,1,1,2,1,1,3]
            ]


class Map(pygame.sprite.Sprite):
    def __init__(self, tile_map, y, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = map_files[tile_map]
        self.rect = self.image.get_rect()

##        if rot != 0:
##            self.image = pygame.transform.rotate(self.image, rot * 90)

        self.x = x
        self.y = y

#Realign the map
    def update(self, cam_x, cam_y):
        self.rect.topleft = self.x - cam_x, self.y - cam_y
        
     
