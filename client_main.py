from socket import *
import sys
import pygame
from pygame.locals import *
from pygame.display import *
from classes import Box, Objective, Player

def get_info():
   ret = ""
   while len(ret) == 0 or ret[-1] != '}':
      pkt = s.recv(1024).decode("ascii")
      ret += pkt
   return ret[:-1]



def quit():
   s.close()
   pygame.quit()


def update():
   pygame.event.pump()
   key = pygame.key.get_pressed()
   direction = '{'
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
   direction += '}'
   s.send(direction.encode("ascii"))
   print(direction)
   
    

def render():
      
      receival = get_info()
      if len(receival) > 0:
         screen.fill(color=pygame.Color("white"))
         players = receival[:receival.index('=')].split('|')[:-1]
         objectives = receival[receival.index('=')+1:].split('|')[:-1]
         tokens = []
         rect = pygame.Rect(0,0,20,20)
         for i in players:
            tokens = i.split(",")
            rect.center = (int(tokens[0]), int(tokens[1]))
            screen.fill(pygame.Color(int(tokens[2]),int(tokens[3]),int(tokens[4])), rect)
         for i in objectives:
            tokens = i.split(",")
            rect.center = (int(tokens[0]), int(tokens[1]))
            screen.fill(pygame.Color(int(tokens[2]),int(tokens[3]),int(tokens[4])), rect)
   


def main():
   while True:
      clock.tick(60)
      render()
      update()
      pygame.display.flip()

## Socket globals
s = socket(AF_INET, SOCK_STREAM)
s.settimeout(10)
s.connect((input("IP Address?\n"), int(input("PORT?\n"))))
s.settimeout(None)
#######

## Pygame Globals 
pygame.init()
clock = pygame.time.Clock()
#info = pygame.display.Info()
#(x, y) = (info.current_w, info.current_h)
x, y = 1024, 768
#screen = pygame.display.set_mode((x//2, y//2))
screen = pygame.display.set_mode((x, y))
#x, y = x//2, y//2
###########

if __name__ == "__main__":
   main()