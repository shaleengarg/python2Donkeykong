#!/usr/bin/python2
'''THIS IS Coded By SHALEEN GARG Rollno : 201401069 '''


import sys
import numpy 
import random

width = 114 
height = 36

class Map():

    def __init__(self):
        self.data = [[" " for x in xrange(width)]for y in xrange(height)]

        for i in xrange(0,width):                       ## making the four walls
            self.data[0][i] = "X"
        for i in xrange(0,width):
            self.data[height-1][i] = "X"
        for i in xrange(0,height):
            self.data[i][0] = "X"
        for i in xrange(0,height):
            self.data[i][width-1] = "X"                 ##end of four walls
       
       # mking of the floors
            
        for i in xrange(0,width-45):
            self.data[6][i] = "X"
        for i in xrange(20,width):
            self.data[12][i] = "X"
        for i in xrange(0,width-35):
            self.data[18][i] = "X"
        for i in xrange(25,width):
            self.data[24][i] = "X"
        for i in xrange(0,width-30):
            self.data[30][i] = "X"

        #the place of the princess

        for i in xrange(30,width-60):
            self.data[2][i] = "X"

        self.data[1][30] = "X"
        self.data[1][32] = "Q"
        self.data[1][53] = "X"

        ##Making of the ladders
        
        for i in xrange(30,height-1):    #### 0th floor to 1st floor ##### 1 ladder full
            self.data[i][75] = "H"
        
        for i in xrange(24, height-6):   ### 1 st floor to 2nd floor ### 1 full ladder && 1 half ladder
            self.data[i][65] = "H"
        self.data[i-1][65] = " "
        self.data[i-2][65] = " "
        for i in xrange(24, height-6):
            self.data[i][40] = "H"

        for i in xrange(18,height-12):   ###2nd floor to 3rd floor same as above
            self.data[i][68] = "H"
        for i in xrange(18,height-12):
            self.data[i][45] = "H"
        self.data[i-1][45] = " "
        self.data[i-2][45] = " "
        
        for i in xrange(12,height-18):   ##3rd to 4th 1 full ladder
            self.data[i][35] = "H"

        for i in xrange(6, height-24):   ### 4th to 5th floor  same as the first
            self.data[i][25] = "H"
        self.data[i-1][25] = " "
        self.data[i-2][25] = " "
        for i in xrange(6, height-24):
            self.data[i][55] = "H"

        for i in xrange(2, height-30):    ####finally to the princess!!!!
            self.data[i][45] = "H"

        self.Coin()
        
    def Print(self):
        for j in xrange(0,height):
            for i in self.data[j]:
                sys.stdout.write(i)
            print " "

    def Coin(self):
        ######### Generating random coins on each level #############
        for x in xrange(0,5):                   ### Top level 
            j = random.randint(1,width-2)
            if self.data[height-2][j] != "H" and self.data[height-2][j] != "C":
                self.data[height-2][j] = "C"

        for x in xrange(0,5):                   ####  5th level
            j = random.randint(1,width-31)
            if self.data[height-7][j] != "H" and self.data[height-7][j]!= "C":
                self.data[height-7][j] = "C"

        for x in xrange(0,5):                  #### 4th level
            j = random.randint(25,width-2)
            if self.data[height-13][j] != "H" and self.data[height-13][j]!= "C":
                self.data[height-13][j] = "C"

        for x in xrange(0,5):                    #### 3rd level
            j = random.randint(1,width-45)
            if self.data[height-19][j] != "H" and self.data[height-19][j]!= "C":
                self.data[height-19][j] = "C"

        for x in xrange(0,5):                    #### 2nd level
            j = random.randint(25, width-2)
            if self.data[height-25][j] != "H" and self.data[height-25][j]!= "C":
                self.data[height-25][j] = "C"

        for x in xrange(0,3):                    ##### 1st level
            j = random.randint(45,width-45)
            if self.data[height-31][j] != "H" and self.data[height-31][j]!= "C":
                self.data[height-31][j] = "C"



#test
def main():
    mapp = Map()
    mapp.Print()


if __name__ == "__main__":
    main()
