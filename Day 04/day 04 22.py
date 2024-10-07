#day 4
import numpy as np
data= open('day 04 22 data.txt').readlines()
data = [x.replace('\n','') for x in data]
# print(data)

def inside(first,second):
    if (int(second[0]) <= int(first[0])) and (int(first[1]) <= int(second[1])):
        return True
        
    elif (int(first[0]) <= int(second[0])) and (int(second[1]) <= int(first[1])):
        return True
    else:
        return False
    
def match(first,second):
    if (int(first[0]) >= int(second[0])) and (int(first[0]) <= int(second[1])):
        return True
    elif (int(first[1]) >= int(second[0])) and (int(first[1]) <= int(second[1])):
        return True
    else:
        return False
    
    
def part_1():
    count = 0
    for line in data:
        pairs = [thing.split('-') for thing in line.split(',')]
        first,second = pairs[0],pairs[1]
        
        if inside(first,second) == True:
            count+=1
    print(count)        
   

def part_2():
    count = 0
    for line in data:
        pairs = [thing.split('-') for thing in line.split(',')]
        first,second = pairs[0],pairs[1]

        if match(first,second) or inside(first,second) == True:
            count+=1

    print(count)  
      
part_1()
part_2()
