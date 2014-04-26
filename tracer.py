#! /usr/bin/python

from cube import *

class EllipticalTracer:
    #Axial Scales
    a = 1; b = 1; c = 1
    z = 0;
    
    #Cursor Location
    class Cursor:
        x = 0.0; y = 0.0; dir = 0; size = 1; nogo = 3;
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
        #We will select the side closet to the curve, indecies are the dir.
        #forward = 0, right = 1, back = 2, left = 3
        distancesToCurve = ["NULL", "NULL", "NULL", "NULL"];
        directionHuman = ["Front", "Right", "Back", "Left"];
        
        if (self.calculateXGivenY(self.cursor.y+self.cursor.size) != "NULL"):
            #Check forward direction.
            value = self.calculateXGivenY(self.cursor.y+self.cursor.size)
            if (self.cursor.nogo != 0):
                distancesToCurve[0] = abs(value - self.cursor.x);

        if (self.calculateXGivenY(self.cursor.y-self.cursor.size) != "NULL"):
            #Check backward direction.
            value = self.calculateXGivenY(self.cursor.y-self.cursor.size)
            if (self.cursor.nogo != 2):
                distancesToCurve[2] = abs(value - self.cursor.x);

        if (self.calculateYGivenX(self.cursor.x+self.cursor.size) != "NULL"):
            #Check right direction.
            value = self.calculateYGivenX(self.cursor.x+self.cursor.size)
            if (self.cursor.nogo != 1):
                distancesToCurve[1] = abs(value - self.cursor.y);
                    
        """if (self.calculateYGivenX(self.cursor.x-self.cursor.size) != "NULL"):
            #Check left direction.
            value = self.calculateYGivenX(self.cursor.x-self.cursor.size)
            if (self.cursor.nogo != 3):
                distancesToCurve[3] = abs(value - self.cursor.y);"""

        minerror = -1; minindex = -3
        for distanceIndex in range(len(distancesToCurve)):
            if (distancesToCurve[distanceIndex] != "NULL"):
                #print "x:", self.cursor.x, "dir:", directionHuman[distanceIndex], "error:", distancesToCurve[distanceIndex];
                #print self.cursor.x, ",", directionHuman[distanceIndex], ",", distancesToCurve[distanceIndex];
                if (distancesToCurve[distanceIndex] < minerror or minerror <= -1):
                    minerror = distancesToCurve[distanceIndex];
                    minindex = distanceIndex;

        self.cursor.nogo = (minindex+2)%4
        return directionHuman[minindex];
                


    def __init__(self, _a = 1, _b = 1, _c = 1, x=1):
        self.a = _a; self.b = _b; self.c = _c;
        self.cursor = self.Cursor(x, self.calculateYGivenX(x), 0, .06)



ellipse = EllipticalTracer(1, .5, 1, 0)

queue = [(0,ellipse.calculateYGivenX(0)/ellipse.cursor.size,1)]
drawscale = .01
#Draw curve.
for point in range(int(math.ceil(ellipse.calculateXGivenY(0)/drawscale))):
    queue.append((point*drawscale, ellipse.calculateYGivenX(point*drawscale)))

#Voxelize.
while (ellipse.cursor.x < ellipse.calculateXGivenY(0)):
    direction = ellipse.whereToGo()
    print ellipse.cursor.x, ellipse.cursor.y, direction, point*drawscale, ellipse.calculateYGivenX(point*drawscale), point

    if (direction == "Front"):
        ellipse.cursor.y += ellipse.cursor.size

    elif (direction == "Right"):
        ellipse.cursor.x += ellipse.cursor.size

    elif (direction == "Back"):
            ellipse.cursor.y -= ellipse.cursor.size

    elif (direction == "Left"):
        ellipse.cursor.x -= ellipse.cursor.size

    queue.append((ellipse.cursor.x/ellipse.cursor.size, ellipse.cursor.y/ellipse.cursor.size, 1))


x = Render()
x.pointqueue = queue
x.setup(500)