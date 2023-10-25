import judge
import random




def tumo(tehai):
    n = len(tehai[0])
    tehai_m = tehai[0][:n-1]
    hai = tehai[0][n-1]
    print(hai)
    print(tehai_m)
    print(judge.mati([tehai_m]))
    if hai in judge.mati([tehai_m]):
        return True
    else:
        return False
    
#print(tumo(li))

def make_yama():#萬子36,筒子36,索子36,風牌16,役牌12
    yama = [j for i in range(4) for j in range(1, 35)]
    for i in range(10):
        random.shuffle(yama)
    print(len(yama))
    return yama



li = [1,2,3,4,5,6]
li_2 = [1,2,3]

li_2.append(li.pop(-1))

for i in range(1,4):
    print(li[-i])