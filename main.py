from line_rasterization import *

if __name__ == '__main__':
    matrix_1 = Matrix(50,50)
    matrix_2 = Matrix(100,100)
    matrix_3 = Matrix(200,200)
    
    line_1 = [[5,5],[25,49]]
    line_2 = [[1,1],[1,49]]
    line_3 = [[3,3],[49,3]]
    line_4 = [[10,10],[45,45]]
    
    triangule_1 = [[0,0],[42,0]]
    triangule_2 = [[42,0],[21,35]]
    triangule_3 = [[21,35],[0,0]]
    
    triangule_4 = [[10,37],[42,37]]
    triangule_5 = [[42,37],[26,12]]
    triangule_6 = [[26,12],[10,37]]
    
    square_1 = [[10,10],[10,40]]
    square_2 = [[10,40],[40,40]]
    square_3 = [[40,40],[40,10]]
    square_4 = [[40,10],[10,10]]
    
    square_5 = [[24,38],[38,21]]
    square_6 = [[38,21],[24,7]]
    square_7 = [[24,7],[9,23]]
    square_8 = [[9,23],[24,38]]
    
    hexagon_1 = [[15,38],[32,38]]
    hexagon_2 = [[32,38],[39,23]]
    hexagon_3 = [[39,23],[32,9]]
    hexagon_4 = [[32,9],[15,9]]
    hexagon_5 = [[15,9],[8,23]]
    hexagon_6 = [[8,23],[15,38]]
    
    hexagon_7 = [[10,33],[24,41]]
    hexagon_8 = [[24,41],[38,33]]
    hexagon_9 = [[38,33],[38,16]]
    hexagon_10 = [[38,16],[24,9]]
    hexagon_11 = [[24,9],[10,16]]
    hexagon_12 = [[10,16],[10,33]]
    
    rm = 1 #Resolution Multiplier
    
    line_1_50x50 = np.multiply(line_1,rm)
    line_2_50x50 = np.multiply(line_2,rm)
    line_3_50x50 = np.multiply(line_3,rm)
    line_4_50x50 = np.multiply(line_4,rm)
    
    square_1_50x50 = [np.multiply(square_1,rm),np.multiply(square_2,rm),np.multiply(square_3,rm),np.multiply(square_4,rm)]
    square_2_50x50 = [np.multiply(square_5,rm),np.multiply(square_6,rm),np.multiply(square_7,rm),np.multiply(square_8,rm)]
    
    triangule_1_50x50 = [np.multiply(triangule_1,rm),np.multiply(triangule_2,rm),np.multiply(triangule_3,rm)]
    triangule_2_50x50 = [np.multiply(triangule_4,rm),np.multiply(triangule_5,rm),np.multiply(triangule_6,rm)]
    
    hexagon_1_50x50 = [np.multiply(hexagon_1,rm),np.multiply(hexagon_2,rm),np.multiply(hexagon_3,rm),np.multiply(hexagon_4,rm),np.multiply(hexagon_5,rm),np.multiply(hexagon_6,rm)]
    hexagon_2_50x50 = [np.multiply(hexagon_7,rm),np.multiply(hexagon_8,rm),np.multiply(hexagon_9,rm),np.multiply(hexagon_10,rm),np.multiply(hexagon_11,rm),np.multiply(hexagon_12,rm)]
    
    rm = 2
    
    line_1_100x100 = np.multiply(line_1,rm)
    line_2_100x100 = np.multiply(line_2,rm)
    line_3_100x100 = np.multiply(line_3,rm)
    line_4_100x100 = np.multiply(line_4,rm)
    
    square_1_100x100 = [np.multiply(square_1,rm),np.multiply(square_2,rm),np.multiply(square_3,rm),np.multiply(square_4,rm)]
    square_2_100x100 = [np.multiply(square_5,rm),np.multiply(square_6,rm),np.multiply(square_7,rm),np.multiply(square_8,rm)]
    
    triangule_1_100x100 = [np.multiply(triangule_1,rm),np.multiply(triangule_2,rm),np.multiply(triangule_3,rm)]
    triangule_2_100x100 = [np.multiply(triangule_4,rm),np.multiply(triangule_5,rm),np.multiply(triangule_6,rm)]
    
    hexagon_1_100x100 = [np.multiply(hexagon_1,rm),np.multiply(hexagon_2,rm),np.multiply(hexagon_3,rm),np.multiply(hexagon_4,rm),np.multiply(hexagon_5,rm),np.multiply(hexagon_6,rm)]
    hexagon_2_100x100 = [np.multiply(hexagon_7,rm),np.multiply(hexagon_8,rm),np.multiply(hexagon_9,rm),np.multiply(hexagon_10,rm),np.multiply(hexagon_11,rm),np.multiply(hexagon_12,rm)]
    
    rm = 4
    
    line_1_200x200 = np.multiply(line_1,rm)
    line_2_200x200 = np.multiply(line_2,rm)
    line_3_200x200 = np.multiply(line_3,rm)
    line_4_200x200 = np.multiply(line_4,rm)
    
    square_1_200x200 = [np.multiply(square_1,rm),np.multiply(square_2,rm),np.multiply(square_3,rm),np.multiply(square_4,rm)]
    square_2_200x200 = [np.multiply(square_5,rm),np.multiply(square_6,rm),np.multiply(square_7,rm),np.multiply(square_8,rm)]
    
    triangule_1_200x200 = [np.multiply(triangule_1,rm),np.multiply(triangule_2,rm),np.multiply(triangule_3,rm)]
    triangule_2_200x200 = [np.multiply(triangule_4,rm),np.multiply(triangule_5,rm),np.multiply(triangule_6,rm)]
    
    hexagon_1_200x200 = [np.multiply(hexagon_1,rm),np.multiply(hexagon_2,rm),np.multiply(hexagon_3,rm),np.multiply(hexagon_4,rm),np.multiply(hexagon_5,rm),np.multiply(hexagon_6,rm)]
    hexagon_2_200x200 = [np.multiply(hexagon_7,rm),np.multiply(hexagon_8,rm),np.multiply(hexagon_9,rm),np.multiply(hexagon_10,rm),np.multiply(hexagon_11,rm),np.multiply(hexagon_12,rm)]
    
    
