import copy
from decimal import Decimal

def pinfu_sub(tehai_m):
    tehai_d = copy.deepcopy(tehai_m)
    tehai_d.sort()
    for _ in range(4):
        if tehai_del_pinfu(tehai_d) != 0:
            tehai_d = tehai_del_pinfu(tehai_d)[0]
        else:
            return False
    if tehai_d[0] == tehai_d[1]:
        return tehai_d[0]
    else:
        tehai_d = copy.deepcopy(tehai_m)
        tehai_d.sort(reverse=True)
        for _ in range(4):
            if tehai_del_re_pinfu(tehai_d) != 0:
                tehai_d = tehai_del_re_pinfu(tehai_d)[0]
            else:
                return False
        if tehai_d[0] == tehai_d[1]:
            return tehai_d[0]
    return False


def pinfu_re_sub(tehai_m):
    tehai_d = copy.deepcopy(tehai_m)
    tehai_d.sort(reverse=True)
    for _ in range(4):
        if tehai_del_re_pinfu(tehai_d) != 0:
            tehai_d = tehai_del_re_pinfu(tehai_d)[0]
        else:
            return False
    if tehai_d[0] == tehai_d[1]:
        return tehai_d[0]
    else:
        tehai_d = copy.deepcopy(tehai_m)
        tehai_d.sort()
        for _ in range(4):
            if tehai_del_pinfu(tehai_d) != 0:
                tehai_d = tehai_del_pinfu(tehai_d)[0]
            else:
                return False
        if tehai_d[0] == tehai_d[1]:
            return tehai_d[0]
    return False


def chitoi_sub(tehai_m):
    tehai_m = copy.deepcopy(tehai_m)
    tehai_m.sort()
    while len(tehai_m) > 0:
        if tehai_m[0] == tehai_m[1]:
            for _ in range(2):
                tehai_m.pop(0)
        else:
            return False
    return True
    

def ipeko_sub(tehai_m):
    tehai_111 = []
    tehai_123 = []
    tehai_d = copy.deepcopy(tehai_m)
    tehai_d.sort()
    Yaku = False
    for i in range(14):
        for _ in range(4):
            if tehai_del(tehai_d, i) != 0:
                if (tehai_del(tehai_d, i)[1][0] == tehai_del(tehai_d, i)[1][1] and tehai_del(tehai_d, i)[1][1] == tehai_del(tehai_d, i)[1][2]):
                    tehai_111.append(tehai_del(tehai_d, i)[1])
                else:
                    tehai_123.append(tehai_del(tehai_d, i)[1])
                tehai_d = tehai_del(tehai_d, i)[0]
                i = 0
            else:
                break
        if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
            for hais in tehai_123:
                if tehai_123.count(hais) == 2: # 三暗刻 > 一盃口
                    return True
        else:
            tehai_111 = []
            tehai_123 = []
            tehai_d = copy.deepcopy(tehai_m)
            tehai_d.sort()
    tehai_111 = []
    tehai_123 = []
    tehai_d = copy.deepcopy(tehai_m)
    tehai_d.sort(reverse=True)
    Yaku = False
    for i in range(14):
        for _ in range(4):
            if tehai_del_re(tehai_d, i) != 0:
                if (tehai_del_re(tehai_d, i)[1][0] == tehai_del_re(tehai_d, i)[1][1] and tehai_del_re(tehai_d, i)[1][1] == tehai_del_re(tehai_d, i)[1][2]):
                    tehai_111.append(tehai_del_re(tehai_d, i)[1])
                else:
                    tehai_123.append(tehai_del_re(tehai_d, i)[1])
                tehai_d = tehai_del_re(tehai_d, i)[0]
                i = 0
            else:
                break
        if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
            for hais in tehai_123:
                if tehai_123.count(hais) == 2: 
                    return True
        else:
            tehai_111 = []
            tehai_123 = []
            tehai_d = copy.deepcopy(tehai_m)
            tehai_d.sort(reverse=True)
    return False


def ryanpeko_sub(tehai):
    tehai_m = copy.deepcopy(tehai[0])
    if pinfu_sub(tehai_m) != False:
        if chitoi_sub(tehai_m):
            return True
    return False

