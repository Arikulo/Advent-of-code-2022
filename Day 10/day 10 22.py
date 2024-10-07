import numpy as np
with open('day 10 22 data.txt') as f:
    data =[x.replace('\n','') for x in f.readlines()]
    
data =[x.split() for x in data]



def part_1():
    X=1
    cycle=[]
    for command in data:
        cycle.append(X)
        if command[0] == 'addx':
            X+=int(command[1])
            cycle.append(X)
    value = [a*cycle[a-2] for a in range(20,260,40)]
    print(sum(value))
    
 
def part_2():
    X=1
    cycles=[]
    for command in data:
        cycles.append(X)
        if command[0] == 'addx':
            X+=int(command[1])
            cycles.append(X)

    values = np.asarray([cycles[i:i + 40] for i in range(0, len(cycles), 40)])
    crt = np.asarray([[i for i in range(40)] for _ in range(6)])
    
    for line in range(len(crt)):
        print(values[line])
    # print(values)
    

    # positions = []
    for line in range(len(values)):
        values_list,crt_list = values[line],crt[line]
        position = ''.join(list(np.where(abs(values_list-1-crt_list)<=1,'■','-')))
        # position = [values[line].index(a) for a,b in zip(values[line],crt[line]) if abs(a-b) <=2]
        print(position)
        
    # for x in positions:
    #     print(x)
    
    



# part_1()
part_2() 
# print(data)

