import sys, pygame
from pygame.locals import *
from classes import Box, Objective, Player

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480))
player = Player()
player.box.rect.center = (20, 240)
objectives = []
objectives.append(Objective())
objectives.append(Objective())
objectives.append(Objective())

count = 0
for i in objectives:
    i.box.rect.center = (count + 100, 240)
    count += 100

def update():
    pygame.event.pump()   
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(False)
    elif key[pygame.K_RIGHT]: 
        player.move(True)
    
    for i in objectives:
        i.handleCollision(player.box.rect)
    

def render():
    screen.fill(color=pygame.Color("blue"))
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

