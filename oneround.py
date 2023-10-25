import copy
import random
import tiles as tls
import judge as jdg

def draw_player(info_list):
    yama = info_list[0]
    tehai_a = info_list[1]
    kawa = info_list[2]
    turn = info_list[3]

    t = turn[0]
    tehai = tehai_a[t]
    tehai[0].append(yama.pop(0))
    


def draw_cpu(info_list):
    yama = info_list[0]
    tehai_a = info_list[1]
    kawa = info_list[2]
    turn = info_list[3]
    p_kaze = info_list[4]

    tehai = tehai_a[turn[0]]
    tehai[0].append(yama.pop(0))
    
    #tls.print_tehai(tehai, turn)
    
    i = random.randint(0,len(tehai[0]) - 1)
    #print(tls.hai_name(tehai[0][i]))

    if (p_kaze[0]+1)%4 == turn[0]:#playerの下家
        hai = tehai[0][i] + 0.3
    if (p_kaze[0]+2)%4 == turn[0]:#playerの対面
        hai = tehai[0][i] + 0.2
    if (p_kaze[0]+3)%4 == turn[0]:#playerの上家
        hai = tehai[0][i] + 0.4
    kawa[turn[0]].append(hai)

    #jdg.naki(yama, tehai_a, tehai[0][i], turn, kawa, p_kaze)
    tehai[0].pop(i)
    #jdg.ron(tehai_a, i, turn)