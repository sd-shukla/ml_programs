# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 22:03:34 2019

@author: sudhanshu shukla
"""
import numpy as np
import pandas as pd
import pprint
#he pprint module provides a capability to “pretty-print” arbitrary Python data structures in a form which can be used as input to the interpreter.
eps = np.finfo(float).eps 
#‘eps’ here is the smallest representable number. 
#At times we get log(0) or 0 in the denominator, to avoid that we are going to use this.
from numpy import log2 as log
dataset = {'Taste':['Salty','Spicy','Spicy','Spicy','Spicy','Sweet','Salty','Sweet','Spicy','Salty'],
       'Temperature':['Hot','Hot','Hot','Cold','Hot','Cold','Cold','Hot','Cold','Hot'],
       'Texture':['Soft','Soft','Hard','Hard','Hard','Soft','Soft','Soft','Soft','Hard'],
       'Eat':['No','No','Yes','No','Yes','Yes','No','Yes','Yes','Yes']}


#dataset = { 'Hair':['Blonde','Blonde','Brown','Blonde','Red','Brown','Brown','Blonde',],
#           'Height':['Avg','Tall','Short','Short','Avg','Tall','Avg','Short'],
#           'Weight':['Light','Avergae','Avergae','Avergae','Heavy','Heavy','Heavy','Light'],
#           'Location':['No','Yes','Yes','No','No','No','No','Yes'],
#           'Sunburn':['Yes','No','No','Yes','Yes','No','No','No']
#            }

df = pd.DataFrame(dataset,columns=['Hair','Height','Weight','Location','Sunburn'])
df = pd.DataFrame(dataset,columns=['Taste','Temperature','Texture','Eat'])

def find_entropy(df):
    Class = df.keys()[-1]   #To make the code generic, changing target variable class name
    entropy = 0
    values = df[Class].unique()#returns unique elements
    for value in values: #iterating over each value
        fraction = df[Class].value_counts()[value]/len(df[Class]) 
        #df[Class].value_counts() gives a data framme of unique values having total number of that enteries
        """
        df['Eat'].value_counts()
        
        Yes    6
        No     4
       
        """
        #and then applying [value] gives the exact value
        #e.g df['Eat'].value_counts()['No']
        entropy += -fraction*np.log2(fraction) #entropy formula
    return entropy
  
  
def find_entropy_attribute(df,attribute):
    
      Class = df.keys()[-1]   #To make the code generic, changing target variable class name
      target_variables = df[Class].unique()  #This gives all 'Yes' and 'No'
      variables = df[attribute].unique()    #This gives different features in that attribute (like 'Hot','Cold' in Temperature)
      entropy2 = 0
      for variable in variables:
          entropy = 0
          for target_variable in target_variables:
              num = len(df[attribute][df[attribute]==variable][df[Class] ==target_variable])
              """
              df[attribute]==variable] for each entry returns a boolean value if its true or false in regrards to variable
              df[Class] ==target_variable] same here as above.
                
              """
              den = len(df[attribute][df[attribute]==variable])
              fraction = num/(den+eps)
              entropy += -fraction*log(fraction+eps)
          fraction2 = den/len(df)
          entropy2 += -fraction2*entropy
      return abs(entropy2)


def find_winner(df):
    IG = []
    for key in df.keys()[:-1]:
        #df.keys()[:-1] give list of column names except the last column which is our label
#         Entropy_att.append(find_entropy_attribute(df,key))
        IG.append(find_entropy(df)-find_entropy_attribute(df,key))
    return df.keys()[:-1][np.argmax(IG)]
  
  
def get_subtable(df, node,value):
    """
    When we reset the index, the old index is added as a column, and a new sequential index is used:
        We can use the drop parameter to avoid the old index being added as a column:
    """
    return df[df[node] == value].reset_index(drop=True)


def buildTree(df,tree=None): 
    
    #Here we build our decision tree

    #Get attribute with maximum information gain
    node = find_winner(df)
    
    #Get distinct value of that attribute]
    attValue = np.unique(df[node])
    
    #Create an empty dictionary to create tree    
    if tree is None:                    
        tree={}
        tree[node] = {}
    
   #We make loop to construct a tree by calling this function recursively. 
    #In this we check if the subset is pure and stops if it is pure. 

    for value in attValue:
        
        subtable = get_subtable(df,node,value)
        clValue,counts = np.unique(subtable['Eat'],return_counts=True)                        
        
        if len(counts)==1:#Checking purity of subset
            tree[node][value] = clValue[0]                                                    
        else:        
            tree[node][value] = buildTree(subtable) #Calling the function recursively 
                   
    return tree

tree=buildTree(df)

pprint.pprint(tree)