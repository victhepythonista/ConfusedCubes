import pygame
import random

up = 0,-1
down = 0,1
left = -1,0
right = 1,0
directions  = [up, down, left, right]

COLORS = [
(30,40,43),
(28,28,54),
(100,98,80),
(23,50,79),
(200,200,230),
(20,100,30),
(40,40,0),
(200,200,12)]
COLORS = [(50,50,50)]
class Cube:
    def __init__(self):
        self.position = random.randrange(0,480,16),random.randrange(0,480,16)
        self.direction = random.choice(directions)
        self.block_positions = [self.position]
        self.color = random.choice(COLORS)
        speed = 32
        self.length = 1

    def reset(self):
        self.block_positions = []
        new_pos = random.randrange(0,480,16),random.randrange(0,480,16)
        self.block_positions.insert(0, new_pos)
        self.color = random.choice(COLORS)
    def move(self, direction):
        for pos in self.block_positions:
            p_x = abs(pos[0]) + (direction[0] * 16)
            p_y =abs(pos[1]) + (direction[1] * 16)
            new_pos = p_x,p_y
            self.block_positions[self.block_positions.index(pos)] = new_pos
    def draw(self, window):
        for pos in self.block_positions:
            rect = pygame.Rect(pos[0], pos[1], 16,16)
            pygame.draw.rect(window, self.color, rect, 0)
    def watch_environment(self):
        pos = self.block_positions[0]
        if pos[0] < 0 or pos [0] >480 or pos[1] > 480 or pos[1] < 0 :
            self.reset()


    def show(self,window):
        self.watch_environment()
        self.draw(window)
        self.move( random.choice(directions))
