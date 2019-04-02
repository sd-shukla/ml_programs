# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:27:00 2019

@author: sudhanshu shukla
"""
import pandas as pd
import numpy as np

dataset = pd.read_csv('tennis.csv')

columns=dataset.columns.values.tolist()

likelihood={}
label=columns[-1]

class_yes=dataset[label].value_counts()['yes']/len(dataset[label])
class_yes=float(format(class_yes, '.4f'))
class_no=dataset[label].value_counts()['no']/len(dataset[label])
class_no=float(format(class_no, '.4f'))
def sumColumn(m, column):
    total = 0
    for row in range(len(m)):
        total += m[row][column]
    return total

def generate_likelihood(column):
    table=[]
    values=dataset[column].unique()
    for value in values:
#        print(value)
#        output=dataset[label].value_counts()
#        print(output)
        
        count_yes=0
        count_no=0
        for i in range(len(dataset)):
            if (dataset[column][i]==value) and (dataset[label][i]=="yes"):
                count_yes+=1
            elif (dataset[column][i]==value) and (dataset[label][i]=="no"):
                count_no+=1
        table.append([value,count_yes,count_no])
    
    sum_yes=sumColumn(table,1)
    sum_no=sumColumn(table,2)
    for i in table:
        i[1]/=sum_yes
        i[2]/=sum_no
        i[1]=float(format(i[1], '.4f'))
        i[2]=float(format(i[2], '.4f'))
        
    
    
    return table

for column in columns[:-1]:
    val=generate_likelihood(column)
    likelihood[column]=val
    
    
def predict(outlook,temp,humidity,windy):
    values_yes=[]
    values_no=[]
    for column in columns[:-1]:
        
        rows=likelihood[column]
        
        for row in rows:
               
            if row[0]==outlook or row[0]==temp or row[0]==humidity or row[0]==bool(windy):
                
                values_yes.append(row[1])
                values_no.append(row[2])
    likelihoodForYes=float(format(np.prod(values_yes)*class_yes, '.6f'))
    likelihoodForNo=float(format(np.prod(values_no)*class_no, '.6f'))
    
    probability_yes=likelihoodForYes/(likelihoodForNo+likelihoodForYes)
    probability_no=likelihoodForNo/(likelihoodForNo+likelihoodForYes)
    
    print("Proability for yes",probability_yes)
    print("Proability for no",probability_no)
    
predict('rainy','cool','normal','False')    
print("___________________________________________________________")
predict('sunny','hot','high','True')    
print("___________________________________________________________")
predict('rainy','hot','high','True')    
    
    
    
    
    