import sys
import pygame
import random
from pygame.locals import *
from pygame.display import *
from classes import Box, Objective, Player

pygame.init()
clock = pygame.time.Clock()
info = pygame.display.Info()
(x, y) = (info.current_w, info.current_h)
screen = pygame.display.set_mode((x//2, y//2))
x, y = x//2, y//2


player = Player()
player.box.rect.center = (random.randint(0, x-20), random.randint(0, y-20))
objectives = []
for i in range(20):
   objectives.append(Objective())

count = 0
for i in objectives:
   i.box.rect.center = (random.randint(0, x-20), random.randint(0, y-20))


def quit():
   pygame.quit()


def update():
   pygame.event.pump()
   key = pygame.key.get_pressed()
   direction = ''
   if key[pygame.K_UP]:
      direction += 'N'
   elif key[pygame.K_DOWN]:
      direction += 'S'
   if key[pygame.K_RIGHT]:
      direction += 'E'
   elif key[pygame.K_LEFT]:
      direction += 'W'
   elif key[pygame.K_ESCAPE]:
      quit()
   
   if direction != '':
      player.move(direction)

   for i in objectives:
      i.handleCollision(player.box)
    

def render():
   screen.fill(color=pygame.Color("white"))
   screen.fill(player.box.color, player.box.rect)
   for i in objectives:
      screen.fill(i.box.color, i.box.rect)


def main():
   while True:
      clock.tick(60)
      update()
      render()
      pygame.display.flip()

if __name__ == "__main__":
   main()

