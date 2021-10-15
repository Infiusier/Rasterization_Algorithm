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
        self.lines = []
        self.matrix = np.zeros((length , width, 1 ))
    
    def draw_line(self,line):
        
        self.lines.append(line)
        
        point_1 = line[0]
        point_2 = line[1]
        
        x1 = (point_1[0])
        y1 = (point_1[1])
        x2 = (point_2[0])
        y2 = (point_2[1])
        
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
            #print("oi")
            self.m=0
            
        self.b = y1 - (self.m*x1)

        if abs(self.deltaX) > abs(self.deltaY):
            for x in range(int(self.Xmin), int(self.Xmax) +1):
                y = self.m*x + self.b
                x = math.floor(x)
                y = math.floor(y)
                
                self.matrix[y][x] = 1
        else:
            for y in range(int(self.Ymin), int(self.Ymax) +1):
                try:
                    x = (y-self.b)/self.m
                    x = math.floor(x)
                except:
                    #print("oi")
                    x =  self.Xmin
                    
                y = math.floor(y)
                self.matrix[y][x] = 1

    def plot(self):
        
        plt.imshow(self.matrix,'gray',origin='lower',extent=(0, self.width, 0, self.length))
        #plt.plot([self.x1,self.x2],[self.y1,self.y2],linestyle='-');
        
        for line in self.lines:
            plt.plot([line[0][0],line[1][0]],[line[0][1],line[1][1]],linestyle='-');
            pass
        
        plt.show();
        
        self.lines.clear()
        
        
    def draw_convex_polygon(self,lines):
        x_pos = []
        y_pos = []
        x_start = 0
        x_end = 0
        
        for line in lines:
            self.draw_line(line)
            
            for point in line:
                x_pos.append(point[0])
                y_pos.append(point[1])
            
        #x_min = int(min(x_pos))
        y_min = int(min(y_pos))
        
        #x_max = int(max(x_pos))
        y_max = int(max(y_pos))
        
        for line in range(y_min,y_max):
    
            for column in range(0,self.width-1):
                if self.matrix[line][column] == 1:
                    x_start = column
                    break
                
            for column in range(self.width-1,0,-1):

                if self.matrix[line][column] == 1:
                    x_end = column
                    break
                 
            for column in range(x_start,x_end):
                self.matrix[line][column] = 1
        
        

if __name__ == '__main__':
    line_1 = [[16,5],[43,17]]
    line_2 = [[43,17],[36,43]]
    line_3 = [[36,43],[3,40]]
    line_4 = [[3,40],[16,5]]
    
    square = []
    square.append(line_1)
    square.append(line_2)
    square.append(line_3)
    square.append(line_4)

    matrix_1 = Matrix(50,50)
    #matrix_1.draw_line(line_1)
    #matrix_1.draw_line(line_2)
    #matrix_1.draw_line(line_3)
    #matrix_1.draw_line(line_4)
    
    matrix_1.draw_convex_polygon(square)
  
    matrix_1.plot()