def sansyoku_123_sub(tehai):
    tehai_m = copy.deepcopy(tehai[0])
    tehai_n = copy.deepcopy(tehai[1])
    if len(tehai_m) == 14:
        tehai_111 = []
        tehai_123 = []
        tehai_d = copy.deepcopy(tehai_m)
        tehai_d.sort()
        for i in range(14):
            for _ in range(4):
                if tehai_del(tehai_d, i) != 0:
                    if (tehai_del(tehai_d, i)[1][0] == tehai_del(tehai_d, i)[1][1] and tehai_del(tehai_d, i)[1][1] == tehai_del(tehai_d, i)[1][2]):
                        tehai_111.append(tehai_del(tehai_d, i)[1])
                    else:
                        tehai_123.append(tehai_del(tehai_d, i)[1])
                    tehai_d = tehai_del(tehai_d, i)[0]
                    i = 0
                else:
                    break
            if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
                tehai_123.sort()
                if len(tehai_123) >= 3:
                    hais_1 = [tehai_123[0][0]+9, tehai_123[0][1]+9, tehai_123[0][2]+9]
                    hais_2 = [tehai_123[0][0]+18, tehai_123[0][1]+18, tehai_123[0][2]+18]
                    if (hais_1 in tehai_123) and (hais_2 in tehai_123):
                        return True
                    hais_1 = [tehai_123[1][0]+9, tehai_123[1][1]+9, tehai_123[1][2]+9]
                    hais_2 = [tehai_123[1][0]+18, tehai_123[1][1]+18, tehai_123[1][2]+18]
                    if (hais_1 in tehai_123) and (hais_2 in tehai_123):
                        return True
            else:
                tehai_111 = []
                tehai_123 = []
                tehai_d = copy.deepcopy(tehai_m)
                tehai_d.sort()
        
        tehai_111 = []
        tehai_123 = []
        tehai_d = copy.deepcopy(tehai_m)
        tehai_d.sort(reverse=True)
        for i in range(14):
            for _ in range(4):
                if tehai_del_re(tehai_d, i) != 0:
                    if (tehai_del_re(tehai_d, i)[1][0] == tehai_del_re(tehai_d, i)[1][1] and tehai_del_re(tehai_d, i)[1][1] == tehai_del_re(tehai_d, i)[1][2]):
                        tehai_111.append(tehai_del_re(tehai_d, i)[1])
                    else:
                        tehai_123.append(tehai_del_re(tehai_d, i)[1])
                    tehai_d = tehai_del_re(tehai_d, i)[0]
                    i = 0
                else:
                    break
            if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
                tehai_123.sort()
                if len(tehai_123) >= 3:
                    hais_1 = [tehai_123[0][0]+9, tehai_123[0][1]+9, tehai_123[0][2]+9]
                    hais_2 = [tehai_123[0][0]+18, tehai_123[0][1]+18, tehai_123[0][2]+18]
                    if (hais_1 in tehai_123) and (hais_2 in tehai_123):
                        return True
                    hais_1 = [tehai_123[1][0]+9, tehai_123[1][1]+9, tehai_123[1][2]+9]
                    hais_2 = [tehai_123[1][0]+18, tehai_123[1][1]+18, tehai_123[1][2]+18]
                    if (hais_1 in tehai_123) and (hais_2 in tehai_123):
                        return True
            else:
                tehai_111 = []
                tehai_123 = []
                tehai_d = copy.deepcopy(tehai_m)
                tehai_d.sort(reverse=True)
    else:
        tehai_111 = []
        tehai_123 = []
        tehai_d = copy.deepcopy(tehai_m)
        tehai_d.sort()
        for i in range(len(tehai_m)):
            for _ in range(int(len(tehai_m)/3)):
                if tehai_del(tehai_d, i) != 0:
                    if (tehai_del(tehai_d, i)[1][0] == tehai_del(tehai_d, i)[1][1] and tehai_del(tehai_d, i)[1][1] == tehai_del(tehai_d, i)[1][2]):
                        tehai_111.append(tehai_del(tehai_d, i)[1])
                    else:
                        tehai_123.append(tehai_del(tehai_d, i)[1])
                    tehai_d = tehai_del(tehai_d, i)[0]
                    i = 0
                else:
                    break
            if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
                break
            else:
                tehai_111 = []
                tehai_123 = []
                tehai_d = copy.deepcopy(tehai_m)
                tehai_d.sort()
        while len(tehai_n) > 0 and tehai_n != [0]:
            if tehai_n[0] >= 100:
                hai = float(Decimal(str(tehai_n[1])) - Decimal("100"))
                tehai_111.append([hai,hai,hai])
                for _ in range(4):
                    tehai_n.pop(0)
            else:
                if tehai_n[0] == tehai_n[1] and tehai_n[1] == tehai_n[2]:
                    tehai_111.append([tehai_n[0],tehai_n[0],tehai_n[0]])
                    for _ in range(3):
                        tehai_n.pop(0)
                elif tehai_n[0]+1 == tehai_n[1] and tehai_n[1]+1 == tehai_n[2]:
                    tehai_123.append([tehai_n[0],tehai_n[1],tehai_n[2]])
                    for _ in range(3):
                        tehai_n.pop(0)
        if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
            tehai_123.sort()
            if len(tehai_123) >= 3:
                hais_1 = [tehai_123[0][0]+9, tehai_123[0][1]+9, tehai_123[0][2]+9]
                hais_2 = [tehai_123[0][0]+18, tehai_123[0][1]+18, tehai_123[0][2]+18]
                if (hais_1 in tehai_123) and (hais_2 in tehai_123):
                    return True
                hais_1 = [tehai_123[1][0]+9, tehai_123[1][1]+9, tehai_123[1][2]+9]
                hais_2 = [tehai_123[1][0]+18, tehai_123[1][1]+18, tehai_123[1][2]+18]
                if (hais_1 in tehai_123) and (hais_2 in tehai_123):
                    return True
        tehai_111 = []
        tehai_123 = []
        tehai_d = copy.deepcopy(tehai_m)
        tehai_d.sort(reverse=True)
        for i in range(len(tehai_m)):
            for _ in range(int(len(tehai_m)/3)):
                if tehai_del_re(tehai_d, i) != 0:
                    if (tehai_del_re(tehai_d, i)[1][0] == tehai_del_re(tehai_d, i)[1][1] and tehai_del_re(tehai_d, i)[1][1] == tehai_del_re(tehai_d, i)[1][2]):
                        tehai_111.append(tehai_del_re(tehai_d, i)[1])
                    else:
                        tehai_123.append(tehai_del_re(tehai_d, i)[1])
                    tehai_d = tehai_del_re(tehai_d, i)[0]
                    i = 0
                else:
                    break
            if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
                break
            else:
                tehai_111 = []
                tehai_123 = []
                tehai_d = copy.deepcopy(tehai_m)
                tehai_d.sort(reverse=True)
        while len(tehai_n) > 0 and tehai_n != [0]:
            if tehai_n[0] >= 100:
                hai = float(Decimal(str(tehai_n[1])) - Decimal("100"))
                tehai_111.append([hai,hai,hai])
                for _ in range(4):
                    tehai_n.pop(0)
            else:
                if tehai_n[0] == tehai_n[1] and tehai_n[1] == tehai_n[2]:
                    tehai_111.append([tehai_n[0],tehai_n[1],tehai_n[2]])
                    for _ in range(3):
                        tehai_n.pop(0)
                elif tehai_n[0]+1 == tehai_n[1] and tehai_n[1]+1 == tehai_n[2]:
                    tehai_123.append([tehai_n[0],tehai_n[1],tehai_n[2]])
                    for _ in range(3):
                        tehai_n.pop(0)
        if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
            tehai_123.sort()
            if len(tehai_123) >= 3:
                hais_1 = [tehai_123[0][0]+9, tehai_123[0][1]+9, tehai_123[0][2]+9]
                hais_2 = [tehai_123[0][0]+18, tehai_123[0][1]+18, tehai_123[0][2]+18]
                if (hais_1 in tehai_123) and (hais_2 in tehai_123):
                    return True
                hais_1 = [tehai_123[1][0]+9, tehai_123[1][1]+9, tehai_123[1][2]+9]
                hais_2 = [tehai_123[1][0]+18, tehai_123[1][1]+18, tehai_123[1][2]+18]
                if (hais_1 in tehai_123) and (hais_2 in tehai_123):
                    return True
    return False


