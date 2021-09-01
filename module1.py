
                                             # Python Program to find numbers divisible 
# by thirteen from a list using anonymous 
# function 

# Take a list of numbers. 
#my_list = [[12, 65],[ 54, 39], [102, 339], [221, 50]] 

## use anonymous function to filter and comparing 
## if divisible or not 
#result = list(filter(lambda x: (x == [12,65]), my_list)) 

## printing the result 
#print(result) 

import math
import random

r = 0

while r!=100:
    r = random.randrange(1, 101 , 1)
    print(r)
    pass

#def distanceUnder(dist, lista, coord):
#    index_coord = []
#    x = list(filter(lambda i: math.hypot((i[0]-coord[0]),(i[1]-coord[1])) < dist , lista))  
#    if(x != [] and (x not in index_coord)):
#        index_coord.append(x)
#    return index_coord
def distanceUnder(dist, lista, coord):
    index_coord = []    
    j=0
    for i in lista:
        if(math.hypot((i[0]-coord[0]),(i[1]-coord[1])) < dist):
            index_coord.append(j)
        j+=1
    return index_coord

offsets = [[[12, 65],[ 54, 39], [102, 339], [221, 50]],[[12, 65],[ 54, 39], [102, 339], [221, 50]]] 
taxi_porto = [[12, 65],[ 54, 39], [102, 339], [221, 50]] 


index_coord = []

for row in offsets:
    for coord in row:
    #    x = list(filter(lambda i: math.sqrt(((coord[0]+i[0])^2)+((coord[1]+i[1])^2)) < 50 , row))  
    #    if(x != [] and (x not in index_coord)):
    #        index_coord.append(x)
    #    if(len(index_coord)==10):
    #        break
    #if(len(index_coord)==10):
    #    break
    #print(index_coord)
        index_coord = distanceUnder(50, row, coord)
print(index_coord)

