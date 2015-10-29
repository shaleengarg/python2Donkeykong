#!/usr/bin/python2

import sys
import os
import board
import random
import time

##class for movement

class Movement():

    def __init__(self, x, y, s):
        self.i = x
        self.j = y
        self.sign = s
        self.before = " "
        mmap.data[self.i][self.j] = self.sign


    def moveleft(self):
        mmap.data[self.i][self.j] = self.before
        self.j -= 1
        self.before = mmap.data[self.i][self.j]
        if self.before == "D":
            self.before = " "

        mmap.data[self.i][self.j] = self.sign


    def moveright(self) :
        mmap.data[self.i][self.j] = self.before
        self.j +=1
        self.before = mmap.data[self.i][self.j]
        if self.before == "D":
            self.before = " "

        mmap.data[self.i][self.j] = self.sign


####Class for implementing Gravity and jump

class gravity() :

    def freefall(self):
        if mmap.data[self.i+1][self.j] == " ":
            while mmap.data[self.i+1][self.j] !="X":
                self.i +=1
                mmap.data[self.i][self.j] = self.sign
                mmap.data[self.i-1][self.j] = " "
                self.nextframe()
                time.sleep(0.10)
        else:
            pass

    def jumproutine(self):                   ##### For code reuse !!! figured out very late >... New to OOPS
        self.before = mmap.data[self.i][self.j]
        self.checkcoin()
        mmap.data[self.i][self.j] = self.sign
        self.nextframe()
        time.sleep(0.10)
        

    def jumpright(self):   
        temp =0                            #####To avoid further code execution if a wall is encountered
        mmap.data[self.i][self.j] = self.before
        self.i -=1
        self.j +=1
        if mmap.data[self.i][self.j] != "X":
            self.jumproutine()

        else:
            temp = 1
            self.i+=1
            self.j-=1
            self.before = " "
        

        if temp == 0:
            mmap.data[self.i][self.j] = self.before
            self.i -=1
            self.j +=1
            if mmap.data[self.i][self.j] != "X":
                self.jumproutine()

            else:                                      ####### For looking up wall while jump
                temp = 1
                self.i+=1
                self.j-=1
                mmap.data[self.i][self.j] = " "
                self.i+=1
                mmap.data[self.i][self.j] = self.sign
                self.before = " "

        if temp == 0:
            mmap.data[self.i][self.j] = self.before
            self.i +=1
            self.j +=1
            if mmap.data[self.i][self.j] != "X":
                self.jumproutine()

            else:                                      ####### For looking up wall while jump
                temp = 1
                self.i+=1
                self.j-=1
                mmap.data[self.i][self.j] = self.sign


        if temp == 0:
            mmap.data[self.i][self.j] = self.before
            self.i +=1
            self.j +=1
            if mmap.data[self.i][self.j] != "X":
                self.jumproutine()
                self.freefall()

            else:
                temp = 1
                self.j -=1
                mmap.data[self.i][self.j] = self.sign
        temp = 0
        

    def jumpleft(self):   
        temp = 0                        #######var to stop further jump code execution if a wall i encountererd
        mmap.data[self.i][self.j] = self.before
        self.i -=1
        self.j -=1

        if mmap.data[self.i][self.j] != "X":
            self.jumproutine()

        else :                               ### Looking for Wall while jumping left
            temp =1
            self.i +=1
            self.j +=1
            mmap.data[self.i][self.j] = self.sign
            self.before = " "


        if temp == 0 :
            mmap.data[self.i][self.j] = self.before
            self.i -=1
            self.j -=1
            if mmap.data[self.i][self.j] != "X":
                self.jumproutine()

            else:
                temp = 1
                self.i +=1
                self.j +=1
                mmap.data[self.i][self.j] = " "
                self.i +=1
                mmap.data[self.i][self.j] = self.sign


        if temp == 0 :
            mmap.data[self.i][self.j] = self.before
            self.i +=1
            self.j -=1
            if mmap.data[self.i][self.j] != "X":
                self.jumproutine()

            else :
                temp = 1
                self.i +=1
                self.j +=1
                mmap.data[self.i][self.j] = self.sign


        if temp == 0 :
            mmap.data[self.i][self.j] = self.before
            self.i +=1
            self.j -=1
            if mmap.data[self.i][self.j] != "X":
                self.jumproutine()
                self.freefall()

            else:
                temp = 1
                self.j +=1
                mmap.data[self.i][self.j] = self.sign
        temp = 0



##############Class for the main player P