def sansyoku_111_sub(tehai):
    tehai_m = copy.deepcopy(tehai[0])
    tehai_n = copy.deepcopy(tehai[1])
    if len(tehai_m) == 14:
        tehai_111 = []
        tehai_123 = []
        tehai_d = copy.deepcopy(tehai_m)
        tehai_d.sort()
        for i in range(14):
            for _ in range(4):
                if tehai_del(tehai_d, i) != 0:
                    if (tehai_del(tehai_d, i)[1][0] == tehai_del(tehai_d, i)[1][1] and tehai_del(tehai_d, i)[1][1] == tehai_del(tehai_d, i)[1][2]):
                        tehai_111.append(tehai_del(tehai_d, i)[1])
                    else:
                        tehai_123.append(tehai_del(tehai_d, i)[1])
                    tehai_d = tehai_del(tehai_d, i)[0]
                    i = 0
                else:
                    break
            if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
                tehai_111.sort()
                if len(tehai_111) >= 3:
                    hais_1 = [tehai_111[0][0]+9, tehai_111[0][1]+9, tehai_111[0][2]+9]
                    hais_2 = [tehai_111[0][0]+18, tehai_111[0][1]+18, tehai_111[0][2]+18]
                    if (hais_1 in tehai_111) and (hais_2 in tehai_111):
                        return True
                    hais_1 = [tehai_111[0][0]+9, tehai_111[0][1]+9, tehai_111[0][2]+9]
                    hais_2 = [tehai_111[0][0]+18, tehai_111[0][1]+18, tehai_111[0][2]+18]
                    if (hais_1 in tehai_111) and (hais_2 in tehai_111):
                        return True
            else:
                tehai_111 = []
                tehai_123 = []
                tehai_d = copy.deepcopy(tehai_m)
                tehai_d.sort()
        
        tehai_111 = []
        tehai_123 = []
        tehai_d = copy.deepcopy(tehai_m)
        tehai_d.sort(reverse=True)
        for i in range(14):
            for _ in range(4):
                if tehai_del_re(tehai_d, i) != 0:
                    if (tehai_del_re(tehai_d, i)[1][0] == tehai_del_re(tehai_d, i)[1][1] and tehai_del_re(tehai_d, i)[1][1] == tehai_del_re(tehai_d, i)[1][2]):
                        tehai_111.append(tehai_del_re(tehai_d, i)[1])
                    else:
                        tehai_123.append(tehai_del_re(tehai_d, i)[1])
                    tehai_d = tehai_del_re(tehai_d, i)[0]
                    i = 0
                else:
                    break
            if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
                tehai_111.sort()
                if len(tehai_111) >= 3:
                    hais_1 = [tehai_111[0][0]+9, tehai_111[0][1]+9, tehai_111[0][2]+9]
                    hais_2 = [tehai_111[0][0]+18, tehai_111[0][1]+18, tehai_111[0][2]+18]
                    if (hais_1 in tehai_111) and (hais_2 in tehai_111):
                        return True
                    hais_1 = [tehai_111[0][0]+9, tehai_111[0][1]+9, tehai_111[0][2]+9]
                    hais_2 = [tehai_111[0][0]+18, tehai_111[0][1]+18, tehai_111[0][2]+18]
                    if (hais_1 in tehai_111) and (hais_2 in tehai_111):
                        return True
            else:
                tehai_111 = []
                tehai_123 = []
                tehai_d = copy.deepcopy(tehai_m)
                tehai_d.sort(reverse=True)
    else:
        tehai_111 = []
        tehai_123 = []
        tehai_d = copy.deepcopy(tehai_m)
        tehai_d.sort()
        for i in range(len(tehai_m)):
            for _ in range(int(len(tehai_m)/3)):
                if tehai_del(tehai_d, i) != 0:
                    if (tehai_del(tehai_d, i)[1][0] == tehai_del(tehai_d, i)[1][1] and tehai_del(tehai_d, i)[1][1] == tehai_del(tehai_d, i)[1][2]):
                        tehai_111.append(tehai_del(tehai_d, i)[1])
                    else:
                        tehai_123.append(tehai_del(tehai_d, i)[1])
                    tehai_d = tehai_del(tehai_d, i)[0]
                    i = 0
                else:
                    break
            if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
                break
            else:
                tehai_111 = []
                tehai_123 = []
                tehai_d = copy.deepcopy(tehai_m)
                tehai_d.sort()
        while len(tehai_n) > 0 and tehai_n != [0]:
            if tehai_n[0] >= 100:
                hai = float(Decimal(str(tehai_n[1])) - Decimal("100"))
                tehai_111.append([hai,hai,hai])
                for _ in range(4):
                    tehai_n.pop(0)
            else:
                if tehai_n[0] == tehai_n[1] and tehai_n[1] == tehai_n[2]:
                    tehai_111.append([tehai_n[0],tehai_n[1],tehai_n[2]])
                    for _ in range(3):
                        tehai_n.pop(0)
                elif tehai_n[0]+1 == tehai_n[1] and tehai_n[1]+1 == tehai_n[2]:
                    tehai_123.append([tehai_n[0],tehai_n[1],tehai_n[2]])
                    for _ in range(3):
                        tehai_n.pop(0)
        if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
            tehai_111.sort()
            if len(tehai_111) >= 3:
                hais_1 = [tehai_111[0][0]+9, tehai_111[0][1]+9, tehai_111[0][2]+9]
                hais_2 = [tehai_111[0][0]+18, tehai_111[0][1]+18, tehai_111[0][2]+18]
                if (hais_1 in tehai_111) and (hais_2 in tehai_111):
                    return True
                hais_1 = [tehai_111[0][0]+9, tehai_111[0][1]+9, tehai_111[0][2]+9]
                hais_2 = [tehai_111[0][0]+18, tehai_111[0][1]+18, tehai_111[0][2]+18]
                if (hais_1 in tehai_111) and (hais_2 in tehai_111):
                    return True
        tehai_111 = []
        tehai_123 = []
        tehai_d = copy.deepcopy(tehai_m)
        tehai_d.sort(reverse=True)
        for i in range(len(tehai_m)):
            for _ in range(int(len(tehai_m)/3)):
                if tehai_del_re(tehai_d, i) != 0:
                    if (tehai_del_re(tehai_d, i)[1][0] == tehai_del_re(tehai_d, i)[1][1] and tehai_del_re(tehai_d, i)[1][1] == tehai_del_re(tehai_d, i)[1][2]):
                        tehai_111.append(tehai_del_re(tehai_d, i)[1])
                    else:
                        tehai_123.append(tehai_del_re(tehai_d, i)[1])
                    tehai_d = tehai_del_re(tehai_d, i)[0]
                    i = 0
                else:
                    break
            if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
                break
            else:
                tehai_111 = []
                tehai_123 = []
                tehai_d = copy.deepcopy(tehai_m)
                tehai_d.sort(reverse=True)
        while len(tehai_n) > 0 and tehai_n != [0]:
            if tehai_n[0] >= 100:
                hai = float(Decimal(str(tehai_n[1])) - Decimal("100"))
                tehai_111.append([hai,hai,hai])
                for _ in range(4):
                    tehai_n.pop(0)
            else:
                if tehai_n[0] == tehai_n[1] and tehai_n[1] == tehai_n[2]:
                    tehai_111.append([tehai_n[0],tehai_n[1],tehai_n[2]])
                    for _ in range(3):
                        tehai_n.pop(0)
                elif tehai_n[0]+1 == tehai_n[1] and tehai_n[1]+1 == tehai_n[2]:
                    tehai_123.append([tehai_n[0],tehai_n[1],tehai_n[2]])
                    for _ in range(3):
                        tehai_n.pop(0)
        if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
            tehai_111.sort()
            if len(tehai_111) >= 3:
                hais_1 = [tehai_111[0][0]+9, tehai_111[0][1]+9, tehai_111[0][2]+9]
                hais_2 = [tehai_111[0][0]+18, tehai_111[0][1]+18, tehai_111[0][2]+18]
                if (hais_1 in tehai_111) and (hais_2 in tehai_111):
                    return True
                hais_1 = [tehai_111[0][0]+9, tehai_111[0][1]+9, tehai_111[0][2]+9]
                hais_2 = [tehai_111[0][0]+18, tehai_111[0][1]+18, tehai_111[0][2]+18]
                if (hais_1 in tehai_111) and (hais_2 in tehai_111):
                    return True
    return False


