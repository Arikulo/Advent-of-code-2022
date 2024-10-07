
boxes = [['Q','W','P','S','Z','R','H','D'],
         ['V','B','R','W','Q','H','F'],
         ['C','V','S','H'],
         ['H','F','G'],
         ['P','G','J','B','Z',],
         ['Q','T','J','H','W','F','L'],
         ['Z','T','W','D','L','V','J','N'],
         ['D','T','Z','C','J','G','H','F'],
         ['W','P','V','M','B','H']]


# boxes = [['Z','N'],['M','C','D'],['P']]

    
data= open('day 05 22 data.txt').readlines()
data = [x.replace('\n','') for x in data]
instructions = []
for line in data:
    instructions.append([thing for thing in line.split() if thing.isdigit()])

def box_moving(amount,start,end,part):

    selected = boxes[start-1][-amount:][::part]
    boxes[start-1] = boxes[start-1][:-amount]
    boxes[end-1]+=selected



def part_1():
    for amount_in,start_in,end_in in instructions:
        box_moving(int(amount_in), int(start_in), int(end_in),-1)
        
    output = ''.join([stack[-1] for stack in boxes if stack])
    print(output)
    
def part_2():

    for amount_in,start_in,end_in in instructions:
        box_moving(int(amount_in), int(start_in), int(end_in),1)
        
    output = ''.join([stack[-1] for stack in boxes if stack])
    print(output)
    
# part_1()
part_2()

