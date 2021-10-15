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
    
    def draw_line(self,line):
        
        point_1 = line[0]
        point_2 = line[1]
        
        x1 = math.floor(point_1[0])
        y1 = math.floor(point_1[1])
        x2 = math.floor(point_2[0])
        y2 = math.floor(point_2[1])
        
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        
        xs = [self.x1, self.x2]
        ys = [self.y1, self.y2]
    
        xs.sort()
        ys.sort()
    
        self.Xmin, self.Xmax = xs
        self.Ymin, self.Ymax = ys
        
        self.deltaX = x2 - x1
        self.deltaY = y2 - y1
        
        try:
            self.m = self.deltaY / self.deltaX
        except:
            print("oi")
            self.m=0
            
        self.b = y1 - (self.m*x1)

        if abs(self.deltaX) > abs(self.deltaY):
            for x in range(self.Xmin, self.Xmax ):
                y = self.m*x + self.b
                x = math.floor(x)
                y = math.floor(y)
                self.matrix[y][x] = 1
        else:
            for y in range(self.Ymin, self.Ymax ):
                try:
                    x = (y-self.b)/self.m
                    x = math.floor(x)
                except:
                    print("oi")
                    x =  self.Xmin
                    
                y = math.floor(y)
                self.matrix[y][x] = 1

    def plot(self):
        
        plt.imshow(self.matrix,'gray',origin='lower',extent=(0, self.width, 0, self.length))
        plt.plot([self.x1,self.x2],[self.y1,self.y2],linestyle='-');
        
        plt.show();

if __name__ == '__main__':
    line_1 = [[0,5],[9,5]]

    matrix_1 = Matrix(10,10)
    matrix_1.draw_line(line_1)
  
    matrix_1.plot()