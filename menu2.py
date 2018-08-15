import os, sys, pygame, random, array, gamemode
import direction,  bounds, timeout, menu
from pygame.locals import *

#Import game modules.
from loader import load_image
import player, maps, traffic, camera, tracks

CENTER_W = -1
CENTER_H = -1

#Menu function
def menu():
    clock = pygame.time.Clock()
    running = True
    cam = camera.Camera()
#create sprite groups.
    map_s     = pygame.sprite.Group()
#generate tiles
    for tile_num in range (0, len(maps.map_tile)):
        maps.map_files.append(load_image(maps.map_tile[tile_num], False))
    for x in range (0, 5):
        for y in range (0, 6):
            map_s.add(maps.Map(maps.map_2[x][y], x * 450, y * 450))
    while running:
        map_s.update(cam.x, cam.y)
        map_s.draw(screen)
        clock.tick(64)
#initialization
pygame.init()

screen = pygame.display.set_mode((pygame.display.Info().current_w,
                                  pygame.display.Info().current_h)
                                  )


pygame.display.set_caption('Table Theory.')
pygame.mouse.set_visible(False)
font = pygame.font.Font(None, 24)

CENTER_W =  int(pygame.display.Info().current_w /2)
CENTER_H =  int(pygame.display.Info().current_h /2)

#new background surface
background = pygame.Surface(screen.get_size())
background = background.convert_alpha()
background.fill((26, 26, 26))

#Enter the mainloop.
menu()

pygame.quit()
sys.exit(0)
