# Tristan Hilbert

import pygame
from pygame import Color

class Box:

    def __init__(self):
        self.rect = pygame.Rect(10,20,20,20)
        self.color = Color(0,0,0)

    def colorChange(self):
        self.color = Color(255,0,0)


class Player:
    
    def __init__(self):
        self.box = Box()
    
    def move(self, dir):
        if dir is True:
            self.box.rect.move_ip(2,0)
        else:
            self.box.rect.move_ip(-2,0)
    
class Objective:

    def __init__(self):
        self.box = Box()
    
    def handleCollision(self, rect):
        if self.box.rect.colliderect(rect):
            self.box.colorChange()