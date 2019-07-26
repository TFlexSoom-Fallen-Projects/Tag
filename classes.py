# Tristan Hilbert

import pygame
from pygame import Color

class Box:

    def __init__(self):
        self.rect = pygame.Rect(10,20,20,20)
        self.color = Color(0,0,0)

    def colorChange(self, color):
        self.color = color


class Player:
    
    def __init__(self):
        self.box = Box()
        self.box.color = Color(102,0,255)
    
    def assign_color(self, color):
        self.box.colorChange(color)
    
    def move(self, direction):
        if direction == 'N':
            self.box.rect.move_ip(0,-4)
        elif direction == 'NE':
            self.box.rect.move_ip(2,-2)
        elif direction == 'E':
            self.box.rect.move_ip(4,0)
        elif direction == 'SE':
            self.box.rect.move_ip(2,2)
        elif direction == 'S':
            self.box.rect.move_ip(0,4)
        elif direction == 'SW':
            self.box.rect.move_ip(-2,2)
        elif direction == 'W':
            self.box.rect.move_ip(-4,0)
        elif direction == 'NW':
            self.box.rect.move_ip(-2,-2)
            
    
class Objective:

    def __init__(self):
        self.box = Box()
    
    def handleCollision(self, box):
        if self.box.rect.colliderect(box.rect):
            self.box.colorChange(box.color)