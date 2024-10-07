from itertools import groupby
import re
import numpy as np


with open('day 11 22 data.txt') as f:
    data = [x[:-1] for x in f.readlines()]

data = [list(group) for ele, group in groupby(data,key=bool) if ele]
# print(data)
def calc(operation):
    if len(operation) == 2:
        a,b,c=1,0,0
    elif operation[0] == '*':
        a,b,c=0,int(operation[1]),0
    elif operation[0] == '+':
        a,b,c = 0,0,int(operation[1])
        
    return a,b,c

def monkey_stuff():
    monkey_data = []
    for monkeys in data:
        items = [int(x) for x in re.findall(r'\d+',monkeys[1])]
        
        operation = sorted(set((monkeys[2][19:].split())))
        a,b,c = calc(operation)
        
        divisor = int(re.findall(r'\d+',monkeys[3])[0])
        if_true = int(re.findall(r'\d+',monkeys[4])[0])
        if_false = int(re.findall(r'\d+',monkeys[5])[0])
        
        monkey_data.append([items,[a,b,c],divisor,[if_true,if_false]])
    # for monkey in monkey_data:
        # print(f'Items: {monkey[0]}\nQuadatic: {monkey[1]}\nDivisor: {monkey[2]}\nWhere to: {monkey[3]}\n\n\n')
    return monkey_data
    

def part_1():
    monkey_data =monkey_stuff()
    inspections = [0]*len(monkey_data)
    for _ in range(20):
        for place,(items,(a,b,c),divisor,(yes,no)) in enumerate(monkey_data):
            # print('\n',items,sep='\n')
            if c != 0:
                worries = [int(np.floor((x+c)/3)) for x in items]
            else:
                worries = [int(np.floor((a*x**2 + b*x)/3)) for x in items]
            # print(worries)
            inspections[place]+=len(worries)
            removes = []
            for value_place,value in enumerate(worries):
                
                if value % divisor == 0:
                    # print(f'{value} divisible by {divisor}, moving item to monkey {yes}')
                    removes.append(value_place)
                    # print(monkey_data[place][0],value_place)
                    monkey_data[yes][0].append(value)
                elif value % divisor != 0:
                    # print(f'{value} not divisible by {divisor}, moving item to monkey {no}')
                    removes.append(value_place)
                    # print(monkey_data[place][0],value_place)
                    monkey_data[no][0].append(value)
            # print(removes)
            for x in sorted(removes,reverse=True):
                # print(monkey_data[place][0],x)
                monkey_data[place][0].pop(x)
                    
        # print('\n\n')
        # for monkey in monkey_data:
        #     print(monkey[0],'\n')
    i_s = sorted(inspections,reverse=True)
    print(i_s[0]*i_s[1])
        
def part_2():
    monkey_data =monkey_stuff()
    inspections = [0]*len(monkey_data)
    lcm = np.prod([monkey_data[n][2] for n in range(len(monkey_data))])
    # print(lcm)
    for _ in range(10000):
        print(_)
        for place,(items,(a,b,c),divisor,(yes,no)) in enumerate(monkey_data):
            # print('\n',items,sep='\n')
            if c != 0:
                worries = [int(np.floor((x+c)%lcm)) for x in items]
            else:
                worries = [int(np.floor(a*x**2 + b*x)%lcm) for x in items]
            # print(worries)
            inspections[place]+=len(worries)
            removes = []
            for value_place,value in enumerate(worries):
                
                if value % divisor == 0:
                    # print(f'{value} divisible by {divisor}, moving item to monkey {yes}')
                    removes.append(value_place)
                    # print(monkey_data[place][0],value_place)
                    monkey_data[yes][0].append(value)
                elif value % divisor != 0:
                    # print(f'{value} not divisible by {divisor}, moving item to monkey {no}')
                    removes.append(value_place)
                    # print(monkey_data[place][0],value_place)
                    monkey_data[no][0].append(value)
            # print(removes)
            for x in sorted(removes,reverse=True):
                # print(monkey_data[place][0],x)
                monkey_data[place][0].pop(x)
                    
        # print('\n\n')
        # for monkey in monkey_data:
        #     print(monkey[0],'\n')
    i_s = sorted(inspections,reverse=True)
    print(i_s[0]*i_s[1])   
    
# part_1()
part_2()