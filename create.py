import copy
import random



def make_yama():#萬子36,筒子36,索子36,風牌16,役牌12
    yama = []
    for i in range(4):
        for j in range(1,35):
            n = float(str(j) + ".0")
            yama.append(n)
    for i in range(10):
        random.shuffle(yama)
    return yama


def make_tehai(yama):
    tehai = []
    
    for _ in range(13):
        tehai.append(yama[0])
        yama.pop(0)
    tehai.sort()
    
    return tehai

def idv_tehai(yama):
    tehai_a = [[0], [0], [0], [0]]
    tehai_player0 = make_tehai(yama)
    tehai_player1 = make_tehai(yama)
    tehai_player2 = make_tehai(yama)
    tehai_player3 = make_tehai(yama)
    tehai_a[0] = [tehai_player0, [0]]
    tehai_a[1] = [tehai_player1, [0]]
    tehai_a[2] = [tehai_player2, [0]]
    tehai_a[3] = [tehai_player3, [0]]

    return tehai_a

#print(make_yama())