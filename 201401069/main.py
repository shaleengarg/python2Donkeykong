#!/usr/bin/python2

from person import *
from Kbhit import *
import os
import sys
import time
import random
from board import *


### Class for the one player gameplay

class Gameplay(player, Donkey):

    def __init__(self):
        global d
        #global mmap
        #mmap = board.Map()
        d = KBHit()
        global FB
        FB = []

    def nextf(self):           #######Calling the new board
	d1.randomove(board.width-46, 2)
	p1.nextframe()
    
    def scan_ip(self):          ####### Scanning for keyboard input and spawning new fireballs also checking for collisions and wins
        direction = "p"
        time.sleep(0.01)
        if d.kbhit():
           direction = d.getch()
	d1.randomove(board.width-45, 2)

        ############spawning new Fireballs
        a = random.random()
        if a > 0.995 : 
            b = Fireball(d1.j+1,"O")
            FB.append(b)
        for a in xrange(0,len(FB)-1):
            if FB[a].i == 34 and FB[a].j == 2:
                mmap.data[34][2] = " "
                del FB[a]
            else:
                FB[a].move()
        ###### END of New fireballs
        ##### Doing the needfull with the Keyboard input
	if direction == 'w':
		p1.moveup()
		self.nextf()
	elif direction == 'a':
		p1.moveleft()
		self.nextf()
	elif direction == 's':
		p1.movedown()
		self.nextf()
	elif direction == 'd':
		p1.moveright()
		self.nextf()
	elif direction == ' ':
                direction = d.getch()
                if direction == "d":
		    p1.jumpright()
                elif direction == "a":
                    p1.jumpleft()
	        self.nextf()
        elif direction == 'q':
            os.system("clear")
            sys.exit("quit game")
	else:
		self.nextf()
		pass

 ### Collision check on player being stationary ###########        

        if mmap.data[p1.i][p1.j] == "O" or mmap.data[p1.i][p1.j] == "D":
            p1.life -=1
            if p1.life == 0:
                sys.exit("You LOOSE !")
        if mmap.data[p1.i][p1.j-1] == "Q":
            sys.exit("You Won!!!")


#Let the Gaming Begin!!!
def main():

    game = Gameplay()
    while (1):
        game.scan_ip()

main()
