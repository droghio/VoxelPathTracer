#! /usr/bin/python

from cube import *

class EllipticalTracer:
    #Axial Scales
    a = 1; b = 1; c = 1
    z = 0;
    
    #Cursor Location
    class Cursor:
        x = 0.0; y = 0.0; dir = 0; size = 1; nogo = 0;
        def __init__(self, _x = 0.0, _y = 0.0, _dir = 0, _size = 1.0):
            self.x = _x; self.y = _y; self.dir = _dir; self.size = _size;
        #For dir: +y = 0, +x = 1, -y = 2, -x = 3
    
    cursor = Cursor()

    def calculateXGivenY(self, y):
        returnvalue = 0;
        try:
            #Equation for an ellipse solving for the x value.
            # x = sqrt((1-a(y^2)/b)
            returnvalue = ((1-self.a*(y)**2)/self.b)**.5

        except ValueError:
            #If there is no x coordinate for the given y value return NULL.
            return "NULL"

        return returnvalue


    def calculateYGivenX(self, x):
        returnvalue = 0;
        try:
            #Equation for an ellipse solving for the x value.
            # y = sqrt((1-b(x^2)/a)
            returnvalue = ((1-self.b*(x)**2)/self.a)**.5
        
        except ValueError:
            #If there is no x coordinate for the given y value return NULL.
            return "NULL"
        
        return returnvalue


    def whereToGo(self):
        if (self.calculateXGivenY(self.cursor.y+self.cursor.size) != "NULL"):
            #Check forward direction.
            value = self.calculateXGivenY(self.cursor.y+self.cursor.size)
            if (value < self.cursor.x + self.cursor.size and
                value > self.cursor.x - self.cursor.size and self.cursor.nogo != 0):
                nogo = 2
                return "Front";

        if (self.calculateXGivenY(self.cursor.y-self.cursor.size) != "NULL"):
            #Check backward direction.
            value = self.calculateXGivenY(self.cursor.y-self.cursor.size)
            if (value < self.cursor.x + self.cursor.size and
                value > self.cursor.x - self.cursor.size and self.cursor.nogo != 2):
                nogo = 0
                return "Back";

        if (self.calculateYGivenX(self.cursor.x+self.cursor.size) != "NULL"):
            #Check right direction.
            value = self.calculateYGivenX(self.cursor.x+self.cursor.size)
            if (value < self.cursor.y + self.cursor.size and
                value > self.cursor.y - self.cursor.size and self.cursor.nogo != 1):
                nogo = 3
                return "Right";




    def __init__(self, _a = 1, _b = 1, _c = 1, x=1):
        self.a = _a; self.b = _b; self.c = _c;
        self.cursor = self.Cursor(x, self.calculateYGivenX(x), 0, .1)



ellipse = EllipticalTracer(1, .5, 1, 0)
print ellipse.calculateXGivenY(.5)
print ellipse.calculateYGivenX(0)
print ellipse.whereToGo();

queue = []
for point in range(141):

    queue.append((point/100.0, ellipse.calculateYGivenX(point/100.0)))
    print queue[-1]

    direction = ellipse.whereToGo()
    print ellipse.cursor.x, direction

    if (point % 1 == 0):
        queue.append((ellipse.cursor.x*10, ellipse.cursor.y*10, 1))

    #ellipse.cursor.x = queue[-1][0]/100.0
    #ellipse.cursor.y = queue[-1][1]/100.0
    
    if (direction == "Front"):
        ellipse.cursor.y += ellipse.cursor.size
    
    elif (direction == "Right"):
        ellipse.cursor.x += ellipse.cursor.size
    
    elif (direction == "Back"):
        ellipse.cursor.y -= ellipse.cursor.size


x = Render()
x.pointqueue = queue
x.setup(500)