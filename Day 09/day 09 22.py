with open('day 09 22 data.txt') as f:
    data =[x.replace('\n','') for x in f.readlines()]


def parse(line):
    moves = {'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}
    direct,steps = line.split(' ')
    return [moves[direct] for _ in range(int(steps))]
    
    
def steps(data):
    steps = [parse(line) for line in data]
    # print(steps)
    return [step for sublist in steps for step in sublist]

def next_list(last_list,n):
    print(n)
    tail = [0,0]
    output_list = []

    for place,head in enumerate(last_list):

        x_diff= head[0]- tail[0]
        y_diff = head[1] - tail[1]
        abs_x = abs(x_diff)
        abs_y = abs(y_diff)

        if abs_x > 1 or abs_y > 1:

            tail = [tail[0] + (0 if x_diff == 0 else x_diff // abs_x),tail[1] + (0 if y_diff == 0 else y_diff // abs_y)]
            output_list.append(tail)
        else:
            output_list.append(tail)

    return output_list


def run_stuff(head,n):
    last_list = head
    outputs = [head]
    for _ in range(1,n):
        output = next_list(last_list,_)
        outputs.append(output)
        last_list = output
    return outputs
    

def solution(n):

    instructions = steps(data)
    head = [0,0]
    head_list = []

    for line in instructions:
        head = [a+b for a,b in zip(head,line)]
        head_list.append(head)
    
    snake = run_stuff(head_list,n)
    
    for n in range(len(snake)):
        # print(snake[n])
        snake[n] = set([str(x) for x in snake[n]])
        sets = [len(part) for part in snake]
        
    print(sets)

solution(10)