def sanankou_sub(tehai, Menzen):
    tehai_m = copy.deepcopy(tehai[0])
    tehai_n = copy.deepcopy(tehai[1])
    if len(tehai_m) == 14:
        tehai_111 = []
        tehai_123 = []
        tehai_d = copy.deepcopy(tehai_m)
        tehai_d.sort()
        for i in range(14):
            for _ in range(4):
                if tehai_del(tehai_d, i) != 0:
                    if (tehai_del(tehai_d, i)[1][0] == tehai_del(tehai_d, i)[1][1] and tehai_del(tehai_d, i)[1][1] == tehai_del(tehai_d, i)[1][2]):
                        tehai_111.append(tehai_del(tehai_d, i)[1])
                    else:
                        tehai_123.append(tehai_del(tehai_d, i)[1])
                    tehai_d = tehai_del(tehai_d, i)[0]
                    i = 0
                else:
                    break
            if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
                tehai_111.sort()
                if len(tehai_111) >= 3:
                    return True
            else:
                tehai_111 = []
                tehai_123 = []
                tehai_d = copy.deepcopy(tehai_m)
                tehai_d.sort()
        tehai_111 = []
        tehai_123 = []
        tehai_d = copy.deepcopy(tehai_m)
        tehai_d.sort(reverse=True)
        for i in range(14):
            for _ in range(4):
                if tehai_del_re(tehai_d, i) != 0:
                    if (tehai_del_re(tehai_d, i)[1][0] == tehai_del_re(tehai_d, i)[1][1] and tehai_del_re(tehai_d, i)[1][1] == tehai_del_re(tehai_d, i)[1][2]):
                        tehai_111.append(tehai_del_re(tehai_d, i)[1])
                    else:
                        tehai_123.append(tehai_del_re(tehai_d, i)[1])
                    tehai_d = tehai_del_re(tehai_d, i)[0]
                    i = 0
                else:
                    break
            if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
                tehai_111.sort()
                if len(tehai_111) >= 3:
                    return True
            else:
                tehai_111 = []
                tehai_123 = []
                tehai_d = copy.deepcopy(tehai_m)
                tehai_d.sort(reverse=True)
    elif Menzen:
        kan = len(tehai_m) + len(tehai_n) - 14
        tehai_111 = []
        tehai_123 = []
        tehai_d = copy.deepcopy(tehai_m)
        tehai_d.sort()
        for i in range(len(tehai_m)):
            for _ in range(int(len(tehai_m)/3)):
                if tehai_del(tehai_d, i) != 0:
                    if (tehai_del(tehai_d, i)[1][0] == tehai_del(tehai_d, i)[1][1] and tehai_del(tehai_d, i)[1][1] == tehai_del(tehai_d, i)[1][2]):
                        tehai_111.append(tehai_del(tehai_d, i)[1])
                    else:
                        tehai_123.append(tehai_del(tehai_d, i)[1])
                    tehai_d = tehai_del(tehai_d, i)[0]
                    i = 0
                else:
                    break
            if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
                break
            else:
                tehai_111 = []
                tehai_123 = []
                tehai_d = copy.deepcopy(tehai_m)
                tehai_d.sort()
        if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
            tehai_111.sort()
            if len(tehai_111) >= (3-kan):
                return True
        tehai_111 = []
        tehai_123 = []
        tehai_d = copy.deepcopy(tehai_m)
        tehai_d.sort(reverse=True)
        for i in range(len(tehai_m)):
            for _ in range(int(len(tehai_m)/3)):
                if tehai_del_re(tehai_d, i) != 0:
                    if (tehai_del_re(tehai_d, i)[1][0] == tehai_del_re(tehai_d, i)[1][1] and tehai_del_re(tehai_d, i)[1][1] == tehai_del_re(tehai_d, i)[1][2]):
                        tehai_111.append(tehai_del_re(tehai_d, i)[1])
                    else:
                        tehai_123.append(tehai_del_re(tehai_d, i)[1])
                    tehai_d = tehai_del_re(tehai_d, i)[0]
                    i = 0
                else:
                    break
            if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
                break
            else:
                tehai_111 = []
                tehai_123 = []
                tehai_d = copy.deepcopy(tehai_m)
                tehai_d.sort(reverse=True)
        if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
            tehai_111.sort()
            if len(tehai_111) >= (3-kan):
                return True
    else:
        tehai_111 = []
        tehai_123 = []
        tehai_d = copy.deepcopy(tehai_m)
        tehai_d.sort()
        for i in range(len(tehai_m)):
            for _ in range(int(len(tehai_m)/3)):
                if tehai_del(tehai_d, i) != 0:
                    if (tehai_del(tehai_d, i)[1][0] == tehai_del(tehai_d, i)[1][1] and tehai_del(tehai_d, i)[1][1] == tehai_del(tehai_d, i)[1][2]):
                        tehai_111.append(tehai_del(tehai_d, i)[1])
                    else:
                        tehai_123.append(tehai_del(tehai_d, i)[1])
                    tehai_d = tehai_del(tehai_d, i)[0]
                    i = 0
                else:
                    break
            if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
                break
            else:
                tehai_111 = []
                tehai_123 = []
                tehai_d = copy.deepcopy(tehai_m)
                tehai_d.sort()
        if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
            tehai_111.sort()
            if len(tehai_111) >= 3:
                return True
        tehai_111 = []
        tehai_123 = []
        tehai_d = copy.deepcopy(tehai_m)
        tehai_d.sort(reverse=True)
        for i in range(len(tehai_m)):
            for _ in range(int(len(tehai_m)/3)):
                if tehai_del_re(tehai_d, i) != 0:
                    if (tehai_del_re(tehai_d, i)[1][0] == tehai_del_re(tehai_d, i)[1][1] and tehai_del_re(tehai_d, i)[1][1] == tehai_del_re(tehai_d, i)[1][2]):
                        tehai_111.append(tehai_del_re(tehai_d, i)[1])
                    else:
                        tehai_123.append(tehai_del_re(tehai_d, i)[1])
                    tehai_d = tehai_del_re(tehai_d, i)[0]
                    i = 0
                else:
                    break
            if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
                break
            else:
                tehai_111 = []
                tehai_123 = []
                tehai_d = copy.deepcopy(tehai_m)
                tehai_d.sort(reverse=True)
        if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
            tehai_111.sort()
            if len(tehai_111) >= 3:
                return True
    return False


def suankou_sub(tehai, Menzen):
    tehai_m = copy.deepcopy(tehai[0])
    tehai_n = copy.deepcopy(tehai[1])
    tehai_m.sort()
    c = 0
    if Menzen:
        kan = 0
        if tehai_n != [0]:
            kan = len(tehai_m) + len(tehai_n) - 14
        atama = 0
        while len(tehai_m) > 0:
            hai = tehai_m[0]
            if tehai_m.count(hai) == 3:
                for _ in range(3):
                    tehai_m.pop(0)
                c += 1
            elif tehai_m[0] == tehai_m[1] and atama == 0:
                for _ in range(2):
                    tehai_m.pop(0)
                    atama = 1
            else:
                break

        if c == (4-kan):
            return True
    return False


def toitoi_sub(tehai):
    tehai_m = copy.deepcopy(tehai[0])
    tehai_n = copy.deepcopy(tehai[1])
    tehai_m.sort()
    atama = 0
    while len(tehai_m) > 0:
        if len(tehai_m) > 2:
            if tehai_m[0] == tehai_m[1] and tehai_m[1] == tehai_m[2]:
                for _ in range(3):
                    tehai_m.pop(0)
            elif tehai_m[0] == tehai_m[1] and atama == 0:
                for _ in range(2):
                    tehai_m.pop(0)
                atama = 1
            else:
                return False
        elif len(tehai_m) == 2:
            if tehai_m[0] == tehai_m[1] and atama == 0:
                for _ in range(2):
                    tehai_m.pop(0)
                atama = 1
            else:
                return False
        else:
            return False
    while len(tehai_n) > 0 and tehai_n != [0]:
        if tehai_n[0] >= 100:
            for _ in range(4):
                tehai_n.pop(0)
        elif tehai_n[0] == tehai_n[1] and tehai_n[1] == tehai_n[2]:
            for _ in range(3):
                tehai_n.pop(0)
        else:
            return False
    return True


