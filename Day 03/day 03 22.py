data= open('day 03 22 data.txt').readlines()
data = [x.replace('\n','') for x in data]

def part_1():
    stuff = []
    for line in data:
        line_set = line[:int(len(line)/2)],line[int(len(line)/2):]
        stuff.append(list(set(line_set[0]).intersection(line_set[1]))[0] )

    capitals = [letter for letter in stuff if letter.isupper() == True]
    lowers = [letter for letter in stuff if letter.isupper() == False]

    capitals_priorities = [ord(a)-38 for a in capitals]
    lowers_priorities = [ord(a)-96 for a in lowers]
    print(sum(capitals_priorities) + sum(lowers_priorities))

    
def part_2():
    stuff = []
    chunks = [data[x:x+3] for x in range(0, len(data), 3)]
        
    for group in chunks:
        a,b,c = group[0],group[1],group[2]
        stuff.append(list(set(a).intersection(b).intersection(c))[0])
            
    capitals = [letter for letter in stuff if letter.isupper() == True]
    lowers = [letter for letter in stuff if letter.isupper() == False]

    capitals_priorities = [ord(a)-38 for a in capitals]
    lowers_priorities = [ord(a)-96 for a in lowers]
    print(sum(capitals_priorities) + sum(lowers_priorities))

    
part_1()
part_2()
