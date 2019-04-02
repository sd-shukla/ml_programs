# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 08:47:30 2019

@author: sudhanshu shukla
"""
import math

dataset={
        'Age':[25,35,45,20,35,52,23,40,60,48,33],
        'Loan':[40000,60000,80000,20000,120000,18000,95000,62000,100000,220000,150000],
        'Default':['N','N','N','N','N','N','Y','Y','Y','Y','Y'],
        }

columns=list(dataset.keys())

def return_Square(data_point1, data_point2):
    return pow((data_point1 - data_point2), 2)

    

def compute_distance(dataset,test_values):
    distance=[0 for x in dataset[columns[0]]]
    for i in range(len(dataset[columns[0]])):
        distance[i]=0
        distance[i]+=return_Square(dataset[columns[0]][i],test_values[0])
        distance[i]+=return_Square(dataset[columns[1]][i],test_values[1])
        distance[i]=math.sqrt(distance[i])
        distance[i]=float(format(distance[i], '.4f'))
    return distance
    

def compute_rank(dataset,distances):
    distances.sort()
    ranks=[0 for x in dataset[columns[0]]]
    for i in range(len(dataset[columns[0]])):
        ranks[i]=distances.index(dataset['distance'][i])+1
    return ranks
    

    
    
#distances=compute_distance(dataset,[48,142000])    
#dataset['distance']=distances
#
#dataset['rank']=compute_rank(dataset,distances.copy())


def predict(dataset,test_values):
    distances=compute_distance(dataset,test_values)    
    dataset['distance']=distances
    ranks=compute_rank(dataset,distances.copy())
    dataset['rank']=ranks
    
    
    print("Enter the value of K")
    k=int(input())
    i=0
    count_yes=0
    count_no=0
    ranks_copy=ranks.copy()
    ranks_copy.sort()
    while i < k:
        if dataset['Default'][ranks.index(ranks_copy[i])] =='Y':
            count_yes+=1
        else:
            count_no+=1
        i+=1
    if count_yes>count_no:
        print("For {} and {} belongs to class Y".format(test_values[0],test_values[1]))
    else:
        print("For {} and {} belongs to class N".format(test_values[0],test_values[1]))
        


predict(dataset,[30,180000])