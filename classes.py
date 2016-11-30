'''
Created on Oct 24, 2016

@author: farida
'''

def compare(self,x1,y1,x2,y2):
    if(x2>x1 and y2>y1):
        return True
    
class Point:
    def __init__(self,x,y ):
        self.x = x
        self.y = y

class Rectangle:
    """A rectangle class defined by the starting point and the ending point"""
    color="Blue"  # class variable shared by all instances
    f = compare
    def __init__(self, x1=0, y1=0,x2=0,y2=0):
        if(self.f(x1,y1,x2,y2)):
            self.x1= x1
            self.x2= x2
            self.y1= y1
            self.y2= y2
        
    def _initPoints(self,p1,p2):
        self.x1 = p1.x
        self.y1 = p1.y
        self.x2 = p2.x
        self.y2 = p2.y
        
    
    def getLength(self):
        return self.x2 - self.x1
    
    def getWidth(self):
        return self.y2-  self.y1
    
    def printRectangle(self):
        print("Coordinates of bottom left corner:("+str(self.x1)+","+str(self.y1)+")")
        print("Coordinates of top right corner:("+str(self.x2)+","+str(self.y2)+")")
        print("Length="+str(self.getLength()))
        print("Width="+str(self.getWidth()))

p1=Point(1,1)
p2=Point(7,5)
rect=Rectangle(p1.x,p1.y,p2.x, p2.y)
rect.printRectangle()
rect2= Rectangle()
rect2._initPoints(p1, p2)
rect2.printRectangle()
print(rect.__doc__) #prints the documentation line at the class definition
print(Rectangle.color)

for line in open("myfile.txt"):
    print(line, end='')
    coordinates= line.split(" ")
    rect=Rectangle(int(coordinates[0]),int(coordinates[1]),int(coordinates[2]), int(coordinates[3]))
    rect.printRectangle()