def honroutou_sub(tehai):
    tehai_m = copy.deepcopy(tehai[0])
    tehai_n = copy.deepcopy(tehai[1])
    tehai_m.sort()
    tehai_111 = []
    atama = 0
    while len(tehai_m) > 0:
        if len(tehai_m) > 2:
            if tehai_m[0] == tehai_m[1] and tehai_m[1] == tehai_m[2]:
                tehai_111.append([tehai_m[0],tehai_m[0],tehai_m[0]])
                for _ in range(3):
                    tehai_m.pop(0)
            elif tehai_m[0] == tehai_m[1] and atama == 0:
                if (1 < tehai_m[0] and 9 > tehai_m[0]) or (10 < tehai_m[0] and 18 > tehai_m[0]) or (19 < tehai_m[0] and 27 > tehai_m[0]):
                    return False
                for _ in range(2):
                    tehai_m.pop(0)
                atama = 1
            else:
                return False
        elif len(tehai_m) == 2:
            if tehai_m[0] == tehai_m[1] and atama == 0:
                if (1 < tehai_m[0] and 9 > tehai_m[0]) or (10 < tehai_m[0] and 18 > tehai_m[0]) or (19 < tehai_m[0] and 27 > tehai_m[0]):
                    return False
                for _ in range(2):
                    tehai_m.pop(0)
                atama = 1
        else:
            return False
    while len(tehai_n) > 0 and tehai_n != [0]:
        if tehai_n[0] >= 100:
            hai = float(Decimal(str(tehai_n[1])) - Decimal("100"))
            tehai_111.append([hai,hai,hai])
            for _ in range(4):
                tehai_n.pop(0)
        elif tehai_n[0] == tehai_n[1] and tehai_n[1] == tehai_n[2]:
            tehai_111.append([tehai_n[0],tehai_n[0],tehai_n[0]])
            for _ in range(3):
                tehai_n.pop(0)
        else:
            return False
    for hais in tehai_111:
        if (1 < hais[0] and 9 > hais[0]) or (10 < hais[0] and 18 > hais[0]) or (19 < hais[0] and 27 > hais[0]):
            return False
    return True


def chinroutou_sub(tehai):
    tehai_m = copy.deepcopy(tehai[0])
    tehai_n = copy.deepcopy(tehai[1])
    tehai_m.sort()
    tehai_111 = []
    atama = 0
    while len(tehai_m) > 0:
        if len(tehai_m) > 2:
            if tehai_m[0] == tehai_m[1] and tehai_m[1] == tehai_m[2]:
                tehai_111.append([tehai_m[0],tehai_m[0],tehai_m[0]])
                for _ in range(3):
                    tehai_m.pop(0)
            elif tehai_m[0] == tehai_m[1] and atama == 0:
                if (1 < tehai_m[0] and 9 > tehai_m[0]) or (10 < tehai_m[0] and 18 > tehai_m[0]) or (19 < tehai_m[0] and 27 > tehai_m[0]) or 27 < tehai_m[0]:
                    return False
                for _ in range(2):
                    tehai_m.pop(0)
                atama = 1
            else:
                return False
        elif len(tehai_m) == 2:
            if tehai_m[0] == tehai_m[1] and atama == 0:
                if (1 < tehai_m[0] and 9 > tehai_m[0]) or (10 < tehai_m[0] and 18 > tehai_m[0]) or (19 < tehai_m[0] and 27 > tehai_m[0]) or 27 < tehai_m[0]:
                    return False
                for _ in range(2):
                    tehai_m.pop(0)
                atama = 1
        else:
            return False
    while len(tehai_n) > 0 and tehai_n != [0]:
        if tehai_n[0] >= 100:
            hai = float(Decimal(str(tehai_n[1])) - Decimal("100"))
            tehai_111.append([hai,hai,hai])
            for _ in range(4):
                tehai_n.pop(0)
        elif tehai_n[0] == tehai_n[1] and tehai_n[1] == tehai_n[2]:
            tehai_111.append([tehai_n[0],tehai_n[0],tehai_n[0]])
            for _ in range(3):
                tehai_n.pop(0)
        else:
            return False
    for hais in tehai_111:
        if (1 < hais[0] and 9 > hais[0]) or (10 < hais[0] and 18 > hais[0]) or (19 < hais[0] and 27 > hais[0]) or 27 < hais[0]:
            return False
    return True


def chanta_sub(tehai):
    tehai_m = copy.deepcopy(tehai[0])
    tehai_n = copy.deepcopy(tehai[1])
    tehai_111 = []
    tehai_123 = []
    while len(tehai_n) > 0 and tehai_n != [0]:
        if tehai_n[0] >= 100:
            hai = float(Decimal(str(tehai_n[1])) - Decimal("100"))
            tehai_111.append([hai,hai,hai])
            for _ in range(4):
                tehai_n.pop(0)
        elif tehai_n[0] == tehai_n[1] and tehai_n[1] == tehai_n[2]:
            tehai_111.append([tehai_n[0],tehai_n[0],tehai_n[0]])
            for _ in range(3):
                tehai_n.pop(0)
        else:
            tehai_123.append([tehai_n[0],tehai_n[1],tehai_n[2]])
            for _ in range(3):
                tehai_n.pop(0)
    tehai_111_t = copy.deepcopy(tehai_111)
    tehai_123_t = copy.deepcopy(tehai_123)
    tehai_d = copy.deepcopy(tehai_m)
    tehai_d.sort()
    for i in range(len(tehai_m)):
        for _ in range(int(len(tehai_m)/3)):
            if tehai_del(tehai_d, i) != 0:
                if (tehai_del(tehai_d, i)[1][0] == tehai_del(tehai_d, i)[1][1] and tehai_del(tehai_d, i)[1][1] == tehai_del(tehai_d, i)[1][2]):
                    tehai_111_t.append(tehai_del(tehai_d, i)[1])
                else:
                    tehai_123_t.append(tehai_del(tehai_d, i)[1])
                tehai_d = tehai_del(tehai_d, i)[0]
                i = 0
            else:
                break
        if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
            j = 0
            if (1 < tehai_d[0] and 9 > tehai_d[0]) or (10 < tehai_d[0] and 18 > tehai_d[0]) or (19 < tehai_d[0] and 27 > tehai_d[0]):
                j = 1
            for hais in tehai_123_t:
                if not((1 in hais) or (9 in hais) or (10 in hais) or (18 in hais) or (19 in hais) or (27 in hais)):
                    j = 1
            for hais in tehai_111_t:
                if (1 < hais[0] and 9 > hais[0]) or (10 < hais[0] and 18 > hais[0]) or (19 < hais[0] and 27 > hais[0]):
                    j = 1
            if j == 0:
                return True
        else:
            tehai_111_t = copy.deepcopy(tehai_111)
            tehai_123_t = copy.deepcopy(tehai_123)
            tehai_d = copy.deepcopy(tehai_m)
            tehai_d.sort()
    tehai_111_t = copy.deepcopy(tehai_111)
    tehai_123_t = copy.deepcopy(tehai_123)
    tehai_d = copy.deepcopy(tehai_m)
    tehai_d.sort(reverse=True)
    for i in range(len(tehai_m)):
        for _ in range(int(len(tehai_m)/3)):
            if tehai_del_re(tehai_d, i) != 0:
                if (tehai_del_re(tehai_d, i)[1][0] == tehai_del_re(tehai_d, i)[1][1] and tehai_del_re(tehai_d, i)[1][1] == tehai_del_re(tehai_d, i)[1][2]):
                    tehai_111_t.append(tehai_del_re(tehai_d, i)[1])
                else:
                    tehai_123_t.append(tehai_del_re(tehai_d, i)[1])
                tehai_d = tehai_del_re(tehai_d, i)[0]
                i = 0
            else:
                break
        if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
            j = 0
            if (1 < tehai_d[0] and 9 > tehai_d[0]) or (10 < tehai_d[0] and 18 > tehai_d[0]) or (19 < tehai_d[0] and 27 > tehai_d[0]):
                j = 1
            for hais in tehai_123_t:
                if not((1 in hais) or (9 in hais) or (10 in hais) or (18 in hais) or (19 in hais) or (27 in hais)):
                    j = 1
            for hais in tehai_111_t:
                if (1 < hais[0] and 9 > hais[0]) or (10 < hais[0] and 18 > hais[0]) or (19 < hais[0] and 27 > hais[0]):
                    j = 1
            if j == 0:
                return True
        else:
            tehai_111_t = copy.deepcopy(tehai_111)
            tehai_123_t = copy.deepcopy(tehai_123)
            tehai_d = copy.deepcopy(tehai_m)
            tehai_d.sort(reverse=True)
    return False


