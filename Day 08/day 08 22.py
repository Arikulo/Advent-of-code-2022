#day 8
import math

data= open('day 08 22 data.txt').readlines()
data = [x.replace('\n','') for x in data]

for row_count,row in enumerate(data):
    data[row_count] = [int(x) for x in row]


def surroundings(row,column,height):

    above = []
    below = []

    left,right = [x for x in data[column+1][:row+1]],[x for x in data[column+1][row+2:]]

    for n in range(column+1):
        above.append(data[n][row+1])
    for n in range(column+2,len(data)):
        below.append(data[n][row+1])
    
    
    return left,right,above,below


def part_1():
    count=2*(len(data) + len(data[0]) -2)
    middle = [line[1:-1] for line in data[1:-1]]

    for position_y,row in enumerate(middle):
        for position_x,tree in enumerate(row):
            checks = 0
            left,right,above,below=surroundings(position_x,position_y,tree)
            
            if tree > max(left) or tree > max(right):
                checks+=1
                
            if tree > max(above) or tree > max(below):
                checks+=1

            if checks >= 1: 
                count+=1
    print(count)
                
def part_2():
    middle = [line[1:-1] for line in data[1:-1]]
    total = []

    for position_y,row in enumerate(middle):
        for position_x,tree in enumerate(row):
            
            left,right,above,below=surroundings(position_x,position_y,tree)
            sight = []
            left = list(reversed(left))
            above = list(reversed(above))
            
            for line in [left,right,above,below]:
                try:
                    item = next(line.index(x) for x in line if x >= tree)+1
                    sight.append(item)
                except StopIteration:

                    sight.append(len(line))
                    
            total.append(math.prod(sight))

            
    print(max(total))
             

part_1()
part_2()
