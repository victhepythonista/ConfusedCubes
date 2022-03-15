import sys,random
import pygame
from screen import Screen
from cube import Cube

cubes_no = 100
CUBES = []

screen_bgs = [
 pygame.Color('white'),
 pygame.Color('cyan')]
screen_color = pygame.Color('white')
for i in range(cubes_no):CUBES.append(Cube())
class CONFUSEDCUBES(Screen):
    def __init__(self):
        Screen.__init__(self, (480,480))
        self.background = screen_color
    def get_keys(self):
        keys =pygame.key.get_pressed()
        if keys[pygame.K_n]:
            self.background = random.choice(screen_bgs)
            print(':::')
    def display_widgets(self):
        self.get_keys()
         
            
        self.window.fill(self.background)
        for cube in CUBES:
            cube.show(self.window)
CONFUSEDCUBES().show()