def junchan_sub(tehai):
    tehai_m = copy.deepcopy(tehai[0])
    tehai_n = copy.deepcopy(tehai[1])
    tehai_111 = []
    tehai_123 = []
    while len(tehai_n) > 0 and tehai_n != [0]:
        if tehai_n[0] >= 100:
            hai = float(Decimal(str(tehai_n[1])) - Decimal("100"))
            tehai_111.append([hai,hai,hai])
            for _ in range(4):
                tehai_n.pop(0)
        elif tehai_n[0] == tehai_n[1] and tehai_n[1] == tehai_n[2]:
            tehai_111.append([tehai_n[0],tehai_n[0],tehai_n[0]])
            for _ in range(3):
                tehai_n.pop(0)
        else:
            tehai_123.append([tehai_n[0],tehai_n[1],tehai_n[2]])
            for _ in range(3):
                tehai_n.pop(0)
    tehai_111_t = copy.deepcopy(tehai_111)
    tehai_123_t = copy.deepcopy(tehai_123)
    tehai_d = copy.deepcopy(tehai_m)
    tehai_d.sort()
    for i in range(len(tehai_m)):
        for _ in range(int(len(tehai_m)/3)):
            if tehai_del(tehai_d, i) != 0:
                if (tehai_del(tehai_d, i)[1][0] == tehai_del(tehai_d, i)[1][1] and tehai_del(tehai_d, i)[1][1] == tehai_del(tehai_d, i)[1][2]):
                    tehai_111_t.append(tehai_del(tehai_d, i)[1])
                else:
                    tehai_123_t.append(tehai_del(tehai_d, i)[1])
                tehai_d = tehai_del(tehai_d, i)[0]
                i = 0
            else:
                break
        if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
            j = 0
            if (1 < tehai_d[0] and 9 > tehai_d[0]) or (10 < tehai_d[0] and 18 > tehai_d[0]) or (19 < tehai_d[0] and 27 > tehai_d[0]) or 27 < tehai_d[0]:
                j = 1
            for hais in tehai_123_t:
                if not((1 in hais) or (9 in hais) or (10 in hais) or (18 in hais) or (19 in hais) or (27 in hais)):
                    j = 1
            for hais in tehai_111_t:
                if (1 < hais[0] and 9 > hais[0]) or (10 < hais[0] and 18 > hais[0]) or (19 < hais[0] and 27 > hais[0]) or 27 < hais[0]:
                    j = 1
            if j == 0:
                return True
        else:
            tehai_111_t = copy.deepcopy(tehai_111)
            tehai_123_t = copy.deepcopy(tehai_123)
            tehai_d = copy.deepcopy(tehai_m)
            tehai_d.sort()
    tehai_111_t = copy.deepcopy(tehai_111)
    tehai_123_t = copy.deepcopy(tehai_123)
    tehai_d = copy.deepcopy(tehai_m)
    tehai_d.sort(reverse=True)
    for i in range(len(tehai_m)):
        for _ in range(int(len(tehai_m)/3)):
            if tehai_del_re(tehai_d, i) != 0:
                if (tehai_del_re(tehai_d, i)[1][0] == tehai_del_re(tehai_d, i)[1][1] and tehai_del_re(tehai_d, i)[1][1] == tehai_del_re(tehai_d, i)[1][2]):
                    tehai_111_t.append(tehai_del_re(tehai_d, i)[1])
                else:
                    tehai_123_t.append(tehai_del_re(tehai_d, i)[1])
                tehai_d = tehai_del_re(tehai_d, i)[0]
                i = 0
            else:
                break
        if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
            j = 0
            if (1 < tehai_d[0] and 9 > tehai_d[0]) or (10 < tehai_d[0] and 18 > tehai_d[0]) or (19 < tehai_d[0] and 27 > tehai_d[0]) or 27 < tehai_d[0]:
                j = 1
            for hais in tehai_123_t:
                if not((1 in hais) or (9 in hais) or (10 in hais) or (18 in hais) or (19 in hais) or (27 in hais)):
                    j = 1
            for hais in tehai_111_t:
                if (1 < hais[0] and 9 > hais[0]) or (10 < hais[0] and 18 > hais[0]) or (19 < hais[0] and 27 > hais[0]) or 27 < hais[0]:
                    j = 1
            if j == 0:
                return True
        else:
            tehai_111_t = copy.deepcopy(tehai_111)
            tehai_123_t = copy.deepcopy(tehai_123)
            tehai_d = copy.deepcopy(tehai_m)
            tehai_d.sort(reverse=True)
    return False