#-----------------Matrix 50x50------------------------------------------------------------------------------------------------
    
    matrix_1.draw_line(line_1_50x50)
    matrix_1.draw_line(line_2_50x50)
    matrix_1.draw_line(line_3_50x50)
    matrix_1.draw_line(line_4_50x50)
    matrix_1.plot()
    
    matrix_1.draw_convex_polygon(triangule_1_50x50)
    matrix_1.plot()
    
    matrix_1.draw_convex_polygon(triangule_2_50x50)
    matrix_1.plot()
    
    matrix_1.draw_convex_polygon(square_1_50x50)
    matrix_1.plot()
    
    matrix_1.draw_convex_polygon(square_2_50x50)
    matrix_1.plot()
    
    matrix_1.draw_convex_polygon(hexagon_1_50x50)
    matrix_1.plot()
    
    matrix_1.draw_convex_polygon(hexagon_2_50x50)
    matrix_1.plot()
    
#-----------------Matrix 100x100------------------------------------------------------------------------------------------------
    
    matrix_2.draw_line(line_1_100x100)
    matrix_2.draw_line(line_2_100x100)
    matrix_2.draw_line(line_3_100x100)
    matrix_2.draw_line(line_4_100x100)
    matrix_2.plot()
    
    matrix_2.draw_convex_polygon(triangule_1_100x100)
    matrix_2.plot()
    
    matrix_2.draw_convex_polygon(triangule_2_100x100)
    matrix_2.plot()
    
    matrix_2.draw_convex_polygon(square_1_100x100)
    matrix_2.plot()
    
    matrix_2.draw_convex_polygon(square_2_100x100)
    matrix_2.plot()
    
    matrix_2.draw_convex_polygon(hexagon_1_100x100)
    matrix_2.plot()
    
    matrix_2.draw_convex_polygon(hexagon_2_100x100)
    matrix_2.plot()
    
#-----------------Matrix 200x200------------------------------------------------------------------------------------------------
    
    matrix_3.draw_line(line_1_200x200)
    matrix_3.draw_line(line_2_200x200)
    matrix_3.draw_line(line_3_200x200)
    matrix_3.draw_line(line_4_200x200)
    matrix_3.plot()
    
    matrix_3.draw_convex_polygon(triangule_1_200x200)
    matrix_3.plot()
    
    matrix_3.draw_convex_polygon(triangule_2_200x200)
    matrix_3.plot()
    
    matrix_3.draw_convex_polygon(square_1_200x200)
    matrix_3.plot()
    
    matrix_3.draw_convex_polygon(square_2_200x200)
    matrix_3.plot()
    
    matrix_3.draw_convex_polygon(hexagon_1_200x200)
    matrix_3.plot()
    
    matrix_3.draw_convex_polygon(hexagon_2_200x200)
    matrix_3.plot()
    
    
    
    