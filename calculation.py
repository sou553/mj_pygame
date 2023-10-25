import sys
import copy
import math
import yaku_sub  as sub
import judge as jdg
from decimal import Decimal

def points(p_tehai, Flags, p_kaze, bakaze, yaku_list):
    points = [0]
    tehai = [[], []]  # 手牌の小数点を捨てる
    tehai_t = copy.deepcopy(p_tehai)
    for hai in tehai_t[0]:
        tehai[0].append(int(hai))
    if tehai_t[1] != [0]:
        for hai in tehai_t[1]:
            tehai[1].append(int(hai))

    TurnFlag = Flags[0]
    FirstTurn = Flags[1]
    Reach = Flags[2]
    Menzen = Flags[3]
    Haitei = Flags[4]
    Rinsyan = Flags[5]
    Chankan = Flags[6]
    if "平和" in yaku_list[0]:
        hu = 20
        if Menzen == True and TurnFlag == "Ron": 
            hu += 10
    elif "七対子" in yaku_list[1]:
        hu = 25
    elif len(yaku_list[5]) != 0:
        hu = 0
    else:
        hu = 20 #　副底
        if Menzen == True and TurnFlag == "Ron": 
            hu += 10
        elif TurnFlag == "Tumo":
            hu += 2
        tehai_111_m, tehai_123_m, tehai_111_n, tehai_123_n, atama = sub.points_sub(tehai)
        #print(tehai_111_m, tehai_123_m, tehai_111_n, tehai_123_n, atama)

        for hais in tehai_111_m:
            if (2 <= hais[0] and 8 >= hais[0]) or (11 <= hais[0] and 17 >= hais[0]) or (20 <= hais[0] and 26 >= hais[0]):
                hu += 4
            else:
                hu += 8
        for hais in tehai_111_n:
            if hais[0] == 100:
                hai_1 = float(Decimal(str(hais[1])) - Decimal("100"))
                if (2 <= hai_1 and 8 >= hai_1) or (11 <= hai_1 and 17 >= hai_1) or (20 <= hai_1 and 26 >= hai_1):
                    hu += 16
                else:
                    hu += 32
            elif hais[0] > 100:
                hai_1 = float(Decimal(str(hais[1])) - Decimal("100"))
                if (2 <= hai_1 and 8 >= hai_1) or (11 <= hai_1 and 17 >= hai_1) or (20 <= hai_1 and 26 >= hai_1):
                    hu += 8
                else:
                    hu += 16
            elif (2 <= hais[0] and 8 >= hais[0]) or (11 <= hais[0] and 17 >= hais[0]) or (20 <= hais[0] and 26 >= hais[0]):
                hu += 2
            else:
                hu += 4
        if atama >= 32:
            hu += 2
        elif atama == p_kaze[0] + 28 or atama == bakaze[0] + 28:
            hu += 2
        hai = tehai.pop()
        matihai = jdg.mati(tehai)
        if len(matihai) == 1:
            hu += 2
    hu = result = math.ceil(hu / 10) * 10
    #print(hu)
    han = 0
    for n in range(7): # 1,2,3,5,6,13,ドラ = [dora, ura_dora]
        if len(yaku_list[n]) != 0:
            if n < 3:
                han += len(yaku_list[n]) * (n+1)
            elif n > 2 and n < 5:
                han += len(yaku_list[n]) * (n+2)
            elif n == 5:
                han = len(yaku_list[n]) * 13
                break
            elif n == 7:
                for m in yaku_list[n]:
                    han += m

    if p_kaze == [0] and TurnFlag == "Ron": # 
        if han == 1:
            if hu == 30:
                points = [1500]
            elif hu == 40:
                points = [2000]
            elif hu == 50:
                points = [2400]
            elif hu == 60:
                points = [2900]
            elif hu == 70:
                points = [3400]
            elif hu == 80:
                points = [3900]
            elif hu == 90:
                points = [4400]
            elif hu == 100:
                points = [4800]
            elif hu == 110:
                points = [5300]
        elif han == 2:
            if hu == 25:
                points = [2400]
            elif hu == 30:
                points = [2900]
            elif hu == 40:
                points = [3900]
            elif hu == 50:
                points = [4800]
            elif hu == 60:
                points = [5800]
            elif hu == 70:
                points = [6800]
            elif hu == 80:
                points = [7700]
            elif hu == 90:
                points = [8700]
            elif hu == 100:
                points = [9600]
            elif hu == 110:
                points = [10600]
        elif han == 3:
            if hu == 25:
                points = [4800]
            elif hu == 30:
                points = [5800]
            elif hu == 40:
                points = [7700]
            elif hu == 50:
                points = [9600]
            elif hu == 60:
                points = [11600]
            elif hu >= 70:
                points = [12000]
        elif han == 4:
            if hu == 25:
                points = [9600]
            elif hu == 30:
                points = [11600]
            elif hu >= 40:
                points = [12000]
        elif han == 5:
            points = [12000]
        elif han == 6 or han == 7:
            points = [18000]
        elif han == 8 or han == 9 or han == 10:
            points = [24000]
        elif han == 11 or han == 12:
            points = [36000]
        elif han == 13:
            points = [48000]
        elif han == 26:
            points = [48000*2]
        elif han == 39:
            points = [48000*3] 
    elif p_kaze == [0] and TurnFlag == "Tumo":
        if han == 1:
            if hu == 30:
                points = [500]
            elif hu == 40:
                points = [700]
            elif hu == 50:
                points = [800]
            elif hu == 60:
                points = [1000]
            elif hu == 70:
                points = [1200]
            elif hu == 80:
                points = [1300]
            elif hu == 90:
                points = [1500]
            elif hu == 100:
                points = [1600]
            elif hu == 110:
                points = [1800]
        elif han == 2:
            if hu == 20:
                points = [700]
            elif hu == 30:
                points = [1000]
            elif hu == 40:
                points = [1300]
            elif hu == 50:
                points = [1600]
            elif hu == 60:
                points = [2000]
            elif hu == 70:
                points = [2300]
            elif hu == 80:
                points = [2600]
            elif hu == 90:
                points = [2900]
            elif hu == 100:
                points = [3200]
            elif hu == 110:
                points = [3600]
        elif han == 3:
            if hu == 20:
                points = [1300]
            if hu == 25:
                points = [1600]
            elif hu == 30:
                points = [2000]
            elif hu == 40:
                points = [2600]
            elif hu == 50:
                points = [3200]
            elif hu == 60:
                points = [3900]
            elif hu >= 70:
                points = [4000]
        elif han == 4:
            if hu == 20:
                points = [2600]
            if hu == 25:
                points = [3200]
            elif hu == 30:
                points = [3900]
            elif hu >= 40:
                points = [4000]
        elif han == 5:
            points = [4000]
        elif han == 6 or han == 7:
            points = [6000]
        elif han == 8 or han == 9 or han == 10:
            points = [8000]
        elif han == 11 or han == 12:
            points = [12000]
        elif han == 13:
            points = [16000]
        elif han == 26:
            points = [16000*2]
        elif han == 39:
            points = [16000*3]
    elif p_kaze != [0] and TurnFlag == "Ron": # 
        if han == 1:
            if hu == 30:
                points = [1000]
            elif hu == 40:
                points = [1300]
            elif hu == 50:
                points = [1600]
            elif hu == 60:
                points = [2000]
            elif hu == 70:
                points = [2300]
            elif hu == 80:
                points = [2600]
            elif hu == 90:
                points = [2900]
            elif hu == 100:
                points = [3200]
            elif hu == 110:
                points = [3600]
        elif han == 2:
            if hu == 25:
                points = [1500]
            elif hu == 30:
                points = [2000]
            elif hu == 40:
                points = [2600]
            elif hu == 50:
                points = [3200]
            elif hu == 60:
                points = [3900]
            elif hu == 70:
                points = [4500]
            elif hu == 80:
                points = [5200]
            elif hu == 90:
                points = [5800]
            elif hu == 100:
                points = [6400]
            elif hu == 110:
                points = [7100]
        elif han == 3:
            if hu == 25:
                points = [3200]
            elif hu == 30:
                points = [3900]
            elif hu == 40:
                points = [5200]
            elif hu == 50:
                points = [6400]
            elif hu == 60:
                points = [7700]
            elif hu >= 70:
                points = [8000]
        elif han == 4:
            if hu == 25:
                points = [6400]
            elif hu == 30:
                points = [7700]
            elif hu >= 40:
                points = [8000]
        elif han == 5:
            points = [8000]
        elif han == 6 or han == 7:
            points = [12000]
        elif han == 8 or han == 9 or han == 10:
            points = [16000]
        elif han == 11 or han == 12:
            points = [24000]
        elif han == 13:
            points = [32000]
        elif han == 26:
            points = [32000*2]
        elif han == 39:
            points = [32000*3]
    elif p_kaze != [0] and TurnFlag == "Tumo":
        if han == 1:
            if hu == 30:
                points = [500, 300]
            elif hu == 40:
                points = [700, 400]
            elif hu == 50:
                points = [800, 400]
            elif hu == 60:
                points = [1000, 500]
            elif hu == 70:
                points = [1200, 600]
            elif hu == 80:
                points = [1300, 700]
            elif hu == 90:
                points = [1500, 800]
            elif hu == 100:
                points = [1600, 800]
            elif hu == 110:
                points = [1800, 900]
        elif han == 2:
            if hu == 20:
                points = [700, 400]
            elif hu == 30:
                points = [1000, 500]
            elif hu == 40:
                points = [1300, 700]
            elif hu == 50:
                points = [1600, 800]
            elif hu == 60:
                points = [2000, 1000]
            elif hu == 70:
                points = [2300, 1200]
            elif hu == 80:
                points = [2600, 1300]
            elif hu == 90:
                points = [2900, 1500]
            elif hu == 100:
                points = [3200, 1600]
            elif hu == 110:
                points = [3600, 1800]
        elif han == 3:
            if hu == 20:
                points = [1300, 700]
            if hu == 25:
                points = [1600, 800]
            elif hu == 30:
                points = [2000, 1000]
            elif hu == 40:
                points = [2600, 1300]
            elif hu == 50:
                points = [3200, 1600]
            elif hu == 60:
                points = [3900, 2000]
            elif hu >= 70:
                points = [4000, 2000]
        elif han == 4:
            if hu == 20:
                points = [2600, 1300]
            if hu == 25:
                points = [3200, 1600]
            elif hu == 30:
                points = [3900, 2000]
            elif hu >= 40:
                points = [4000, 2000]
        elif han == 5:
            points = [4000, 2000]
        elif han == 6 or han == 7:
            points = [6000, 3000]
        elif han == 8 or han == 9 or han == 10:
            points = [8000, 4000]
        elif han == 11 or han == 12:
            points = [12000, 6000]
        elif han == 13:
            points = [16000, 8000]
        elif han == 26:
            points = [16000*2, 8000*2]
        elif han == 39:
            points = [16000*3, 8000*3]
    print(han, hu)
    print(points)
    return points


if __name__ == "__main__":
    p_tehai = [[6,7,8,12,8,8,8,12],[130,28,28,28,100,1,1,1]]
    TurnFlag = "Ron"
    FirstTurn = True
    Reach = False
    Menzen = False
    Haitei = False
    Rinsyan = False
    Chankan = False
    Flags = [TurnFlag, FirstTurn, Reach, Menzen, Haitei, Rinsyan, Chankan]
    dora = []
    ura_dora = []
    p_kaze = [0]
    bakaze = [0]
    yaku_list = [[],[],[],[],[],[]]
    points(p_tehai, Flags, p_kaze, yaku_list)