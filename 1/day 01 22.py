#day 1 - 2022

from itertools import groupby

data = open('day 01 22 data.txt').readlines()
data = [thing[:-1] for thing in data]

data_fixed = [list(sub) for ele, sub in groupby(data, key = bool) if ele]
amounts = []

for elf in data_fixed:
    amounts.append(sum([int(x) for x in elf]))
    
print(max(amounts))
print(sum(sorted(amounts,reverse = True)[0:3]))
