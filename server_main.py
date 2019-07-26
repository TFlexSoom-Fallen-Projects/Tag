# Tristan Hilbert
# Simple Port Script
#
#
# Port -> 7019

# Network Globals
from classes import Box, Objective, Player
from pygame import Color
import random
import sys
import socket
import time
import traceback
ipv4_address = '127.0.0.1'
port = 7027

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ipv4_address, port))
###################

# Server Game Info

map_width = 1024
map_height = 768
objectives = []
players = []
#############

# Auxillary Class


class ServerPlayer(Player):

    def __init__(self, connection):
        Player.__init__(self)
        self.connection = connection


def spawn():
    x = 0
    y = 0
    for i in range(30):
        objectives.append(Objective())
        x = random.randint(0, map_width - 20)
        y = random.randint(0, map_width - 20)
        objectives[-1].box.rect.center = (x, y)
    for i in players:
        x = random.randint(0, map_width - 20)
        y = random.randint(0, map_width - 20)
        i.box.rect.center = (x, y)
        i.box.color = Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        


def update():
    for i in players:
        command = i.connection.recv(1024).decode("ascii")
        if(len(command) > 0):
            command = command[1:-1]
        
        if(len(command) > 0):
            direction = command[-2:]
            if len(direction) > 1 and direction[0] != 'N' and direction[0] != 'S':
                direction = direction[:-1]
            if len(direction) > 1 and direction[1] != 'E' and direction[1] != 'W':
                direction = direction[:-1]
            i.move(direction)
        for j in objectives:
            j.handleCollision(i.box)


def send():
    manip = ''
    for i in players:
        for j in players:
            manip = ''
            manip += str(j.box.rect.centerx) + ',' + str(j.box.rect.centery)
            manip += ',' + str(j.box.color.r) + ',' + str(j.box.color.g)
            manip += ',' + str(j.box.color.b)
            manip += '|'
            i.connection.send(str.encode(manip))
        i.connection.send(b'=')
        for j in objectives:
            manip = ''
            manip += str(j.box.rect.centerx) + ',' + str(j.box.rect.centery)
            manip += ',' + str(j.box.color.r) + ',' + str(j.box.color.g)
            manip += ',' + str(j.box.color.b)
            manip += '|'
            i.connection.send(str.encode(manip))
        i.connection.send(b'}')


def main():
    while True:
        try:
            a = 0
            while a != 1:
                try:
                    sock.settimeout(20)
                    sock.listen(0)
                    print("Started Connection!")

                    conn, addr = sock.accept()
                    conn.settimeout(None)
                    players.append(ServerPlayer(conn))
                    print("Connection!")
                except socket.timeout:
                    print("Timeout!")
                finally:
                    a = int(input("Continue Checking?"))
                    if a == 2:
                        raise Exception("Clear Game!")
            sock.settimeout(None)
            spawn()
            while len(players) > 0:
                send()
                update()

        except Exception:
            traceback.print_exc()

        finally:
            for i in players:
                i.connection.close()
            sock.close()
            break


if __name__ == "__main__":
    main()