def ittuu_sub(tehai):
    tehai_m = copy.deepcopy(tehai[0])
    tehai_n = copy.deepcopy(tehai[1])
    tehai_111 = []
    tehai_123 = []
    while len(tehai_n) > 0 and tehai_n != [0]:
        if tehai_n[0] >= 100:
            hai = float(Decimal(str(tehai_n[1])) - Decimal("100"))
            tehai_111.append([hai,hai,hai])
            for _ in range(4):
                tehai_n.pop(0)
        elif tehai_n[0] == tehai_n[1] and tehai_n[1] == tehai_n[2]:
            tehai_111.append([tehai_n[0],tehai_n[0],tehai_n[0]])
            for _ in range(3):
                tehai_n.pop(0)
        else:
            tehai_123.append([tehai_n[0],tehai_n[1],tehai_n[2]])
            for _ in range(3):
                tehai_n.pop(0)
    tehai_111_t = copy.deepcopy(tehai_111)
    tehai_123_t = copy.deepcopy(tehai_123)
    tehai_d = copy.deepcopy(tehai_m)
    tehai_d.sort()
    for i in range(len(tehai_m)):
        for _ in range(int(len(tehai_m)/3)):
            if tehai_del(tehai_d, i) != 0:
                if (tehai_del(tehai_d, i)[1][0] == tehai_del(tehai_d, i)[1][1] and tehai_del(tehai_d, i)[1][1] == tehai_del(tehai_d, i)[1][2]):
                    tehai_111_t.append(tehai_del(tehai_d, i)[1])
                else:
                    tehai_123_t.append(tehai_del(tehai_d, i)[1])
                tehai_d = tehai_del(tehai_d, i)[0]
                i = 0
            else:
                break
        if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
            tehai_123_t.sort()
            if len(tehai_123_t) >= 3:
                for i in range(3):
                    hais_1 = [1 + (9*i), 2 + (9*i), 3 + (9*i)]
                    hais_2 = [4 + (9*i), 5 + (9*i), 6 + (9*i)]
                    hais_3 = [7 + (9*i), 8 + (9*i), 9 + (9*i)]
                    if (hais_1 in tehai_123_t) and (hais_2 in tehai_123_t) and (hais_3 in tehai_123_t):
                        return True
        else:
            tehai_111_t = copy.deepcopy(tehai_111)
            tehai_123_t = copy.deepcopy(tehai_123)
            tehai_d = copy.deepcopy(tehai_m)
            tehai_d.sort()
    tehai_111_t = copy.deepcopy(tehai_111)
    tehai_123_t = copy.deepcopy(tehai_123)
    tehai_d = copy.deepcopy(tehai_m)
    tehai_d.sort(reverse=True)
    for i in range(len(tehai_m)):
        for _ in range(int(len(tehai_m)/3)):
            if tehai_del_re(tehai_d, i) != 0:
                if (tehai_del_re(tehai_d, i)[1][0] == tehai_del_re(tehai_d, i)[1][1] and tehai_del_re(tehai_d, i)[1][1] == tehai_del_re(tehai_d, i)[1][2]):
                    tehai_111_t.append(tehai_del_re(tehai_d, i)[1])
                else:
                    tehai_123_t.append(tehai_del_re(tehai_d, i)[1])
                tehai_d = tehai_del_re(tehai_d, i)[0]
                i = 0
            else:
                break
        if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
            if len(tehai_123_t) >= 3:
                for i in range(3):
                    hais_1 = [1 + (9*i), 2 + (9*i), 3 + (9*i)]
                    hais_2 = [4 + (9*i), 5 + (9*i), 6 + (9*i)]
                    hais_3 = [7 + (9*i), 8 + (9*i), 9 + (9*i)]
                    if (hais_1 in tehai_123_t) and (hais_2 in tehai_123_t) and (hais_3 in tehai_123_t):
                        return True
        else:
            tehai_111_t = copy.deepcopy(tehai_111)
            tehai_123_t = copy.deepcopy(tehai_123)
            tehai_d = copy.deepcopy(tehai_m)
            tehai_d.sort(reverse=True)
    return False


def points_sub(tehai):
    tehai_m = copy.deepcopy(tehai[0])
    tehai_n = copy.deepcopy(tehai[1])
    tehai_111_n = []
    tehai_123_n = []
    while len(tehai_n) > 0 and tehai_n != [0]:
        if tehai_n[0] >= 100:
            hai = float(Decimal(str(tehai_n[1])) - Decimal("100"))
            tehai_111_n.append([tehai_n[0], hai, hai])#100, 3, 3
            for _ in range(4):
                tehai_n.pop(0)
        elif tehai_n[0] == tehai_n[1] and tehai_n[1] == tehai_n[2]:
            tehai_111_n.append([tehai_n[0],tehai_n[0],tehai_n[0]])
            for _ in range(3):
                tehai_n.pop(0)
        else:
            tehai_123_n.append([tehai_n[0],tehai_n[1],tehai_n[2]])
            for _ in range(3):
                tehai_n.pop(0)
    tehai_111_m = []
    tehai_123_m = []
    tehai_d = copy.deepcopy(tehai_m)
    tehai_d.sort()
    for i in range(len(tehai_m)):
        for _ in range(int(len(tehai_m)/3)):
            if tehai_del(tehai_d, i) != 0:
                if (tehai_del(tehai_d, i)[1][0] == tehai_del(tehai_d, i)[1][1] and tehai_del(tehai_d, i)[1][1] == tehai_del(tehai_d, i)[1][2]):
                    tehai_111_m.append(tehai_del(tehai_d, i)[1])
                else:
                    tehai_123_m.append(tehai_del(tehai_d, i)[1])
                tehai_d = tehai_del(tehai_d, i)[0]
                i = 0
            else:
                break
        if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
            return tehai_111_m, tehai_123_m, tehai_111_n, tehai_123_n, tehai_d[0]
        else:
            tehai_111_m = []
            tehai_123_m = []
            tehai_d = copy.deepcopy(tehai_m)
            tehai_d.sort()
    tehai_111_m = []
    tehai_123_m = []
    tehai_d = copy.deepcopy(tehai_m)
    tehai_d.sort(reverse=True)
    for i in range(len(tehai_m)):
        for _ in range(int(len(tehai_m)/3)):
            if tehai_del_re(tehai_d, i) != 0:
                if (tehai_del_re(tehai_d, i)[1][0] == tehai_del_re(tehai_d, i)[1][1] and tehai_del_re(tehai_d, i)[1][1] == tehai_del_re(tehai_d, i)[1][2]):
                    tehai_111_m.append(tehai_del_re(tehai_d, i)[1])
                else:
                    tehai_123_m.append(tehai_del_re(tehai_d, i)[1])
                tehai_d = tehai_del_re(tehai_d, i)[0]
                i = 0
            else:
                break
        if tehai_d[0] == tehai_d[1] and len(tehai_d) == 2:
            j = 0
            return tehai_111_m, tehai_123_m, tehai_111_n, tehai_123_n, tehai_d[0]
        else:
            tehai_111_m = []
            tehai_123_m = []
            tehai_d = copy.deepcopy(tehai_m)
            tehai_d.sort(reverse=True)



def tehai_del_pinfu(tehai_m, n=0):#list[]
    tehai_0 = copy.deepcopy(tehai_m)
    for i in range(n, len(tehai_0)):
        result_del = del_3_123(tehai_0, i)
        #print(result_del)
        if result_del != 0:
            return result_del
    return 0


def tehai_del_re_pinfu(tehai_m, n=0):#list[]
    tehai_0 = copy.deepcopy(tehai_m)
    for i in range(n, len(tehai_0)):
        result_del = del_3_re_123(tehai_0, i)
        #print(result_del)
        if result_del != 0:
            return result_del
    return 0
    

def tehai_del(tehai_m, n=0):#list[]
    tehai_0 = copy.deepcopy(tehai_m)
    for i in range(n, len(tehai_m)):
        result_del = del_3(tehai_0, i)
        if result_del != 0:
            return result_del
    return 0


def tehai_del_re(tehai_m, n=0):#list[]
    tehai_0 = copy.deepcopy(tehai_m)
    for i in range(n, len(tehai_m)):
        result_del = del_3_re(tehai_0, i)
        if result_del != 0:
            return result_del
    return 0