class player(Movement, gravity):    
    
    def __init__(self, x, y, s):          
        Movement.__init__(self, x, y, s)
        self.life = 3
        self.points = 0             ######points for collecting coins
        self.nextframe()
        self.movingup = 0             ########### variable to see if player is going up or not


    def checkCollision(self):          ######### Check if the player collided with donkey or fireball
        if self.before == "O" or self.before == "D":
            self.life -=1
            self.before = " "
            mmap.data[self.i][self.j] = self.before
            self.i = 34
            self.j = 2
            mmap.data[self.i][self.j] = self.sign
        if self.life < 0:
            sys.exit("You LOOSE!!!")

    def nextframe(self):               ###### Print board with updated results
        #d1.randomove(board.width-45, 2)
        mmap.Print()
        r = str(self.points)
        print "Player points = " + r
        r = str(self.life)
        print "Player lives = " + r

    def checkcoin(self):             ###### Check if coin is collected by player
        if self.before == "C":
            self.points +=5
            self.before = " "

    def moveroutine(self):          #### Code Reuse !!
        self.before = mmap.data[self.i][self.j]
        self.checkCollision()
        if self.before == "P":
            self.before = " "
        mmap.data[self.i][self.j] = self.sign
        self.checkcoin()
        self.freefall()

    def moveup(self):
        
        if self.movingup == 1:
            mmap.data[self.i][self.j] = self.before
            if self.before == "P":
                self.before = " "
            self.i -= 1
            self.before =  mmap.data[self.i][self.j]
            mmap.data[self.i][self.j] = self.sign
            self.movingup = 0

        elif self.movingup == 0 :
            if mmap.data[self.i -1][self.j] == " " :
                pass
            else:
                mmap.data[self.i][self.j] = self.before
                self.i-=1
                self.before =  mmap.data[self.i][self.j]
                self.checkCollision()
                if self.before == "H" :
                    self.movingup = 1
                mmap.data[self.i][self.j] = self.sign
        self.checkcoin()

    def moveleft(self):
        if mmap.data[self.i][self.j-1] == "X" :
            pass
        else :
            mmap.data[self.i][self.j] = self.before
            self.j -=1
            self.moveroutine()
        self.checkCollision()

    def moveright(self) :
        if mmap.data[self.i][self.j+1] == "X":
            pass
        else :
            mmap.data[self.i][self.j] = self.before
            self.j +=1
            self.moveroutine()
        self.checkCollision()

    def movedown(self):
        if mmap.data[self.i+1][self.j] == "H":
            mmap.data[self.i][self.j] = self.before
            self.i+=1
            self.before =  mmap.data[self.i][self.j]
            mmap.data[self.i][self.j] = self.sign
        else:
            pass
        self.checkcoin()
        self.checkCollision()
    

class Donkey(Movement, player):

    def __init__(self, x, y, s):
        Movement.__init__(self, x, y, s)
        self.currentdir = 0           ###currentdir == current direction variable 0 == right, 1 == left

    def randomove(self, x, y) :
        a= random.random()
        if a > 0.95:
            if self.currentdir == 0:
                if self.j < x:
                    self.moveright()
                else:
                    self.currentdir = 1

            else :
                if self.j > 1 :
                    self.moveleft()

                else:
                    self.currentdir = 0

class Fireball():

    def __init__(self, j, sign):
        self.i = 5                 ##### The fireball always spawns on the highest level
        self.j = j                 ##### j of the donkey at that instance
        self.sign = sign
        self.m = 0                 ##### to see if the fireball is moving right or left  0 -> right && 1-> left
        self.before = " " 

    def move(self):
        a = random.random()
        if a > 0.7:
            if self.m == 0:
        	    if mmap.data[self.i][self.j+1] != "X":
        	        self.moveright()

                    else :
                        self.m = 1
                        pass

            elif self.m == 1:
                if mmap.data[self.i][self.j-1] != "X":
                    self.moveleft()

                else :
                    self.m = 0
                    pass


    def moveleft(self):
        mmap.data[self.i][self.j] = self.before
        self.j -=1
        self.before = mmap.data[self.i][self.j]
        if self.before == "O" or self.before == "D":
            self.before = " "
        mmap.data[self.i][self.j] = self.sign
        self.freefall()


    def moveright(self):
        mmap.data[self.i][self.j] = self.before
        self.j +=1
        self.before = mmap.data[self.i][self.j]
        if self.before == "O" or self.before == "D":
            self.before = " "
        mmap.data[self.i][self.j] = self.sign
        self.freefall()


    def freefall(self):                        ######Special freefall for fireballs
        if mmap.data[self.i+1][self.j] == " ":
            while mmap.data[self.i+1][self.j] != "X":
                self.i +=1
                mmap.data[self.i][self.j] = self.sign
                mmap.data[self.i-1][self.j] = " "
                p1.nextframe()


    def __del__(self):
        self.sign = " "


### Defining the Needful
mmap = board.Map()
d1 = Donkey(5,2,"D")
p1 = player(34,2,"P")
