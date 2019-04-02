# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:30:11 2019

@author: sudhanshu shukla
"""
import random 
import math
dataset = {"individual":[1, 2, 3, 4, 5, 6, 7],
           "variable1":[1,1.5,3,5,3.5,4.5,3.5],
           "variable2":[1,2,4,7,5,5,4.5]
        }
columns=list(dataset.keys())

k = 2

initial_centroids = random.sample(dataset[columns[0]],k)
#initial_centroids = [1,4]

def Average(lst): 
    return sum(lst) / len(lst)


def compute_distance(dataset,distance_value):
    values=[]
    for i in range(len(dataset[columns[0]])):
        val=0
        val = ((dataset[columns[1]][i]-distance_value[0])**2 + (dataset[columns[2]][i]-distance_value[1])**2)
        val = math.sqrt(val)
        val = float(format(val, '.3f'))
        values.append(val)
    return values
    
def make_table(dataset,initial_centroids):
    
    columns_of_table = len(initial_centroids)
    table = []
    for i in range(columns_of_table):
        index_value = dataset[columns[0]].index(initial_centroids[i])
        distance_value = [dataset[columns[1]][index_value],dataset[columns[2]][index_value]]
        val=compute_distance(dataset,distance_value)
        table.append(val)
    return table

def make_table_with(dataset,new_centroids):
    print("new Centroids are",new_centroids)
    table = []
    for i in range(2):
        
        distance_value = [new_centroids[i][0],new_centroids[i][1]]
        val=compute_distance(dataset,distance_value)
        table.append(val)
    return table

def compute_new_centroid(clusters_new):
    
    values = []
    val1_avg=0
    val2_avg=0
    for i in range(len(clusters_new)):
        val1=[]
        val2=[]
        for j in range(len(clusters_new[i])):
            val1.append(dataset[columns[1]][clusters_new[i][j]])
            val2.append(dataset[columns[2]][clusters_new[i][j]])
#            val_tuple=[dataset[columns[1]][clusters_new[i][j]],dataset[columns[2]][clusters_new[i][j]]]
           
        val1_avg= float(format(Average(val1), '.3f'))
        val2_avg= float(format(Average(val2), '.3f'))  
        values.append([val1_avg,val2_avg])
    return values
     
    

def cluster(dataset,initial_centroids):
    print("Initial centroids are",initial_centroids)
    clusters_old=[]
    clusters_new = []
    table = make_table(dataset,initial_centroids)
    while True:
        group1=[]
        group2=[]
        for i in range(len(dataset[columns[0]])):
            
            if table[0][i] <= table[1][i]:
                group1.append(i)
                
            else:
                group2.append(i)
        clusters_new.append(group1)
        clusters_new.append(group2)
        print("Cluster old",clusters_old)
        print("Cluster new",clusters_new)
        if clusters_old == clusters_new:
            break
        else:
            clusters_old =clusters_new.copy()
        new_centroids = compute_new_centroid(clusters_new)
        
        table = make_table_with(dataset,new_centroids)
        
        
        clusters_new.clear()
        
        
cluster(dataset,initial_centroids)                
    
    
    
    
    
    
    
    