def del_3(tehai, i):#list[],int
    j = 0
    del_hais = []
    max_l = len(tehai)
    for a in range(i, max_l):
        for b in range(a+1, max_l):
            for c in range(b+1, max_l):
                x = tehai[a]
                y = tehai[b]
                z = tehai[c]
                if (x < 10 and y < 10 and z < 10):
                    #print(a,b,c)
                    if (x == y and y == z):
                        del_hais.append(tehai[a])
                        del_hais.append(tehai[b])
                        del_hais.append(tehai[c])
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    elif (x+1 == y and y+1 == z):
                        del_hais.append(tehai[a])
                        del_hais.append(tehai[b])
                        del_hais.append(tehai[c])
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    else:
                        continue
                elif (x > 9 and y > 9 and z > 9) and (x < 19 and y < 19 and z < 19):
                    #print(a,b,c)
                    if (x == y and y == z):
                        del_hais.append(tehai[a])
                        del_hais.append(tehai[b])
                        del_hais.append(tehai[c])
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    elif (x+1 == y and y+1 == z):
                        del_hais.append(tehai[a])
                        del_hais.append(tehai[b])
                        del_hais.append(tehai[c])
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    else:
                        continue
                elif (x > 18 and y > 18 and z > 18) and (x < 28 and y < 28 and z < 28):
                    #print(a,b,c)
                    if (x == y and y == z):
                        del_hais.append(tehai[a])
                        del_hais.append(tehai[b])
                        del_hais.append(tehai[c])
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    elif (x+1 == y and y+1 == z):
                        del_hais.append(tehai[a])
                        del_hais.append(tehai[b])
                        del_hais.append(tehai[c])
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    else:
                        continue
                elif (x > 27 and y > 27 and z > 27):
                    if(x == y and y == z):
                        del_hais.append(tehai[a])
                        del_hais.append(tehai[b])
                        del_hais.append(tehai[c])
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    else:
                        continue
                if j == 1:
                    break
            if j == 1:
                break
        if j == 1:
            break
    del_hais.sort()
    try:
        for a in range(3):
            tehai.remove(0)
        return [tehai, del_hais]
    except:
        return 0
    

def del_3_re(tehai, i):#list[],int
    j = 0
    del_hais = []
    max_l = len(tehai)
    for a in range(i, max_l):
        for b in range(a+1, max_l):
            for c in range(b+1, max_l):
                x = tehai[a]
                y = tehai[b]
                z = tehai[c]
                if (x < 10 and y < 10 and z < 10):
                    #print(a,b,c)
                    if (x == y and y == z):
                        del_hais.append(tehai[a])
                        del_hais.append(tehai[b])
                        del_hais.append(tehai[c])
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    elif (x-1 == y and y-1 == z):
                        del_hais.append(tehai[a])
                        del_hais.append(tehai[b])
                        del_hais.append(tehai[c])
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    else:
                        continue
                elif (x > 9 and y > 9 and z > 9) and (x < 19 and y < 19 and z < 19):
                    #print(a,b,c)
                    if (x == y and y == z):
                        del_hais.append(tehai[a])
                        del_hais.append(tehai[b])
                        del_hais.append(tehai[c])
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    elif (x-1 == y and y-1 == z):
                        del_hais.append(tehai[a])
                        del_hais.append(tehai[b])
                        del_hais.append(tehai[c])
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    else:
                        continue
                elif (x > 18 and y > 18 and z > 18) and (x < 28 and y < 28 and z < 28):
                    #print(a,b,c)
                    if (x == y and y == z):
                        del_hais.append(tehai[a])
                        del_hais.append(tehai[b])
                        del_hais.append(tehai[c])
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    elif (x-1 == y and y-1 == z):
                        del_hais.append(tehai[a])
                        del_hais.append(tehai[b])
                        del_hais.append(tehai[c])
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    else:
                        continue
                elif (x > 27 and y > 27 and z > 27):
                    if(x == y and y == z):
                        del_hais.append(tehai[a])
                        del_hais.append(tehai[b])
                        del_hais.append(tehai[c])
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    else:
                        continue
                if j == 1:
                    break
            if j == 1:
                break
        if j == 1:
            break
    del_hais.sort()
    try:
        for a in range(3):
            tehai.remove(0)
        return [tehai, del_hais]
    except:
        return 0


def del_3_123(tehai, i): # 順子
    j = 0
    del_hais = []
    max_l = len(tehai)
    for a in range(i, max_l):
        for b in range(a+1, max_l):
            for c in range(b+1, max_l):
                x = tehai[a]
                y = tehai[b]
                z = tehai[c]
                if (x < 10 and y < 10 and z < 10):
                    #print(a,b,c)
                    if (x+1 == y and y+1 == z):
                        del_hais.append(tehai[a])
                        del_hais.append(tehai[b])
                        del_hais.append(tehai[c])
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    else:
                        continue
                elif (x > 9 and y > 9 and z > 9) and (x < 19 and y < 19 and z < 19):
                    #print(a,b,c)
                    if (x+1 == y and y+1 == z):
                        del_hais.append(tehai[a])
                        del_hais.append(tehai[b])
                        del_hais.append(tehai[c])
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    else:
                        continue
                elif (x > 18 and y > 18 and z > 18) and (x < 28 and y < 28 and z < 28):
                    #print(a,b,c)
                    if (x+1 == y and y+1 == z):
                        del_hais.append(tehai[a])
                        del_hais.append(tehai[b])
                        del_hais.append(tehai[c])
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    else:
                        continue
                elif (x > 27 and y > 27 and z > 27):
                    continue
                if j == 1:
                    break
            if j == 1:
                break
        if j == 1:
            break
    del_hais.sort()
    try:
        for _ in range(3):
            tehai.remove(0)
        return [tehai, del_hais]
    except:
        return 0
    

def del_3_re_123(tehai, i): # 順子
    j = 0
    del_hais = []
    max_l = len(tehai)
    for a in range(i, max_l):
        for b in range(a+1, max_l):
            for c in range(b+1, max_l):
                x = tehai[a]
                y = tehai[b]
                z = tehai[c]
                if (x < 10 and y < 10 and z < 10):
                    if (x-1 == y and y-1 == z):
                        del_hais.append(tehai[a])
                        del_hais.append(tehai[b])
                        del_hais.append(tehai[c])
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    else:
                        continue
                elif (x > 9 and y > 9 and z > 9) and (x < 19 and y < 19 and z < 19):
                    #print(a,b,c)
                    if (x-1 == y and y-1 == z):
                        del_hais.append(tehai[a])
                        del_hais.append(tehai[b])
                        del_hais.append(tehai[c])
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    else:
                        continue
                elif (x > 18 and y > 18 and z > 18) and (x < 28 and y < 28 and z < 28):
                    #print(a,b,c)
                    if (x-1 == y and y-1 == z):
                        del_hais.append(tehai[a])
                        del_hais.append(tehai[b])
                        del_hais.append(tehai[c])
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    else:
                        continue
                elif (x > 27 and y > 27 and z > 27):    
                    continue
                if j == 1:
                    break
            if j == 1:
                break
        if j == 1:
            break
    del_hais.sort()
    try:
        for _ in range(3):
            tehai.remove(0)
        return [tehai, del_hais]
    except:
        return 0



if __name__ == "__main__":
    tehai_m = [[1,2,3,7,8,9,19,20,21,27,27],[9,9,9]]
    tehai_m_g = [10,11,12,13,14,15,16,17,18,10,10,10,12,12]
    Menzen = True
    print(chanta_sub(tehai_m))