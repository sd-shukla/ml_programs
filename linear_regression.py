# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 09:44:10 2019

@author: sudhanshu shukla
"""


import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.metrics import mean_squared_error

def ssd(A,B):
    squares = (A[:,:,:3] - B[:,:,:3]) ** 2
    return numpy.sum(squares)
                         
def estimate_coef(x, y): 
    
    n = np.size(x) 
  
    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 
  
    
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y * x) - n *m_y *m_x # SS_xy is the sum of cross-deviations of y and x
    SS_xx = np.sum(x * x) - n * m_x *m_x # SS_xx is the sum of squared deviations of x
  
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1 * m_x 
  
    return(b_0, b_1) 
  
def plot_regression_line(x, y, b): 
    
    plt.scatter(x, y, color = "m", marker = "o", s = 30) 
    y_pred = b[0] + b[1]*x #The equation of regression line is represented as:
    plt.plot(x, y_pred, color = "g") 
    plt.xlabel('x') 
    plt.ylabel('y') 
    plt.show() 
  
def main(): 
#    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
#    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12]) 
    
    x = np.array([340,1080,640,880,990,510]) 
    y = np.array([500,1700,1100,800,1400,500])
  
    # estimating coefficients 
    b = estimate_coef(x, y) 
    print("Estimated coefficients:\nb_0 = {}  \n b_1 = {}".format(b[0], b[1])) 
    mse = mean_squared_error(x,y)
    print(b)
    y1_list=[]
    sse=0.0
    for i in range(len(x)):
        y1=b[0]+b[1]*x[i]
        y1_list.append(y1)
    for i in range(len(y)):
        sse+=(y[i]-y1_list[i])**2
    
        
    print("Sum of Squared Total Error (SST) is {}".format(mse))
    print("Sum of Squared Error (SSE) is {}".format(sse))
    print("Sum of Squared Regression Error (SSR) is {}".format(mse-sse))
    
    # plotting regression line 
    plot_regression_line(x, y, b) 
  

if __name__ == "__main__": 
	main() 
