import numpy as np
import math
import matplotlib.pyplot as plt

class Matrix:
    '''deltaX: float
    deltaY: float
    b: float
    m: float'''

    def __init__(self,width,length):
        self.width = width
        self.length = length
        self.matrix = np.zeros((length , width, 1 ))
    
    def draw_line(self,x1,y1,x2,y2):
        self.x1=int(x1)
        self.x2=int(x2)
        self.y1=int(y1)
        self.y2=int(y2)
        
        xs = [self.x1, self.x2]
        ys = [self.y1, self.y2]
    
        xs.sort()
        ys.sort()
    
        self.Xmin, self.Xmax = xs
        self.Ymin, self.Ymax = ys
        
        self.deltaX = x2 - x1
        self.deltaY = y2 - y1
        
        self.m = self.deltaY / self.deltaX
        self.b = y1 - (self.m*x1)

        if abs(self.deltaX) > abs(self.deltaY):
            for x in range(self.Xmin, self.Xmax ):
                y = self.m*x + self.b
                x = math.floor(x)
                y = math.floor(y)
                self.matrix[x][y] = 1
        else:
            for y in range(self.Ymin, self.Ymax ):
                x = (y-self.b)/self.m
                x = math.floor(x)
                y = math.floor(y)
                self.matrix[x][y] = 1

    def plot(self):
        
        plt.imshow(self.matrix,'gray',origin='lower',extent=(0, self.width, 0, self.length))
        plt.plot([self.x1,self.y1],[self.x2,self.y2],linestyle='-');
        
        plt.show();

if __name__ == '__main__':

    matrix_1 = Matrix(50,50)
    matrix_1.draw_line(0,0,5,50)
  
    matrix_1.plot()