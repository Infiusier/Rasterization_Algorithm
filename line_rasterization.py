import numpy as np
import math
import matplotlib.pyplot as plt

ENABLE_LINE_PLOT = 1

class Matrix:

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
        
        list_of_x = [self.x1, self.x2]
        list_of_y = [self.y1, self.y2]
    
        list_of_x.sort()
        list_of_y.sort()
    
        self.x_min, self.x_max = list_of_x
        self.y_min, self.y_max = list_of_y
        
        self.delta_x = x2 - x1
        self.delta_y = y2 - y1
        
        try:
            self.m = self.delta_y / self.delta_x
        except:
            self.m=0
            
        self.b = y1 - (self.m*x1)

        if abs(self.delta_x) > abs(self.delta_y):
            for x in range(int(self.x_min), int(self.x_max) +0):
                y = self.m*x + self.b
                x = math.floor(x)
                y = math.floor(y)
                
                self.matrix[y][x] = 1
        else:
            for y in range(int(self.y_min), int(self.y_max) +0):
                try:
                    x = (y-self.b)/self.m
                    x = math.floor(x)
                except:
                    x =  self.x_min
                    
                y = math.floor(y)
                self.matrix[y][x] = 1

    def plot(self):
        
        plt.imshow(self.matrix,'gray',origin='lower',extent=(0, self.width, 0, self.length))
        #plt.plot([self.x1,self.x2],[self.y1,self.y2],linestyle='-');
        
        for line in self.lines:
            if ENABLE_LINE_PLOT == 1:
                plt.plot([line[0][0],line[1][0]],[line[0][1],line[1][1]],linestyle='-');
        
        plt.show();
        
        self.matrix = np.zeros((self.length , self.width, 1 ))
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
            
        y_min = int(min(y_pos))
        
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
                pass
        
        

