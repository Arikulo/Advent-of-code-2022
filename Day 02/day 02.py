#day 2
data= open('day 02 22 data.py').readlines()

data=[(data[x][0],data[x][2]) for x in range(len(data))]
# print(data)


states_enemy=['A','B','C']
states_player=['X','Y','Z']

def part_1():
    score = []
    for line in data:
        enemy,player=line[0],line[1]
        enemy = states_enemy.index(enemy)+1
        player = states_player.index(player)+1
        winner = (enemy-player)%3
        # print(enemy,player,winner)
        if winner == 1:
            #draw
            score.append(player)
        elif winner == 0:
            #lose
            score.append(3+player)
        else:
            #win
            score.append(6+player)
    print(sum(score))
        
def part_2():
    score = []
    for line in data:
        enemy,player=line[0],line[1]
        enemy = states_enemy.index(enemy)+1
        player = states_player.index(player)+1
        if player == 1:
            #lose
            output = [3,1,2]
            elf_score = output[enemy-1]
            score.append(elf_score)
            # print(enemy,player,elf_score,sep=',')

        elif player == 2:
            #draw
            elf_score = 3+enemy
            score.append(elf_score)
            # print(enemy,player,elf_score,sep=',')
        else:
            #win
            output = [2,3,1]
            elf_score = 6+output[enemy-1]
            score.append(elf_score)
            # print(enemy,player,elf_score,sep=',')
        # print(enemy,player,score[data.index(line)],sep=',')
    print(sum(score))
    


    
# part_1()
part_2()
